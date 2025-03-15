# Generated by Django 5.1.7 on 2025-03-09 20:44

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='GdVoisinsHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.RichTextField(blank=True, null=True)),
                ('intro', wagtail.fields.RichTextField(blank=True, null=True)),
                ('footer1', wagtail.fields.RichTextField(blank=True, null=True)),
                ('footer2', wagtail.fields.RichTextField(blank=True, null=True)),
                ('ghost_post_tag', models.SlugField(blank=True, null=True)),
                ('redirect_url', models.URLField(blank=True, null=True)),
                ('section1', wagtail.fields.RichTextField(blank=True, null=True)),
                ('section2', wagtail.fields.RichTextField(blank=True, null=True)),
                ('section3', wagtail.fields.RichTextField(blank=True, null=True)),
                ('agenda', wagtail.fields.RichTextField(blank=True, null=True)),
                ('ghost_tag', models.CharField(blank=True, max_length=255, null=True)),
                ('ghost_filter', models.CharField(blank=True, max_length=255, null=True)),
                ('ghost_order', models.CharField(blank=True, max_length=255, null=True)),
                ('ghost_limit', models.CharField(blank=True, max_length=8, null=True)),
                ('ghost_include', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WagtailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepage_link', models.URLField(blank=True, null=True)),
                ('footer1', wagtail.fields.RichTextField(blank=True, null=True)),
                ('footer2', wagtail.fields.RichTextField(blank=True, null=True)),
                ('site_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Default Settings for All Websites',
            },
        ),
        migrations.CreateModel(
            name='WebsiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepage_link', models.URLField(blank=True, null=True)),
                ('footer1', wagtail.fields.RichTextField(blank=True, null=True)),
                ('footer2', wagtail.fields.RichTextField(blank=True, null=True)),
                ('csscolors', models.TextField(blank=True, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
                ('site_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Settings Per Website',
            },
        ),
    ]
