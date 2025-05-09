
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
import gdvoisins.services
from .utils import notanytest
from .settings import WebsiteSettings, WagtailSettings

class GdVoisinsHomePage(Page):
    body = RichTextField(blank=True, null=True)
    intro = RichTextField(blank=True, null=True)
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)
    ghost_post_tag = models.SlugField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    redirect_url = models.URLField(blank=True, null=True)
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

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("intro"),
        FieldPanel("ghost_post_tag"),
        FieldPanel("image"),
        FieldPanel("section1"),
        FieldPanel("section2"),
        FieldPanel("section3"),
        FieldPanel("agenda"),
        FieldPanel("ghost_tag"),
        FieldPanel("ghost_filter"),
        FieldPanel("ghost_order"),
        FieldPanel("ghost_limit"),
        FieldPanel("ghost_include"),
    ]
    settings_panels = [
        # FieldPanel("theme"),
        # FieldPanel("extramenu"),
        FieldPanel("footer1"),
        FieldPanel("footer2"),
        FieldPanel("redirect_url"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["website_settings"] = WebsiteSettings.for_request(request=request)
        context["wagtail_settings"] = WagtailSettings.load(request_or_site=request)
        # for item in ["site_logo", "homepage_link", "footer1", "footer2", "theme", "menu"]:
        for item in ["site_logo", "homepage_link", "footer1", "footer2"]:
            context[item] = getattr(context["website_settings"], item)
            if notanytest(context[item]):
                context[item] = getattr(context["wagtail_settings"], item)
        # for item in ["site_logo", "homepage_link", "footer1", "footer2", "theme", "menu"]:
        for item in ["site_logo", "homepage_link", "footer1", "footer2"]:
            context[item] = getattr(context["website_settings"], item)
            if hasattr(self, item) and getattr(self, item) != "":
                context[item] = getattr(self, item)
            elif notanytest(context[item]):
                context[item] = getattr(context["wagtail_settings"], item)
        # if hasattr(self, "extramenu") and getattr(self, "extramenu") != "":
        #     context["extramenu"] = getattr(self, "extramenu")
        else:
            context["extramenu"] = []
        # context["menuitems"] = gdvoisinsGetMenuItems(self)
        # context["breadcrumbs"] = gdvoisinsGetBreadcrumbs(self)
        params = {
            "ghost_tag": self.ghost_tag,
            "ghost_limit": self.ghost_limit,
            "ghost_include": self.ghost_include,
            "ghost_order": self.ghost_order,
            "ghost_filter": self.ghost_filter,
            "ghost_page": request.GET.get("page", 1),
        }
        context["posts"] = gdvoisins.services.get_blog_posts(gdvoisins.services.ProcessGhostParams(params))
        return context
