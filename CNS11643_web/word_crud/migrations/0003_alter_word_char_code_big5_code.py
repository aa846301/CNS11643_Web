# Generated by Django 4.1.7 on 2023-03-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_crud', '0002_alter_word_char_code_big5_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word_char_code',
            name='big5_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
