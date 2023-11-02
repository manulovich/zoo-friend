# Generated by Django 4.2.5 on 2023-09-27 11:43

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_contact_alter_useraccount_is_owner_shelter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tg',
            field=models.URLField(blank=True, verbose_name='Телеграм'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='vk',
            field=models.URLField(blank=True, verbose_name='ВКонтакте'),
        ),
    ]
