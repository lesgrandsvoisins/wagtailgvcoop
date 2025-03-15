

from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, BaseSiteSetting, register_setting
from django.db import models
from wagtail.fields import RichTextField

@register_setting
class WagtailSettings(BaseGenericSetting):
    site_logo = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    homepage_link = models.URLField(
        null=True,
        blank=True,
    )
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)

    panels = [
        FieldPanel("site_logo"),
        FieldPanel("homepage_link"),
        FieldPanel("footer1"),
        FieldPanel("footer2"),
    ]

    class Meta:
        verbose_name = "Default Settings for All Websites"


@register_setting
class WebsiteSettings(BaseSiteSetting):
    site_logo = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    homepage_link = models.URLField(
        null=True,
        blank=True,
    )
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)
    csscolors = models.TextField(blank=True, null=True)
    panels = WagtailSettings.panels + [
        FieldPanel("csscolors"),
    ]
    class Meta:
        verbose_name = "Settings Per Website"