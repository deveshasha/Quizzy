from django.shortcuts import render
from .models import Question,Phpquestion
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from itertools import chain

javalist = Question.objects.order_by('q_id')[:5]
phplist = Phpquestion.objects.order_by('q_id')[:5]

def test(request):
    return render(request, 'test.html')

def index(request):
    if request.user.is_authenticated():
        latest_question_list = chain(javalist,phplist)
        return render(request,'index.html',{'latest_question_list': latest_question_list})
    else:
        return HttpResponse("Please login before continuing.")

def result(request):
    i = 1
    ch = [0]
    correct = 0
    for i in range(1,6):
        s = request.POST.get(str(i))
        question, choice = s.split('-')
        ch.append(choice)
        #print ch
        jobjects = Question.objects.get(pk=i)
        if jobjects.ans == ch[i]:
            correct+=1
    for i in range(1,6):
        s = request.POST.get(str(i+5))
        question, choice = s.split('-')
        ch.append(choice)
        #print ch
        phpobjects = Phpquestion.objects.get(pk=i)
        if phpobjects.ans == ch[i+5]:
            correct+=1

    return HttpResponse(correct)