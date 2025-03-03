# Generated by Django 5.1.6 on 2025-02-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0003_staff_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('hiredate', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
