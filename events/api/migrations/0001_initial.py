# Generated by Django 3.2.12 on 2023-05-29 21:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название события', max_length=128, verbose_name='Событее')),
                ('description', models.CharField(help_text='Описание события', max_length=512, verbose_name='Описание')),
                ('image', models.ImageField(default=None, help_text='Выберите изображение для события', null=True, upload_to='events/image/', verbose_name='Изображение')),
                ('date', models.DateField(blank=True, default=None, help_text='Дата проведения мероприятия', verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название организации', max_length=128, verbose_name='Организация')),
                ('description', models.CharField(help_text='Описание организации', max_length=512, verbose_name='Описание')),
                ('address', models.CharField(help_text='Адрес организации', max_length=256, verbose_name='Адрес')),
                ('postcode', models.IntegerField(help_text='Индекс организации', validators=[django.core.validators.MinValueValidator(100000, message='Индекс от 100000'), django.core.validators.MaxValueValidator(699999, message='Индекс до 699999')], verbose_name='Индекс')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationInEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organization')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='organizations',
            field=models.ManyToManyField(help_text='Список организаций', through='api.OrganizationInEvent', to='api.Organization', verbose_name='Организации'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, help_text='Введите электронную почту пользователя', max_length=128, unique=True, verbose_name='Электронная почта')),
                ('password', models.CharField(help_text='Введите пароль', max_length=128, verbose_name='Пароль')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='api.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
