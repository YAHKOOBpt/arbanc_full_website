# Generated by Django 4.2.6 on 2023-10-27 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbainc', '0004_commercial_alter_plot_dev_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
    ]
