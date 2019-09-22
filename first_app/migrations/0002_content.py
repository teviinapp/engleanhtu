# Generated by Django 2.2.5 on 2019-09-07 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('content', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='images')),
                ('webpage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='first_app.Webpage')),
            ],
        ),
    ]
