# Generated by Django 2.1.4 on 2018-12-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunubusApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='heroes',
            options={},
        ),
        migrations.RemoveField(
            model_name='heroes',
            name='created',
        ),
        migrations.AlterField(
            model_name='heroes',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='idHero',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='prenom',
            field=models.CharField(max_length=100),
        ),
    ]
