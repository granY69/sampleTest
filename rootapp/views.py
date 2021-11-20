from django.shortcuts import render
from django.http import HttpResponse, response, Http404
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-p_date')[:5]
    template = loader.get_template('rootapp/index.html')
    context = {
        'latest_question_list' : latest_question_list
    }
    return HttpResponse(template.render(context, request))
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'rootapp/details.html', {'question': question})
def results(request, question_id):
    return HttpResponse("You are looking at the results of the question %s" %question_id)
def vote(request, question_id):
    return HttpResponse("You are voting on question %s" %question_id)

def owner(request):
    return HttpResponse("Hello, world. 14bc3485 is the polls index.")