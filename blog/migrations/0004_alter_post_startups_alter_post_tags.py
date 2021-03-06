# Generated by Django 4.0 on 2021-12-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0009_alter_startup_tags'),
        ('blog', '0003_blog_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='startups',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='organizer.Startup'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='organizer.Tag'),
        ),
    ]
