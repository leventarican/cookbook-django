from django.http import HttpResponse
from django.http import Http404
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    return HttpResponse("vote view/page: %s" % question_id)

from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    """API endpoint for listing and creating questions."""
    queryset = Question.objects.order_by('end')
    serializer_class = QuestionSerializer
