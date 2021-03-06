# Generated by Django 2.1.5 on 2019-04-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190411_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, help_text='Recipient Email', max_length=255, null=True)),
                ('name', models.CharField(blank=True, help_text='Recipient name', max_length=255, null=True)),
                ('message', models.CharField(blank=True, help_text='Message', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, help_text='Recipient Email', max_length=255, null=True)),
                ('name', models.CharField(blank=True, help_text='Recipient name', max_length=255, null=True)),
                ('message', models.CharField(blank=True, help_text='Message', max_length=255, null=True)),
                ('rating', models.IntegerField(blank=True, help_text='Rating (from scale -100 to 100)', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, help_text='Recipient Email', max_length=255, null=True)),
                ('name', models.CharField(blank=True, help_text='Recipient name', max_length=255, null=True)),
                ('message', models.CharField(blank=True, help_text='Message', max_length=255, null=True)),
                ('problem_screenshot', models.ImageField(blank=True, help_text='Problem screenshot', null=True, upload_to='problem_insystem_images')),
            ],
        ),
    ]
