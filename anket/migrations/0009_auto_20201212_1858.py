# Generated by Django 3.1.3 on 2020-12-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anket', '0008_auto_20201212_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anket',
            name='alinabilecek_onlem',
            field=models.TextField(verbose_name='Sorun ve Çözüm İçin Tavsiyeler'),
        ),
    ]
