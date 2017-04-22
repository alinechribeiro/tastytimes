from django.contrib import admin
from .models import Subject, Thread, Post

##Subjects will be created ONLY in the site
## admin pages as only the site admin should 
## be able to specify what subjects are available 
## to be discussed on your forum. Once you’ve
## create the model and run your migrations later 
##you should login to the admin and create a few subjects to play around with. 

admin.site.register(Subject)
admin.site.register(Thread)
admin.site.register(Post)

