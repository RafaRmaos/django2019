# Generated by Django 2.0.13 on 2019-08-20 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_produto_fornecedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='fornecedor',
        ),
    ]
