# Generated by Django 4.0.4 on 2022-05-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receivers', '0002_rename_receivers_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='logo',
            field=models.ImageField(default='images/no_photo.png', upload_to=''),
        ),
    ]