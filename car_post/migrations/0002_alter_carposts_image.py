# Generated by Django 5.0.2 on 2024-02-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carposts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car_post/media/uploads/'),
        ),
    ]
