# Generated by Django 2.1.3 on 2019-10-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mz', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHERS')], default='M', max_length=1),
        ),
    ]
