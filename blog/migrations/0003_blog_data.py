# Generated by Django 4.0 on 2021-12-22 23:42

from django.db import migrations
from datetime import date


POSTS = (
	{
		'title': 'How To Use Canva To Create Gorgeous Blog Graphics',
		'slug': 'how-to-use-canva-to-create-gorgeous-blog-graphics',
		'text': "Whether you've been blogging for a while, or just started you've probably realized that having nice images and/or graphics for your posts is just as important as the words your writer. An unattractive image/graphic can turn readers away from an otherwise great post. It can also keep your post from being shared on social media.",
		'pub_date': date(2021, 12, 22),
		'tags': [
			{'name': 'canva', 'slug': 'canva'},
			{'name': 'design', 'slug': 'design'},
			{'name': 'blog', 'slug': 'blog'},
		],
		'startups': [
			{
				'name': 'CANVA',
				'slug': 'canva',
				'founded_date': date(2013, 12, 22),
			},
		],
	},
)


def add_blog_data(apps, schema_editor):
	Post = apps.get_model('blog', 'Post')
	for post in POSTS:
		post_object = Post.objects.get_or_create(
			title = post.get('title'),
			slug = post.get('slug'),
			text = post.get('text'),
			pub_date = post.get('pub_date'),
		)[0]
		post_object.save()


def remove_blog_data(apps, schema_editor):
	Post = apps.get_model('blog', 'Post')
	for post in POSTS:
		post_object = Post.objects.get(
			slug = post.get('slug')
		)
		post_object.delete()


class Migration(migrations.Migration):

	dependencies = [
		('blog', '0002_alter_post_pub_date'),
		('organizer', '0005_startup_data'),
	]

	operations = [
		migrations.RunPython(
			add_blog_data,
			remove_blog_data,
		)
	]
