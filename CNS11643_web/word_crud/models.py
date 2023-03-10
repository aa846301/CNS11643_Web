from django.db import models

# Create your models here.

class WordModels(models.Model):
    cns_code = models.CharField(max_length=7,blank=False,null=False)
    chinese_char = models.CharField(max_length=1,blank=True,null=True)
    unicode_code = models.CharField(max_length=5,blank=True,null=True)
    big5_code = models.CharField(max_length=5,blank=True,null=True)
    
    def __str__(self):
        return f"CNS:{self.cns_code} 中文:{self.chinese_char}"