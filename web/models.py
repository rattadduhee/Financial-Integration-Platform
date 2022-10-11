from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # 기본적으로 제공하는 필드 외에 원하는 필드를 적어준다.
    age = models.CharField(max_length=50)
    child = models.CharField(max_length=10)
    Marriage = models.CharField(max_length=10)
    work = models.CharField(max_length=10)
    work_address = models.CharField(max_length=100)
    hope_address = models.CharField(max_length=100)

class Consume(models.Model): 
    title = models.CharField(max_length=100) # CharField는 길이제한 가지는 필드
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 날짜, 시간 저장하는 필드