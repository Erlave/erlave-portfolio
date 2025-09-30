from django.db import models

# Create your models here.
class hi(models.Model):
    title=models.CharField(("سلام من ... هستم"), max_length=50)
    is_active=models.BooleanField(("فعال/ غیر فعال") , default=False)
    class Meta:
        verbose_name = 'سلام من ... هستم'
        verbose_name_plural = 'سلام من ... هستم'

    def __str__(self):
        return self.title




class home_model (models.Model):
    image = models.ImageField(("عکس در خانه"),null=True , blank=True ,upload_to='profile/', height_field=None, width_field=None, max_length=None)
    title_1_of_3 =models.CharField(("متن قبل باکس سبز"), max_length=50)
    title_2_of_3 =models.CharField(("متن باکس سبز"), max_length=50)
    title_3_of_3 =models.CharField(("متن بعد باکس سبز"), max_length=50)
    descreption = models.CharField(("توضیحات"), max_length=200)

    complate_projects=models.CharField(("پروژه های کامل"), max_length=50)
    customer=models.CharField(("مشتری"), max_length=50)
    experience=models.CharField(("تجربه"), max_length=50)
    is_active=models.BooleanField(("فعال/ غیر فعال") , default=False)

    class Meta:
        verbose_name = 'تنظیمات خانه'
        verbose_name_plural = ' تنظیمات خانه' 


    def __str__(self):
        return f"{self.title_1_of_3} {self.title_2_of_3} {self.title_3_of_3}"