# Generated by Django 4.1.2 on 2023-11-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbainc', '0021_remove_home_heading_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stratup',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='Startup/'),
        ),
        migrations.AddField(
            model_name='stratup',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='Startup/'),
        ),
        migrations.AlterField(
            model_name='stratup',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Startup/'),
        ),
    ]
