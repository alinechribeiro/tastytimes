import uuid
from django import template
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
 
register = template.Library()
 
 
def paypal_form_for(magazine, user):
    ##Here we’re doing something a little more complex than before, as we’re first checking if the user is already subscribed to the magazine. If they are, we skip making the form altogether and return ‘Subscribed’.
    if user.is_subscribed(magazine):
        html = "Subscribed!"
    ##If not, then we create our form using a dict with these values:
    else:
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "currency_code": "USD",
            "cmd": "_xclick-subscriptions",
            "a3": magazine.price,
            "p3": 1,
            "t3": "M",
            "src": 1,
            "sra": 1,
            "item_name": magazine.name,
            "invoice": uuid.uuid4(),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return/" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel/" % settings.SITE_URL,
            "custom": "%s-%s" % (magazine.pk, user.id)
        }
 
        if settings.DEBUG:
            html = PayPalPaymentsForm(initial=paypal_dict,button_type='subscribe').sandbox()
        else:
            html = PayPalPaymentsForm(initial=paypal_dict,button_type='subscribe').render()
 
    return html
 
register.simple_tag(paypal_form_for)