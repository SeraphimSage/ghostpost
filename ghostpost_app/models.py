from django.db import models
from django.utils import timezone

# Create your models here.
"""
BR_Post
- Title - str - 280
- Boast/Roast - Boolean
- Up_field - IntegerField for up votes
- Down_field - IntegerField for down votes
- post_date - datetime
"""


class BR_Post(models.Model):

    POST_CHOICE = ((True, 'Boast'), (False, 'Roast'))

    title = models.CharField(max_length=280)
    boast_roast = models.BooleanField(choices=POST_CHOICE)
    up_field = models.IntegerField(default=0)
    down_field = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)

    # sohail was a big help with this during study hall.
    @property
    def votes(self):
        return self.up_field - self.down_field

    def __str__(self):
        return self.title
