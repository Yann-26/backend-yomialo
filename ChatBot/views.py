from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Conversation
from .serializers import ConversationSerializer
from openai import OpenAI

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def save_conversation(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user_message = data.get('user_message')

        if user_message:
            client = OpenAI()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}],
                stream=True,
            )

            bot_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    bot_response += chunk.choices[0].delta.content

            conversation = Conversation(user_message=user_message, bot_response=bot_response)
            conversation.save()

            serializer = ConversationSerializer(conversation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"error": "user_message not provided"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_conversations(request):
    if request.method == 'GET':
        conversations = Conversation.objects.all().order_by('-timestamp')
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)