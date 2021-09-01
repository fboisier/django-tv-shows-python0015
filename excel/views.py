import csv

from django.http import HttpResponse
from django.contrib.auth.models import User
from app.models import Show

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response,delimiter=';')
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response

def export_shows(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="shows.csv"'

    writer = csv.writer(response,delimiter=';')
    writer.writerow(['TV Name', 'Descripción'])

    # shows = Show.objects.all().values_list('title', 'description')
    shows = Show.objects.all()
    for s in shows:
        writer.writerow([s.title, s.description])

    return response