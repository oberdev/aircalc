# Generated by Django 2.1.7 on 2019-02-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploader', models.CharField(max_length=16)),
                ('file', models.FileField(upload_to='sources/')),
                ('upload_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
