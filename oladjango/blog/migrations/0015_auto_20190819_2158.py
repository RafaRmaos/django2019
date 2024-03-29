# Generated by Django 2.0.13 on 2019-08-20 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_produto_fornecedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Cidade'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Fornecedor'),
        ),
    ]
