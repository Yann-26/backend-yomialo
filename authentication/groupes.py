from django.contrib.auth.models import Group, Permission

def create_groups():
    patient_group, created = Group.objects.get_or_create(name='Patients')
    courier_group, created = Group.objects.get_or_create(name='Couriers')
    admin_group, created = Group.objects.get_or_create(name='Administrators')

    # Assigner les permissions selon les besoins, par exemple :
    # admin_group.permissions.add(...)
