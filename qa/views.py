from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from qa.models import Question
# Create your views here.

python_users = 0
network_users = 0


def index(req):
    return render(req, 'qa/index.html')


def initial(req):
    return HttpResponse(python_users)


def get_users_py(req):
    return HttpResponse(python_users)


def get_users_cn(req):
    return HttpResponse(network_users)


def python(req):
    global python_users
    ques = list(Question.objects.all())
    mydict = {}
    final_dict = {}
    numbering = 0

    for i in range(len(ques)):
        if(ques[i].cat == 'python'):
            mydict['ques'] = ques[i].ques
            mydict['ans1'] = ques[i].ans1
            mydict['ans2'] = ques[i].ans2
            mydict['ans3'] = ques[i].ans3
            mydict['ans4'] = ques[i].ans4
            mydict['correct'] = ques[i].correct_answer
            final_dict['question'+str(numbering)] = mydict
            numbering += 1

        mydict = {}
    python_users += 1
    final_dict['users'] = python_users
    return JsonResponse(final_dict)


def networks(req):
    global network_users
    ques = list(Question.objects.all())
    mydict = {}
    final_dict = {}
    numbering = 0
    for i in range(len(ques)):
        if(ques[i].cat == 'cn'):
            mydict['ques'] = ques[i].ques
            mydict['ans1'] = ques[i].ans1
            mydict['ans2'] = ques[i].ans2
            mydict['ans3'] = ques[i].ans3
            mydict['ans4'] = ques[i].ans4
            mydict['correct'] = ques[i].correct_answer
            final_dict['question'+str(numbering)] = mydict
            numbering += 1

        mydict = {}
    network_users += 1
    final_dict['users'] = network_users
    return JsonResponse(final_dict)


def submit_python(req):
    global python_users
    python_users -= 1
    return HttpResponse(python_users)


def submit_networks(req):
    global network_users
    network_users -= 1
    return HttpResponse(network_users)
