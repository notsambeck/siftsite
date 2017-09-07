from django.db import models
from django.contrib.auth.models import User
import jsonfield
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
    filename = models.FileField("file path", upload_to='images')
    source = models.CharField("image source: web, sift generator func, camera",
                              max_length=512, default=None, null=True)
    correct_label = models.IntegerField("Correct label; 0=simulated, 1=image")
    sift_label = models.IntegerField("SIFT-generated label; 0=sim, 1=image",
                                     null=True)
    description = models.CharField("Labels generated by google vision API",
                                   max_length=512, default=None, null=True)
    tweeted = models.BooleanField("Image was tweeted?", default=False)

    uploaded_by = models.ForeignKey(User, default=None, null=True)
    google_raw_data = jsonfield.JSONField('google cloud vision API - JSON',
                                          null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'img: class={}, source={}, file={}'.format(self.correct_label,
                                                          self.source,
                                                          self.filename)


class Choice(models.Model):
    """ possible choices for labels, w/ explanatory text """
    choice = models.IntegerField()
    alt_text = models.CharField("text explaining what integer label means",
                                max_length=64)

    def __str__(self):
        return "choice: int {} means {}".format(self.choice, self.alt_text)


def create_choice(value, text):
    ''' method to create choices so that field is always populated'''
    c = Choice.objects.create(choice=value, alt_text=text)
    c.save()


if Choice.objects.all().count() == 0:
    print("CREATING CHOICES FROM models.py SCRIPT")
    create_choice(1, 'appears to be a photographic image')
    create_choice(0, 'is fake')


class TotalVotes(models.Model):
    """ Aggregated votes (by all users) for an individual Image """
    image = models.ForeignKey(Image)
    choice = models.ForeignKey(Choice)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} -  has {} votes for label {}".format(str(self.image),
                                                        str(self.votes),
                                                        str(self.choice))
