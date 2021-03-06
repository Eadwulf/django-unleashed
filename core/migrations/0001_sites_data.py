# Generated by Django 4.0 on 2022-01-03 15:08

from django.db import migrations


def add_site_data(apps, schema_editor):
	Site = apps.get_model('sites', 'Site')
	site_id = getattr('settings', 'SITE_ID', 1)

	if Site.objects.exists():
		site = Site.objects.get(pk=site_id)
		site.domain = 'site.django-unleashed.com'
		site.name = 'Startup Organizer'
		site.save()
	else:
		Site.objects.create(
			domain = 'site.django-unleashed.com',
			name = 'Startup Organizer',
			pk = site_id,
		)

def remove_site_data(apps, schema_editor):
	Site = apps.get_model('sites', 'Site')
	site = Site.objects.get(
		pk = getattr('settings', 'SITE_ID', 1)
	)
	site.domain = 'example.com'
	site.name = 'example.com'
	site.save()


class Migration(migrations.Migration):

    dependencies = [
		('sites', '0001_initial'),
    ]

    operations = [
		migrations.RunPython(
			add_site_data,
			remove_site_data,
		),
    ]
