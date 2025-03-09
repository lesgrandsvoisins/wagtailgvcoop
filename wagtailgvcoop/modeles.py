from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class GvcoopPageHome(Page):
    section1 = RichTextField(blank=True, null=True)
    section2 = RichTextField(blank=True, null=True)
    section3 = RichTextField(blank=True, null=True)
    agenda = RichTextField(blank=True, null=True)
    ghost_tag = models.CharField(blank=True, null=True, max_length=255)
    ghost_filter = models.CharField(blank=True, null=True, max_length=255)
    ghost_order = models.CharField(blank=True, null=True, max_length=255)
    # ghost_formats = models.CharField(blank=True, null=True, max_length=255)
    ghost_limit = models.CharField(blank=True, null=True, max_length=8)
    ghost_include = models.CharField(blank=True, null=True, max_length=255)
    page_description = "Une page home "

    content_panels = FaireMainHomePage.content_panels + [
        FieldPanel("section1"),
        FieldPanel("section2"),
        FieldPanel("section3"),
    ] + [
        FieldPanel("agenda"),
        FieldPanel("ghost_tag"),
        FieldPanel("ghost_filter"),
        FieldPanel("ghost_order"),
        FieldPanel("ghost_limit"),
        FieldPanel("ghost_include"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        params = {
            "ghost_tag": self.ghost_tag,
            "ghost_limit": self.ghost_limit,
            "ghost_include": self.ghost_include,
            "ghost_order": self.ghost_order,
            "ghost_filter": self.ghost_filter,
            "ghost_page": request.GET.get("page", 1),
        }
        context["posts"] = lesgv.services.get_blog_posts(lesgv.services.ProcessGhostParams(params))
        return context