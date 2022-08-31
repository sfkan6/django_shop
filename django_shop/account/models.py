from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from PIL import Image


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('Имя пользователя должно быть указано')
        if not email:
            raise ValueError('Адрес электронной почты должен быть указан')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser должен быть is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser должен быть is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):

    username = models.CharField(blank=True, unique=True, max_length=150, verbose_name='Логин', )
    email = models.EmailField(unique=True, max_length=320, verbose_name='Email', )
    phone = PhoneNumberField(blank=True, null=True, unique=True, verbose_name='Телефон',
                            error_messages={
                                'invalid': "Введите правильный номер телефона +12125552368.",
                                'unique': "Этот номер телефона уже используется."
                            })
    image = models.ImageField(default='default.png', upload_to='avatar')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def clean_data(self):
        data = {
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
        }

        return data
