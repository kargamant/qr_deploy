# Generated by Django 3.0 on 2021-03-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='адрес электронной почты')),
                ('password', models.CharField(max_length=50, verbose_name='пароль')),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
