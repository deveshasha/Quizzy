from django.shortcuts import render
from .models import Question,Phpquestion,Userprof
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
#from itertools import chain
from polls.forms import *
import random,json
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
        request.session['jlist'] = [j.q_id for j in jlist]
        return render(request,'index.html',{'latest_question_list': jlist})
    else:
        return HttpResponse("Please login before continuing.")

def javaresult(request):
    ch = []
    correct = 0
    idlist = request.session['jlist']
    jlist = []
    for i in idlist:
        jlist.append(Question.objects.get(pk=i))
    answers = []
    for j in jlist:
        answers.append(j.ans)

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

    lisst = zip(jlist,ch)

    up = Userprof.objects.create(username=request.user.username,subject='java',score=correct)

    return render(request,'result.html',{'qlist':lisst,'score':correct})

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

    up = Userprof.objects.create(username=request.user.username,subject='php',score=correct)

    return render(request,'result.html',{'qlist':lisst,'score':correct})

def show_javachart(request):
    userss = Userprof.objects.filter(username__exact=request.user.username,subject__exact='java')
    c=1
    array = [['TestNumber', 'Java'],[0,0]]
    tickcount = [0]
    for u in userss:
        temp=[]
        temp.append(int(c))
        temp.append(int(u.score))
        array.append(temp)
        tickcount.append(c)
        c+=1

    return render(request,'chart.html', {'array': json.dumps(array),'tickcount':json.dumps(tickcount)})

def show_phpchart(request):
    userss = Userprof.objects.filter(username__exact=request.user.username,subject__exact='php')
    c=1
    array = [['TestNumber', 'PHP'],[0,0]]
    tickcount = [0]
    for u in userss:
        temp=[]
        temp.append(int(c))
        temp.append(int(u.score))
        array.append(temp)
        tickcount.append(c)
        c+=1

    return render(request,'chart.html', {'array': json.dumps(array),'tickcount':json.dumps(tickcount)})

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