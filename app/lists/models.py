from django.db import models
from django.utils import timezone

# ##################### Manager ##########################3
#
# class PublishedManager(models.Manager):
#     use_for_related_fields = True
#     def published(self,**kwargs):
#         return self.filter(pub_date__lte=timezone.now())
# #################### Create your models here.###################
# class TimeStampModel(models.Model):
#     created =   models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
#
# class Flavor(TimeStampModel):
#     title = models.CharField(max_length=200)
#
# class FlavorReview(models.Model):
#     review = models.CharField(max_length=255)
#     pub_date = models.DateTimeField()
#     object = PublishedManager()

class Item(models.Model):

    text = models.CharField(max_length=255)
