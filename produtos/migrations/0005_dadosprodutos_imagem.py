# Generated by Django 2.0.4 on 2018-04-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20180417_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosprodutos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens'),
        ),
    ]
