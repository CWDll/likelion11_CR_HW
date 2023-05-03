from django.db import models

# Create your models here.

<<<<<<< HEAD
# 이놈이 본체다. 얘 바뀔 때마다 migration (명령 2개)해줘야 함.

=======
>>>>>>> 7c46afe8e19fddf1c5d717d94f9e66669aca341f
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
<<<<<<< HEAD

=======
    
>>>>>>> 7c46afe8e19fddf1c5d717d94f9e66669aca341f
    def __str__(self):
        return self.title

    def summary(self):
<<<<<<< HEAD
        return self.body[:20]

=======
        return self.body[:20]
>>>>>>> 7c46afe8e19fddf1c5d717d94f9e66669aca341f
