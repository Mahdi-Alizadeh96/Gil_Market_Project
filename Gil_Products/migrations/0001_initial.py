# Generated by Django 3.1.7 on 2021-06-22 18:06

import Gil_Products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Gil_Products_Category', '0001_initial'),
        ('Gil_Product_Brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_fa', models.CharField(max_length=150, verbose_name='نام محصول (فارسی)')),
                ('name_en', models.CharField(max_length=150, verbose_name='نام محصول (انگلیسی)')),
                ('year', models.IntegerField(verbose_name='سال تولید')),
                ('price', models.BigIntegerField(verbose_name='قیمت')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='درصد تخفیف')),
                ('description', models.TextField(verbose_name='توضیحات محصول')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Gil_Products.models.upload_image_path, verbose_name='تصویر اصلی')),
                ('image1', models.ImageField(blank=True, null=True, upload_to=Gil_Products.models.upload_image_path, verbose_name='1تصویر')),
                ('image2', models.ImageField(blank=True, null=True, upload_to=Gil_Products.models.upload_image_path, verbose_name='2تصویر')),
                ('image3', models.ImageField(blank=True, null=True, upload_to=Gil_Products.models.upload_image_path, verbose_name='3تصویر')),
                ('image4', models.ImageField(blank=True, null=True, upload_to=Gil_Products.models.upload_image_path, verbose_name='4تصویر')),
                ('active', models.BooleanField(default=False, verbose_name='موجود / ناموجود')),
                ('attributes', models.TextField(null=True, verbose_name='ویژگی های محصول')),
                ('brands', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gil_Product_Brand.productbrand', verbose_name='برندها')),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gil_Products_Category.productcategory', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
