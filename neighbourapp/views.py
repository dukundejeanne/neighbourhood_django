from django.shortcuts import render,redirect,get_object_or_404
from .models import Neighbour,Profile,Rates,Business
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import NewNeighbourForm,UpdatebioForm,PostForm,VotesForm
from .email import send_welcome_email
from .forms import NewsLetterForm
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import  MoringaMerch
# from .serializer import MerchSerializer,MerchSerializerProfile
# from rest_framework import status
# from .permissions import IsAdminOrReadOnly

# display images
@login_required(login_url='/accounts/login/')
def home_images(request):
    # if request.GET.get('search_iterm'):
    #     pictures=Image.search(request.GET.get('search_iterm'))
    # else:
    pictures=Neighbour.objects.all()
    current_user=request.user
    myprof=Profile.objects.filter(id=current_user.id).first()
    # comment=Comment.objects.filter(id=current_user.id).first()
    form=NewsLetterForm()
    # if request.method== 'POST':
    #     form=NewsLetterForm(request.POST or None)
    #     if form.is_valid():
    #         name=form.cleaned_data['your_name']
    #         email=form.cleaned_data['email']
    #         recipient=NewsLetterRecipients(name=name,email=email)
    #         recipient.save()
    #         send_welcome_email(name,email)
    #         HttpResponseRedirect('home_images')
    return render(request,'index.html',{"pictures":pictures,'letterForm':form,"myprof":myprof})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user=request.user
    if request.method=='POST':
        form=NewNeighbourForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
            # HttpResponseRedirect('hamePage')
        return redirect('homePage')
    else:
        form=NewNeighbourForm()
    return render(request,'registration/new_image.html',{"form":form})



@login_required(login_url='/accounts/login/')
def profilemy(request,username=None):
    current_user=request.user
    pictures=Neighbour.objects.filter(name=current_user)
    business=Business.objects.filter(owner=current_user).all()
    if not username:
        username=request.user.username
        images=Neighbour.objects.filter(name=username)
        # proc_img=Profile.objects.filter(user=current_user).first()
    return render(request,'profilemy.html',locals(),{"business":business,"pictures":pictures})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user=request.user
    if request.method=='POST':
        form=UpdatebioForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('homePage')
    else:
        form=UpdatebioForm()
    return render(request,'registration/profile_edit.html',{"form":form})

def user_list(request):
    user_list=User.objects.all()
    context={'user_list':user_list}
    return render(request,'user_list.html',context)

@login_required(login_url='/accounts/login/')     
def add_post(request,image_id):
    current_user=request.user
    image_item=Neighbour.objects.filter(id=image_id).first()
    # prof=Profile.objects.filter(user=current_user.id).first()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            postform.save(commit=False)
            comment.title=prof
            comment.comment_image=image_item
            comment.save()
            return redirect('homePage')
    else:
        form=PostForm()
    return render(request,'comment_form.html',{"form":form,"image_id":image_id})

def add_business(request):
    current_user=request.user
    buz=Business.objects.filter(user=user).first()
    # all=Rates.objects.filter(project=id) 
    if request.method == 'POST':
        form = businessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.buz=buz
            business.save()
        return redirect(reverse('profilemy',args=[current_user.id]))
    else:
        form=businessForm()
    return render(request,'business.html',{'form':form})
    

def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_title =Business.search_by_business(search_term)
        message = f"{search_term}"

        return render(request, 'all_news/search.html',{"message":message,"users": searched_title})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_news/search.html',{"message":message})
        
@login_required(login_url='/accounts/login/') 
def likes(request,id,Neighbour_id):
    likes=1
    image=Neighbour.objects.get(id=id)
    image.likes=image.likes+1
    image.save()
    return redirect('homePage')

@login_required(login_url='/accounts/login/') 
def projects(request,id):
    
    projects=Neighbour.objects.filter(id=id)
    all=Rates.objects.filter(project=id) 
    if request.method == 'POST':
        form = VotesForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project =id
            rate.save()
        return redirect('projects',id)
        
    else:
        form = VotesForm() 
    calcul=Rates.objects.filter(project=id)
    usability=[]
    design=[]
    content=[]
    aver_usability=0
    aver_design=0
    aver_content=0
    for i in calcul:
        usability.append(i.usability)
        design.append(i.design)
        content.append(i.content)

        if len(usability)>0 or len(design)>0 or len(content)>0:
            aver_usability+= round(sum(usability)/len(usability))
            aver_design+= round(sum(design)/len(design))
            aver_content+= round(sum(content)/len(content))
        else:
            aver_usability=0.0
            aver_design=0.0
            aver_content=0.0
    
    return render(request,'one_project.html',{"projects":projects,"all":all,"form":form,"usability":aver_usability,"design":aver_design,"content":aver_content})

