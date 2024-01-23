# Generated by Django 4.2.6 on 2023-12-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_mahsulot_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='slug',
            field=models.SlugField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bot',
            name='status',
            field=models.CharField(choices=[('YR', 'Yaroqli'), ('YS', 'Yaroqsiz')], default='YR', max_length=2),
        ),
    ]