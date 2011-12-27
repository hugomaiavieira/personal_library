from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    edition = models.CharField(max_length=200)
    key_words = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

class Summary(models.Model):
    content = models.TextField()
    publication = models.ForeignKey(Publication)

