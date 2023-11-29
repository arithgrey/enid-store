# Generated by Django 4.2.7 on 2023-11-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('is_visible', models.BooleanField(default=True)),
                ('url_img', models.URLField(default=False)),
            ],
        ),
    ]
