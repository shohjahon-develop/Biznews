# Generated by Django 4.2.6 on 2023-12-10 13:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_bot_slug_bot_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lorem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('bio', models.TextField()),
                ('img', models.ImageField(upload_to='category/img')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(max_length=300)),
                ('status', models.CharField(choices=[('YR', 'Yaroqli'), ('YS', 'Yaroqsiz')], default='YR', max_length=2)),
            ],
        ),
    ]
