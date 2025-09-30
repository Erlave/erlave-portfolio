from django.db import models

# Create your models here.
class services (models.Model):
    title=models.CharField(("خدمات که ارائه میدی"), max_length=50)
    projects=models.CharField(("تعداد پروژه که انجام دادی"), max_length=50)
    icon=models.CharField(("اسم به اینگلیسی برای ایکون"),null=True,blank=True, max_length=50)
    descreption=models.CharField(("توضیحات"), max_length=200)
    url=models.URLField(("لینک برای بیشتر بخوانید"),null=True,blank=True, max_length=200)

    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)

    class Meta:
        verbose_name = 'چه خدماتی ارائه می دهم؟'
        verbose_name_plural = 'چه خدماتی ارائه می دهم؟'

    def __str__(self):
        return self.title