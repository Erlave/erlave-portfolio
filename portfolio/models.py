from django.db import models

# Create your models here.

class prot_title(models.Model):
    title=models.CharField(("تایتل برای پلن ها"), max_length=100)

    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)


    class Meta:
        verbose_name = 'تایتل نمونه کار ها'
        verbose_name_plural = 'تایتل نمونه کار ها'

    def __str__(self):
        return self.title
    
class portfolio(models.Model):
    img=models.ImageField(("عکس نمونه کار"), upload_to='portfolio/', height_field=None, width_field=None, max_length=None)
    title=models.CharField(("اسم"), max_length=100)
    type1=models.CharField(("با چیا پروژه رو زدی"),null=True,blank=True, max_length=100)
    type2=models.CharField(("با چیا پروژه رو زدی"),null=True,blank=True, max_length=100)
    type3=models.CharField(("با چیا پروژه رو زدی"),null=True,blank=True, max_length=100)
    type4=models.CharField(("با چیا پروژه رو زدی"),null=True,blank=True, max_length=100)

    url_github=models.URLField(("لینک گیت هاب پروژه"),null=True,blank=True, max_length=200)

    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)

    class Meta:
        verbose_name = ' نمونه کار ها'
        verbose_name_plural = ' نمونه کار ها'

    def __str__(self):
        return self.title