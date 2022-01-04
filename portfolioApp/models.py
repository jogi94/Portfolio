from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
)

TITLE_CHOICES = (
		('ERROR','ERROR'),
		('SUCCESS','SUCCESS'),
		('WARNING','WARNING'),
		('THANKYOU','THANKYOU'),
	)

#
class messageModel(models.Model):
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorMM', null=True, blank=True)
	title = models.CharField(max_length=256,null=True, blank=True)
	messageFor = models.CharField(max_length=50, choices=TITLE_CHOICES, null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	
	def __str__(self):
		return self.titleType or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Message Model Content'



#
class siteSetting(models.Model):
	author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorSS', null=True, blank=True)
	logo = models.ImageField(upload_to='basic/logo/', null=True, blank=True)
	title = models.CharField(max_length=500,null=True, blank=True)
	siteDescription = models.CharField(max_length=500, null=True, blank=True)
	contactNumber = models.BigIntegerField(null=True, blank=True)
	email = models.EmailField(max_length=254, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	location = models.CharField(max_length=500, null=True, blank=True)
	embedLocation = models.URLField(max_length=500, null=True, blank=True)
	working_hours = models.CharField(max_length=100, null=True, blank=True)
	facebook = models.CharField(max_length=100, null=True, blank=True)
	twitter = models.CharField(max_length=100, null=True, blank=True)
	skype = models.CharField(max_length=100, null=True, blank=True)
	whatsApp = models.CharField(max_length=1000, null=True, blank=True)
	linkedin = models.CharField(max_length=100, null=True, blank=True)
	pinterest = models.CharField(max_length=100, null=True, blank=True)
	youtube = models.CharField(max_length=100, null=True, blank=True)
	instagram = models.CharField(max_length=100, null=True, blank=True)
	other_footer_id = models.CharField(max_length=100, null=True, blank=True)
	other_footer_icon = models.ImageField(upload_to='basic/icon/', null=True, blank=True)
	phone = models.BigIntegerField(null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	
	def __str__(self):
		return self.title or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Site Setting'

class portifolio_page(models.Model):
	our_name = models.CharField(max_length=256, null=True, blank=True, default='Hello, I’m Fatima.')
	our_profession = models.CharField(max_length=256, null=True, blank=True, default='FREELANCE DIGITAL DESIGNER')
	subtitle = models.CharField(max_length=256, null=True, blank=True)
	background_image = models.ImageField(upload_to='portifolio/backgroundImage/', null=True, blank=True)
	download_cv_file = models.FileField(upload_to='portifolio/cv/', null=True, blank=True, validators=[FileExtensionValidator(['csv','docx','pdf'])])
	download_cv_url = models.CharField(max_length=256, null=True, blank=True)
	download_cv_button = models.CharField(max_length=256, null=True, blank=True, default='DOWNLOAD CV')
	#aboutSection
	about_heading = models.CharField(max_length=256, null=True, blank=True, default='My About')
	about_subtitle = models.CharField(max_length=256, null=True, blank=True, default='Read About Me')
	about_content = models.TextField(null=True, blank=True)
	about_image = models.ImageField(upload_to='portifolio/aboutImage/', null=True, blank=True)
	#client
	client_heading = models.CharField(max_length=256, null=True, blank=True, default='My Top Clients')
	client_subtitle = models.CharField(max_length=256, null=True, blank=True, default='Clients Meeting With Me')
	client_video_file = models.FileField(upload_to='portifolio/client_video/', null=True, blank=True, validators=[FileExtensionValidator(['mp4'])])
	client_video_id = models.URLField(null=True, blank=True)
	#performance
	performance_heading =models.CharField(max_length=256, null=True, blank=True, default='My Best Performance')
	performance_subtitle = models.CharField(max_length=256, null=True, blank=True, default='My Performance')
	performance_content = models.TextField(null=True, blank=True)
	performance_image = models.ImageField(upload_to='portifolio/performanceImage', null=True, blank=True)
	performance_button = models.CharField(max_length=256, null=True, blank=True, default='SEE MY SKILL')
	#ourProjects
	project_heading = models.CharField(max_length=256, null=True, blank=True, default='Some of My Recent Works')
	project_sub_heading = models.CharField(max_length=256, null=True, blank=True, default='Our Project')
	project_subtitle = models.CharField(max_length=256, null=True, blank=True, default='There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration.')
	project_button = models.CharField(max_length=256, null=True, blank=True, default='VIEW PROJECTS')
	#contactUS
	contact_heading = models.CharField(max_length=256, null=True, blank=True, default="Let's Say Hi")
	contact_sub_heading = models.CharField(max_length=256, null=True, blank=True, default="Hire Me.")
	contact_image = models.ImageField(upload_to='portifolio/contactImage', null=True, blank=True)
	call_number_heading = models.CharField(max_length=256, null=True, blank=True, default="Call us directly : ")
	email_heading = models.CharField(max_length=256, null=True, blank=True, default="Contact Email : ")
	contact_button = models.CharField(max_length=256, null=True, blank=True, default='SUBMIT NOW')
	page_end_title = models.CharField(max_length=256, null=True, blank=True, default='Ready to start creating a standard website?')
	page_last_button = models.CharField(max_length=256, null=True, blank=True, default='SUBMIT NOW')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	
	def __str__(self):
		return self.our_name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Portifolio Page'

class educational_skills(models.Model):
	heading = models.CharField(max_length=256, null=True, blank=True, default='Educational Skill')
	subtitle = models.CharField(max_length=256, null=True, blank=True, default='Lorem ipsum dolor sit amet, onecis et mollis.')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='draft')
	
	def __str__(self):
		return self.heading or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Educational Skills'

class our_clients(models.Model):
	client_name = models.CharField(max_length=256, null=True, blank=True)
	client_logo = models.ImageField(upload_to='clients/logo/', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='draft')
	
	def __str__(self):
		return self.client_name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Our Clients'

#
class our_projects(models.Model):
	project_name = models.CharField(max_length=256, null=True, blank=True)
	project_subtitle = models.CharField(max_length=256, null=True, blank=True)
	project_image = models.ImageField(upload_to='project/image/', null=True, blank=True)
	video_content = models.TextField(null=True, blank=True)
	slug = models.SlugField(max_length=256, null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='draft')

	def get_absolute_url(self):
		return reverse('portfolioApp:ourWorkDetailUrl', args=[self.slug])
	
	def __str__(self):
		return self.project_name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Our Projects'

class videos(models.Model):
	video_file = models.FileField('File', upload_to='images/')
	video_id = models.CharField(max_length=256, null=True, blank=True)
	title = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(max_length=250, null=True, blank=True)
	our_work = models.ForeignKey('our_projects', related_name='ourWorkV', on_delete=models.SET_NULL, blank=True, null=True)
	our_work_Video = models.BooleanField(null=True, blank=True)

	def __str__(self):
		return self.filename

	@property
	def filename(self):
		return self.video_file.name.rsplit('/', 1)[-1]

#
class lead_contacts(models.Model):
	name = models.CharField(max_length=256, null=True, blank=True)
	phone_number = models.BigIntegerField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	generatedFrom = models.CharField(max_length=256, null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='draft')
	
	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Lead Contact'

