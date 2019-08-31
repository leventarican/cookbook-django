from django.http import HttpResponse

# reach this site here: http://127.0.0.1:8000/polls/
# a view called index. the URL map is done in app/urls.py (e.g. polls/urls.py)
def index(request):
    return HttpResponse("[app polls view index]")
