# models.py
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='emailID', unique=True)
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    updated_at = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=8, verbose_name='등급',
                             choices=(
                                 ('admin', 'admin'),
                                 ('user', 'user')
                             ))

    def __str__(self):
        return self.useremail

    class Meta:
        db_table = 'accounts'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
