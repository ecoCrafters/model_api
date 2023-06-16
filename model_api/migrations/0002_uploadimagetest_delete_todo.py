# Generated by Django 4.2.2 on 2023-06-16 00:01

from django.db import migrations, models
import model_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('model_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImageTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=model_api.models.nameFile)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
