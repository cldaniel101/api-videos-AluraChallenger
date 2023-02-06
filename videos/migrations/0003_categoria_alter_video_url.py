# Generated by Django 4.1.6 on 2023-02-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_rename_videos_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('cor', models.CharField(choices=[('VM', 'Vermelho'), ('VD', 'Verde'), ('AZ', 'Azul'), ('AM', 'Amarelo'), ('L', 'Laranja'), ('R', 'Rosa')], default='VM', max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(max_length=100, unique=True),
        ),
    ]
