# Generated by Django 4.1.3 on 2022-11-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
    ]
