from django.db import models

# Create your models here.
class services (models.Model):
    title=models.CharField(("خدمات که ارائه میدی"), max_length=50)
    projects=models.CharField(("تعداد پروژه که انجام دادی"), max_length=50)
    icon=models.CharField(("اسم به اینگلیسی برای ایکون"),default="default-icon", max_length=50)
    descreption=models.CharField(("توضیحات"), max_length=200)
    url=models.URLField(("لینک برای بیشتر بخوانید"),default="default-url", max_length=200)

    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)

    class Meta:
        verbose_name = 'چه خدماتی ارائه می دهم؟'
        verbose_name_plural = 'چه خدماتی ارائه می دهم؟'

    def __str__(self):
        return self.title
    

class plan_title(models.Model):
    title=models.CharField(("تایتل برای پلن ها"), max_length=100)
    des=models.CharField(("توضیحات پلن ها"), max_length=400)

    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)


    class Meta:
        verbose_name = 'پلن های خدمات'
        verbose_name_plural = 'پلن های خدمات'

    def __str__(self):
        return self.title
    

class plan_cart(models.Model):
    plan_type=models.CharField(("تایپ پلن مثال  :استاندارد , پریمیرم"), max_length=50)
    price=models.CharField(("قیمت پلن ها"), max_length=50)
    ops1=models.CharField(("قابلیت های پلن"),null=True,blank=True, max_length=50)
    ops2=models.CharField(("قابلیت های پلن"),null=True,blank=True, max_length=50)
    ops3=models.CharField(("قابلیت های پلن"),null=True,blank=True, max_length=50)
    ops4=models.CharField(("قابلیت های پلن"),null=True,blank=True, max_length=50)

    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)


    class Meta:
        verbose_name = ' کارت پلن های خدمات' 
        verbose_name_plural = ' کارت پلن های خدمات'

    def __str__(self):
        return self.plan_type