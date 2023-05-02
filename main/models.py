from django.db import models

# Create your models here.

# 이놈이 본체다. 얘 바뀔 때마다 migration (명령 2개)해줘야 함.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

