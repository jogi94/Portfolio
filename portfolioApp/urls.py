from django.urls import path
from . import views

app_name = 'portfolioApp'

urlpatterns = [
	path('', views.portfolioView, name='portfolioUrl'),
	path('our-work/', views.ourWorkView, name='ourWorkUrl'),
	path('our-work-detail/<slug>/', views.ourWorkDetailView, name='ourWorkDetailUrl'),
	#submitURL
	path('contact-form/', views.contactFormView, name='contactFormUrl'),
]