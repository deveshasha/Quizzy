from django.shortcuts import render
from .models import Question,Phpquestion
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
#from itertools import chain
from polls.forms import *
import random
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.core import serializers


def test(request):
    return render(request, 'test.html')

def javaindex(request):
    if request.user.is_authenticated():
        javapool = list(Question.objects.all())
        random.shuffle(javapool)
        jlist = javapool[:10]
        request.session['jlist'] = [j.ans for j in jlist]
        return render(request,'index.html',{'latest_question_list': jlist})
    else:
        return HttpResponse("Please login before continuing.")

def javaresult(request):
    ch = []
    correct = 0
    jlist = request.session['jlist'] 
    for i in range(1,11):
        s = request.POST.get(str(i))
        if s:
            question, choice = s.split('-')
            ch.append(choice)
        else:
            ch.append(None)
    for i in range(0,10):
        if ch[i] == jlist[i]:
            correct+=1
    return HttpResponse(correct)

def phpindex(request):
    if request.user.is_authenticated():
        phppool = list(Phpquestion.objects.all())
        random.shuffle(phppool)
        phplist = phppool[:10]
        request.session['plist'] = [p.ans for p in phplist]
        return render(request,'index.html',{'latest_question_list': phplist})
    else:
        return HttpResponse("Please login before continuing.")

def phpresult(request):
    ch = []
    correct = 0
    phplist = request.session['plist'] 
    for i in range(1,11):
        s = request.POST.get(str(i))
        if s:
            question, choice = s.split('-')
            ch.append(choice)
        else:
            ch.append(None)
    for i in range(0,10):
        if ch[i] == phplist[i]:
            correct+=1
    return HttpResponse(correct)

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')
            

            # Email the profile with the 
            # contact information
            template = get_template('polls/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render({'context':context})

            email = EmailMessage(
                "New contact form submission",
                content,
                "QuizUp" +'',
                ['quizup@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return HttpResponseRedirect('contact')

    return render(request, 'polls/contact.html', {
        'form': form_class,
    })