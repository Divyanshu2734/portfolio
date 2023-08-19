from django.db import models

class reachme(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=25)
    email=models.CharField(max_length=100)
    mobile=models.IntegerField()
    discription=models.TextField()

    def __str__(self) :
        return self.name


class blog(models.Model):
    title=models.CharField(max_length=70)
    discription=models.TextField()
    author_name=models.CharField(max_length=80)
    image=models.ImageField(upload_to='blog',blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str(self):
        return self.title
    
class msg(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=90)
    subject=models.TextField()
    mssages=models.TextField()

    def __str__(self) :
        return self.name

