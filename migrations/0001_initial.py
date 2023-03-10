# Generated by Django 4.1.4 on 2023-01-25 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='予定開始日')),
                ('end_date', models.DateField(verbose_name='予定終了日')),
                ('event_name', models.CharField(max_length=200, verbose_name='タイトル')),
                ('info', models.TextField(blank=True, max_length=100, verbose_name='予定内容')),
            ],
        ),
    ]
