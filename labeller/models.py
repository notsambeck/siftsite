from django.db import models
from django.contrib.auth.models import User
# from django.conf import settings

'''
Models for label_game app

models we will need:

user: ID, name, profile picture, etc (built in)
image: image ID, classification, source, source_user, date, filename
user label: image, user, label
total votes: for each image, label - number of votes
'''

# Create your models here.


class Image(models.Model):
    """ A database record for uploaded images to be labeled """
    source = models.CharField("image source: web, sift generator func, camera",
                              max_length=512, default=None, null=True)
    correct_label = models.IntegerField("Correct label; 0=simulated, 1=image")
    uploaded_by = models.ForeignKey(User, default=None, null=True)
    filename = models.FileField("file path", upload_to='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'IMAGE: class={}, source={}'.format(self.correct_label,
                                                   self.source)


class UserLabel(models.Model):
    """ Individual user labels (for a label for an image) """
    image = models.ForeignKey(Image)
    my_label = models.IntegerField()
    user = models.ForeignKey(User, default=None, null=True)

    def __str__(self):
        return 'User {} label: image={} class={}'.format(self.user,
                                                         self.image.filename,
                                                         self.label)


class TotalVotes(models.Model):
    """ Aggregated votes (by all users) for an individual Image """
    image = models.ForeignKey(Image)
    label = models.ForeignKey(UserLabel)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.image.caption + str(self.votes)
