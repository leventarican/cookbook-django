from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Question

# reach this site here: http://127.0.0.1:8000/polls/
# a view called index. the URL map is done in app/urls.py (e.g. polls/urls.py)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("details view/page: %s" % question_id)

def results(request, question_id):
    return HttpResponse("results view/page: %s" % question_id)

def vote(request, question_id):
    return HttpResponse("vote view/page: %s" % question_id)
