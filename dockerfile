# استفاده از پایتون 3.13
FROM python:3.13-slim

# جلوگیری از کش و بهتر شدن لاگ‌ها
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ساخت دایرکتوری داخل کانتینر
WORKDIR /app

# اول فقط requirements رو کپی کن (برای کش بهتر)
COPY requirements.txt /app/

# نصب پکیج‌ها
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# حالا بقیه کد پروژه رو کپی کن
COPY . /app/

# اکسپوز کردن پورت
EXPOSE 8000

# اجرای پروژه (اینجا با runserver چون تازه میخوای تست کنی)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
