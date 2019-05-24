import factory
from wagtail_factories import PageFactory

from wagtail_site_sections.models import SectionPage


class SectionPageFactory(PageFactory):
    """
    Factory for wagtail_references.models.Reference
    """
    title = factory.Sequence('SectionPage {}'.format)

    class Meta(object):
        model = SectionPage
