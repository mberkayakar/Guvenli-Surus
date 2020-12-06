# Generated by Django 3.1.3 on 2020-12-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='İletisim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50, verbose_name='lütfen Sizinle iletişime geçebilmemiz adına gereçli bir e posta adresi giriniz')),
                ('subject', models.CharField(max_length=150, verbose_name='Hangi konu hakkında bizimle ilerişime geçmek istersiniz ?')),
                ('message', models.CharField(max_length=2000, verbose_name='mesajınızı bize detaylı olarak anlatınız')),
            ],
        ),
    ]
