
from django.template import loader, TemplateDoesNotExist
from django import template
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from pharmacies.models import *


def is_admin(user):
    return user.is_authenticated and user.is_superuser


User = get_user_model()

@login_required(login_url="/login/")
@user_passes_test(is_admin)
def index(request):
    user = User.objects
    current_user_count = user.count()
    pharmacies = Pharmacie.objects.all()
    context = {
        'segment': 'index',
        'pharmacies': pharmacies,
        'user': current_user_count
        }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        # Remove 'pages/' prefix from the URL path
        load_template = request.path.lstrip('/').replace('pages/', '')

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        print(f"Unexpected error: {e}")  # Log the exception for debugging
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
