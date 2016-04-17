import random,json
from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.core import serializers
from django.db.models import Max
from .models import Question,Phpquestion,Userprof,ContactDetails,UserQuestions,Pythonquestion
from polls.forms import *


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
        return HttpResponseRedirect('/')

def javaresult(request):
    if request.user.is_authenticated():
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
    else:
        return HttpResponseRedirect('/')

def mixindex(request):
    if request.user.is_authenticated():
        jpool = Question.objects.all()
        ppool = Phpquestion.objects.all()
        pypool = Pythonquestion.objects.all()
        mixlist = list(chain(jpool,ppool,pypool))
        random.shuffle(mixlist)
        mlist = mixlist[:10]
        request.session['mlist'] = [m.all_id for m in mlist]
        return render(request,'index.html',{'latest_question_list': mlist})
    else:
        return HttpResponseRedirect('/')

def mixresult(request):
    if request.user.is_authenticated():
        ch = []
        correct = 0
        idlist = request.session['mlist']
        qlist = []
        for i in idlist:
            if i>=1 and i<=31:
                qlist.append(Question.objects.get(all_id=i))
            elif i>=32 and i<=61:
                qlist.append(Phpquestion.objects.get(all_id=i))
            else:
                qlist.append(Pythonquestion.objects.get(all_id=i))
        answers = []
        for q in qlist:
            answers.append(q.ans)
        for i in range(1,11):
            s = request.POST.get(str(i))
            if s:
                question,choice = s.split('-')
                ch.append(choice)
            else:
                ch.append(None)
        for i in range(0,10):
            if ch[i] == answers[i]:
                correct+=1
        lisst = zip(qlist,ch)
        # u = Userprof.objects create
        return render(request,'result.html',{'qlist':lisst,'score':correct})
    else:
        return HttpResponseRedirect('/')

def phpindex(request):
    if request.user.is_authenticated():
        phppool = list(Phpquestion.objects.all())
        random.shuffle(phppool)
        phplist = phppool[:10]
        request.session['phplist'] = [p.q_id for p in phplist]
        return render(request,'index.html',{'latest_question_list': phplist})
    else:
        return HttpResponseRedirect('/')

def phpresult(request):
    if request.user.is_authenticated():
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
    else:
        return HttpResponseRedirect('/')

def pythonindex(request):
    if request.user.is_authenticated():
        pypool = list(Pythonquestion.objects.all())
        random.shuffle(pypool)
        pylist = pypool[:10]
        request.session['pylist'] = [p.q_id for p in pylist]
        return render(request,'index.html',{'latest_question_list': pylist})
    else:
        return HttpResponseRedirect('/')

def pythonresult(request):
    if request.user.is_authenticated():
        ch = []
        correct = 0
        idlist = request.session['pylist']
        pylist = []
        for i in idlist:
            pylist.append(Pythonquestion.objects.get(pk=i))
        answers = []
        for p in pylist:
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

        lisst = zip(pylist,ch)

        up = Userprof.objects.create(username=request.user.username,subject='python',score=correct)

        return render(request,'result.html',{'qlist':lisst,'score':correct})
    else:
        return HttpResponseRedirect('/')

def show_perfindex(request):
    if request.user.is_authenticated():
        userj = Userprof.objects.filter(username__exact=request.user.username,subject__exact='java')
        userp = Userprof.objects.filter(username__exact=request.user.username,subject__exact='php')
        userpy = Userprof.objects.filter(username__exact=request.user.username,subject__exact='python')
        return render(request,'performance.html',{'userj':userj,'userp':userp,'userpy':userpy})
    else:
        return HttpResponseRedirect('/')

def show_javachart(request):
    if request.user.is_authenticated():
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
    else:
        return HttpResponseRedirect('/')

def show_phpchart(request):
    if request.user.is_authenticated():
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
    else:
        return HttpResponseRedirect('/')

def show_pychart(request):
    if request.user.is_authenticated():
        userss = Userprof.objects.filter(username__exact=request.user.username,subject__exact='python')
        c=1
        array = [['TestNumber', 'Python'],[0,0]]
        tickcount = [0]
        for u in userss:
            temp=[]
            temp.append(int(c))
            temp.append(int(u.score))
            array.append(temp)
            tickcount.append(c)
            c+=1

        return render(request,'chart.html', {'array': json.dumps(array),'tickcount':json.dumps(tickcount)})
    else:
        return HttpResponseRedirect('/')

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            FormObj = ContactDetails(username=contact_name,email=contact_email,content=form_content)
            FormObj.save()
            # Email the profile with the 
            # contact information
            template = get_template('polls/contact_template.txt')
            context = {'contact_name': contact_name,'contact_email': contact_email,'form_content': form_content,}
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
    return render(request, 'polls/contact.html', {'form': form_class,})

def submitq(request):
    form_class = QuestionForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            FormObj = UserQuestions(username=contact_name,email=contact_email,question=form_content)
            FormObj.save()

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

    return render(request, 'polls/question.html', {'form': form_class,})

def showleadindex(request):
    return render(request,'polls/mainleaderboard.html')

def javaleaderboard(request):
    p = Userprof.objects.values('username','subject').annotate(score=Max('score')).order_by('-score')
    jp = p.filter(subject__exact='java')
    subj = 'Java'
    return render(request, 'polls/leaderboard.html',{'p':jp,'subj':subj})

def phpleaderboard(request):
    p = Userprof.objects.values('username','subject').annotate(score=Max('score')).order_by('-score')
    pp = p.filter(subject__exact='php')
    subj = 'PHP'
    return render(request, 'polls/leaderboard.html',{'p':pp,'subj':subj})

def pyleaderboard(request):
    p = Userprof.objects.values('username','subject').annotate(score=Max('score')).order_by('-score')
    pp = p.filter(subject__exact='python')
    subj = 'Python'
    return render(request, 'polls/leaderboard.html',{'p':pp,'subj':subj})

def handler404(request):
    return render(request,'404.html')

def handler500(request):
    return render(request,'500.html')