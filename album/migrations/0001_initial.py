# Generated by Django 3.2.8 on 2022-03-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='images/')),
                ('descriptions', models.CharField(max_length=100)),
            ],
        ),
    ]
