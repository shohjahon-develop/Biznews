# Generated by Django 4.2.6 on 2023-12-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_bot_alter_mahsulot_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='slug',
            field=models.SlugField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
