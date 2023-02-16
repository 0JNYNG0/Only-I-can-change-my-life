from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):
    # related_name 은 request.user.profile 처럼 바로 접근할 수 있게 이름을 설정 하는 것이다
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # media/ 경로 아래에 profile/ 경로가 추가 되어 이미지 접근을 할 수 있게 된다
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
