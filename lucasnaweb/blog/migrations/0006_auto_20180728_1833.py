# Generated by Django 2.0.7 on 2018-07-28 21:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180728_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('subtitle', models.CharField(default='', max_length=200)),
                ('text', models.TextField()),
                ('jumbotron', models.ImageField(default='header-blog-posts.jpg', upload_to='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]