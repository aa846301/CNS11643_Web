from django.db import models

# Create your models here.

class word_char_code(models.Model):
    cns_code = models.CharField(max_length=7,blank=False,null=False)
    unicode_code = models.CharField(max_length=5,blank=True,null=True)
    big5_code = models.CharField(max_length=5,blank=True,null=True)