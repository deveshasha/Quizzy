from django.shortcuts import render
from .models import Question,Phpquestion,Userprof
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
        # userlist = Userprof.objects.all()
        # for u in userlist:
        #     print u.username
        javapool = list(Question.objects.all())
        random.shuffle(javapool)
        jlist = javapool[:15]
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
        request.session['phplist'] = [p.q_id for p in phplist]
        return render(request,'index.html',{'latest_question_list': phplist})
    else:
        return HttpResponse("Please login before continuing.")

def phpresult(request):
    ch = []
    correct = 0
    # phplist = Phpquestion.objects.filter(q_id__in=request.session['phplist'])
    idlist = request.session['phplist']
    phplist = []
    for i in idlist:
        phplist.append(Phpquestion.objects.get(pk=i))
    answers = []
    for p in phplist:
        answers.append(p.ans)

    for i in range(1,11):
        s = request.POST.get(str(i))
        if s:
            question, choice = s.split('-')
            ch.append(choice)
        else:
            ch.append(None)
    
    for i in range(0,10):
        if ch[i] == answers[i]:
            correct+=1
    lisst = zip(phplist,ch)
    return render(request,'result.html',{'qlist':lisst,'score':correct})

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
                "Quizzy" +'',
                ['quizzy2016@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return HttpResponseRedirect('contact')

    return render(request, 'polls/contact.html', {
        'form': form_class,
    })

def submitq(request):
    form_class = QuestionForm

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
            template = get_template('polls/question1.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render({'context':context})
            email = EmailMessage(
                "User has Entered",
                content,
                "" +'',
                [''],
                headers = {'': contact_email }
            )
            email.send()
            return HttpResponseRedirect('/submitq')

    return render(request, 'polls/question.html', {
        'form': form_class,
    })