# Generated by Django 2.0.6 on 2018-07-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_vocabulary', '0002_auto_20180430_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagVocabulary',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
