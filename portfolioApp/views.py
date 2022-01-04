from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

def portfolioView(request):
	basicInfo = siteSetting.objects.latest('pk')
	educationalSkills = educational_skills.objects.filter(status='published')
	ourClients = our_clients.objects.filter(status='published')
	ourProjects = our_projects.objects.filter(status='published')
	messageSuccess = messageModel.objects.filter(messageFor='SUCCESS')
	messageError = messageModel.objects.filter(messageFor='ERROR')
	messageWarning = messageModel.objects.filter(messageFor='WARNING')
	messageThankyou = messageModel.objects.filter(messageFor='THANKYOU')
	try:
		portfolioPageInfo = portifolio_page.objects.latest('pk')
	except:
		portfolioPageInfo = None
	context = {
		'basicInfo':basicInfo,
		'portfolioPageInfo':portfolioPageInfo,	
		'educationalSkills':educationalSkills,
		'ourClients':ourClients,
		'ourProjects':ourProjects,
		'messageSuccess':messageSuccess,
		'messageError':messageError,
		'messageWarning':messageWarning,
		'messageThankyou':messageThankyou,
	}
	return render(request, 'UI/index.html', context)

#
def ourWorkView(request):
	projectInst = our_projects.objects.filter(status='published')
	context = {
		'projectInst':projectInst,
	}
	return render(request, 'UI/our-work.html' , context)

#
def ourWorkDetailView(request,slug):
	workInst = get_object_or_404(our_projects, slug=slug)
	videoInst = videos.objects.filter(our_work_Video=True , our_work=workInst)
	context = {
		'workInst':workInst,
		'videoInst':videoInst,
	}
	return render(request, 'UI/our-work-detail.html', context)

def contactFormView(request):
	if request.method == 'POST':
		redirecting = request.POST.get('redirectTo')
		objForm = contactForm(request.POST)
		if objForm.is_valid():
			cd = objForm.save()
			cd.save()
			cd.refresh_from_db()
			messages.success(request, 'I have recieved your details, Will get back to you ASAP.')
			redirecting += '?contact=success'
			get_object_or_404(messageModel, **kwargs)
		else:
			messages.error(request, 'Please Try again, Form not submitted due to some error.')
			get_object_or_404(messageModel,**kwargs)
		return redirect(redirecting)
	else:
		return HttpResponse('Invalid Entry Point!')