from django.db import models

# Create your models here.

class about_me_model(models.Model):
    img = models.ImageField(("عکس در درباره ما"), upload_to='about/', height_field=None, width_field=None, max_length=None)
    title_1_of_3 =models.CharField(("متن قبل  سبز"), max_length=50)
    title_2_of_3 =models.CharField(("متن باکس سبز"), max_length=50)
    title_3_of_3 =models.CharField(("متن بعد  سبز"), max_length=50)
    descreption = models.CharField(("توضیحات"), max_length=200)

    ability1=models.CharField(("تیک توانایی ها 1"), max_length=50)
    ability2=models.CharField(("تیک توانایی ها 2"), max_length=50)
    ability3=models.CharField(("تیک توانایی ها 3"), max_length=50)
    ability4=models.CharField(("تیک توانایی ها 4"), max_length=50)

    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)

    class Meta:
        verbose_name = ' درباره من سکشن 1'
        verbose_name_plural = ' درباره من سکشن 1'