from django.shortcuts import render
from .models import Question,Phpquestion
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from itertools import chain
from polls.forms import *

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

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