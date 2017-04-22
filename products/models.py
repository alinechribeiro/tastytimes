import uuid
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
#can also create a field for images here for example.
    #image = models.ImageField(upload_to="images", blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

@property
def paypal_form(self):
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": self.price,
        "currency": "USD",
        "item_name": self.name,
        "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
        "notify_url": settings.PAYPAL_NOTIFY_URL,
        "return_url": "%s/paypal-return" % settings.SITE_URL,
        "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
    }
    return PayPalPaymentsForm(initial=paypal_dict)

def __unicode__(self):
    return self.name

##class Post(models.Model):
##    thread = models.ForeignKey(Thread, related_name='posts')
##    comment = HTMLField(blank=True)
##    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
##    created_at = models.DateTimeField(default=timezone.now)
