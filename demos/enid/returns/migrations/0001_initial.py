# Generated by Django 4.2.7 on 2023-11-30 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Returns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.CharField(max_length=255)),
                ('answer', models.TextField(default=None, null=True)),
            ],
        ),
    ]
