# Generated by Django 3.0.5 on 2020-06-11 17:46

from django.db import migrations, models
import uploadApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to=uploadApp.models.get_upload_path)),
            ],
        ),
    ]