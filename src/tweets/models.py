from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import random
from django.contrib.auth.models import User

STATUS = (
    ('draft',"Draft"),
    ('live',"Live"),
    ('expired',"Expired")
)

TOPIC = (
    ('politics',"Politics"),
    ('health',"Health"),
    ('sport',"Sport"),
    ('tech',"Tech")
)

LIKE_DISLIKE = (
    ('like', 'Like'),
    ('dislike', 'Dislike')
)


# Create your models here.

class Post(models.Model):

    def validate_expiration(expiration_time):
        time_now = timezone.now()
        if expiration_time < time_now:
            raise ValidationError('Please select expiraton time after the current time')

    def create_new_ref_number():
      return str(random.randint(0, 99999))

    post_identifier = models.CharField(max_length=5, blank=True, editable=False, default=create_new_ref_number())
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100, choices=TOPIC, default='Politics')
    publish_time = models.DateTimeField(auto_now=True)
    message_body = models.TextField()
    expiration_time = models.DateTimeField(default=timezone.now, validators = [validate_expiration])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return ("Commented: " + format(self.comment) + " by " + format(self.author))

class Likes(models.Model):

    def validate_no_self_likes(self, *args, **kwargs):
        message = get_object_or_404(Post, pk=serializer.initial_data['post'])
        #post_author = Post.objects.all().filter(title=self.post).values('author')
        if messsage.author == self.author:
           raise ValidationError("Cannot self like post")

    like_or_dislike = models.CharField(max_length=20, choices=LIKE_DISLIKE, default='like')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return ("Vote: " + format(self.like_or_dislike))