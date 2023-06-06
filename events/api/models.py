from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.html import format_html

from events.settings import MEDIA_URL


class Organization(models.Model):
    objects = models.Manager()
    title = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='Организация',
        help_text='Название организации')
    description = models.CharField(
        max_length=512,
        verbose_name='Описание',
        help_text='Описание организации')
    address = models.CharField(
        max_length=256,
        verbose_name='Адрес',
        help_text='Адрес организации')
    postcode = models.IntegerField(
        validators=[
            MinValueValidator(100000, message='Индекс от 100000'),
            MaxValueValidator(699999, message='Индекс до 699999')
        ],
        verbose_name='Индекс',
        help_text='Индекс организации')

    def __str__(self):
        return self.title


class Event(models.Model):
    objects = models.Manager()
    title = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='Событее',
        help_text='Название события')
    description = models.CharField(
        max_length=512,
        verbose_name='Описание',
        help_text='Описание события')
    organizations = models.ManyToManyField(
        Organization,
        through="OrganizationInEvent",
        verbose_name='Организации',
        help_text='Список организаций')
    image = models.ImageField(
        null=True,  
        default=None,
        verbose_name='Изображение',
        upload_to='events/image/',
        help_text='Выберите изображение для события'
    )
    date = models.DateField(
        verbose_name='Дата',
        help_text='Дата проведения мероприятия',
        blank=True,
        default=None,
    )

    def image_tag(self):
        return format_html('<img src="%s%s" width="150" height="150" />' % (f'{MEDIA_URL}', self.image))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title


class OrganizationInEvent(models.Model):
    objects = models.Manager()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, organization, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
        )
        org_id = organization if isinstance(organization, int) else organization.id
        user.organization = Organization.objects.get(id=org_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, organization, password=None):
        user = self.create_user(
            email,
            password=password,
            organization=organization
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        db_index=True,
        unique=True,
        max_length=128,
        verbose_name='Электронная почта',
        help_text='Введите электронную почту пользователя')
    password = models.CharField(
        max_length=128,
        verbose_name='Пароль',
        help_text='Введите пароль')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    organization = models.ForeignKey(Organization,
                                     related_name='members',
                                     on_delete=models.CASCADE)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'organization']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email
