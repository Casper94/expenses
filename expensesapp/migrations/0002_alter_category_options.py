# Generated by Django 4.0.3 on 2022-05-16 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]