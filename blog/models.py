from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL)
  title = models.CharField(max_length=255)
  slug = models.SlugField(unique=True, max_length=255)
  description = models.CharField(max_length=255)
  content = models.TextField()
  published = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  created_date = models.DateTimeField(auto_now_add=True)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
  	self.published_date = timezone.now()
  	#self.created= timezone.now()
  	self.save()

  def __unicode__(self):
  	return self.title

class Meta:
  ordering = ['-created']

def __unicode__(self):
  return u'%s' % self.title

def get_absolute_url(self):
  return reverse('blog.views.post', args=[self.slug])

class Contact(models.Model):
	#class Meta: #include this to ensure build in IDE
	#	app_label = "blog" 
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	mobile = models.CharField(max_length=20)

	def __str__(self):
		return ' '.join([
			self.first_name,
			self.last_name,
		])

class Interview(models.Model):
  #author = models.ForeignKey('auth.User', blank=True, default=1, null=True)
  title = models.CharField(max_length=255)
  slug = models.SlugField(unique=True, max_length=255)
  description = models.CharField(max_length=255)
  content = models.TextField()

  def publish(self):
  	self.published_date = timezone.now()
  	#self.created= timezone.now()
  	self.save()

  def __unicode__(self):
  	return self.title

#