# Generated by Django 5.0.6 on 2024-05-09 16:56

import django.db.models.deletion
import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', jsonfield.fields.JSONField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='ImageComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_description', models.CharField(blank=True, default='', max_length=100)),
                ('alt_text', models.CharField(blank=True, default='', max_length=50)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagefield', to='patcher.post')),
            ],
        ),
        migrations.CreateModel(
            name='TextFieldComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textfield', to='patcher.post')),
            ],
        ),
    ]
