from django.shortcuts import render, redirect
from .forms import ChildrenForm, ParentForm, LeaderForm, PostForm, SquadForm, CampForm
from .serializers import SelectChildrens
from .models import Children
import datetime

from rest_framework import generics
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class SelectChildren(APIView):
    def get(self, request):
        childrens = Children.objects.all()
        serializer = SelectChildrens(childrens, many=True)
        return Response(serializer.data)

def index(request):
    childrens = Children.objects.all()
    return render(request, 'vitacamp/index.html', {'childrens': childrens})

def add_user(request):
    if request.method == "POST":
        if request.POST['type_user'] == 'leader':
            form = LeaderForm(request.POST)
            if form.is_valid():
                leader = form.save(commit=False)
                leader.last_name = request.POST['last_name']
                leader.first_name = request.POST['first_name']
                leader.middle_name = request.POST['middle_name']
                leader.contact_phone = request.POST['contact_phone']
                leader.save()
                return redirect('index')
            else:
                form = LeaderForm()

        elif request.POST.type_user == 'parent':
            form = ParentForm(request.POST)
            if form.is_valid():
                parent = form.save(commit=False)
                parent.last_name = request.POST['last_name']
                parent.first_name = request.POST['first_name']
                parent.middle_name = request.POST['middle_name']
                parent.contact_phone = request.POST['contact_phone']
                parent.save()
                return redirect('index')
            else:
                form = ParentForm()

        elif request.POST.type_user == 'children':
            form = ChildrenForm(request.POST)
            if form.is_valid():
                children = form.save(commit=False)
                children.last_name = request.POST['last_name']
                children.first_name = request.POST['first_name']
                children.middle_name = request.POST['middle_name']
                children.contact_phone = request.POST['contact_phone']
                children.birthday = request.POST['birthday']
                children.save()
                return redirect('index')
            else:
                form = ChildrenForm()
                
    return render(request, 'vitacamp/add_user.html')


def add_event(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.created_date = request.POST['created_date']
            post.published_date = str(datetime.datetime.now())
            post.save()
            return redirect('index')
        else:
            form = PostForm()
    return render(request, 'vitacamp/add_event.html')

def add_squad(request):
    if request.method == "POST":
        form = SquadForm(request.POST)
        if form.is_valid():
            squad = form.save(commit=False)
            squad.nick = request.POST['nick']
            squad.slogan = request.POST['slogan']
            squad.save()
            return redirect('index')
        else:
            form = SquadForm()
    return render(request, 'vitacamp/add_squad.html')

def add_camp(request):
    if request.method == "POST":
        form = CampForm(request.POST)
        if form.is_valid():
            camp = form.save(commit=False)
            camp.title = request.POST['title']
            camp.label = request.POST['label']
            camp.save()
            return redirect('index')
        else:
            form = CampForm()
    return render(request, 'vitacamp/add_camp.html')