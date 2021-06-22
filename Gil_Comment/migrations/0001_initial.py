# Generated by Django 3.1.7 on 2021-06-22 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Gil_Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام کاربر')),
                ('message', models.TextField(verbose_name='متن پیام')),
                ('postedTime', models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال')),
                ('active', models.BooleanField(default=False, verbose_name='نمایش / عدم نمایش')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Gil_Products.product', verbose_name='نام محصول')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
    ]
