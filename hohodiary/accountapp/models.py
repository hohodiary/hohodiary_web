from django.db import models

# Create your models here.
class Account(models.Model):
    userid = models.CharField(max_length= 64,
                                verbose_name= '아이디')
    username = models.CharField(max_length= 12,
                                verbose_name= '이름')
    nickname = models.CharField(max_length= 64,
                                verbose_name= '닉네임')
    useremail = models.EmailField(max_length=128,
                                verbose_name='사용자 이메일')
    password = models.CharField(max_length= 64,
                                verbose_name= '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add= True,
                                            verbose_name='등록시간')
    
    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'account'
        verbose_name = '사용자'
        verbose_name_plural = '사용자들'