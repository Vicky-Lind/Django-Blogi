# Generated by Django 4.1.5 on 2023-03-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0006_alter_postaus_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='postaus',
            name='otsikko_lower',
            field=models.CharField(help_text='Exact same as normal title but in lowercase', max_length=200, null=True),
        ),
    ]
