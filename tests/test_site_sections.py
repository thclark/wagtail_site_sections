from django.test import TestCase
from django.urls import reverse
from wagtail.tests.utils import WagtailPageTests, WagtailTestUtils
from wagtail.core.models import Page
from wagtail.tests.utils.form_data import nested_form_data, streamfield
from wagtail_site_sections.models import SectionPage
from wagtail_site_sections.serializers import SectionPageSerializer


class SiteSectionTestCase(WagtailPageTests, WagtailTestUtils):

    def test_page_serializer(self):

        root_page = Page.objects.get(pk=1)
        data = nested_form_data({
            'title': 'All the sections on display. Like freaking peacocks.',
            'body': streamfield([
                ('hero_section', {
                    'title': 'Hero title',
                    'subtitle': 'Hero subtitle',
                    # image = ImageChooserBlock(required=True, label='Hero image')
                    'content': streamfield([
                        ('button', {'text': 'button text', 'url': 'https://www.testing-streamfields-sucks.com'}),
                        ('video', 'https://www.youtube.com/watch?v=x_ZeDn-hHGE'),
                        ('quote', {'text': 'I am a super inspiring person', 'author': 'me'}),
                     ]),
                }),
                # TODO Test other section types
            ]),
        })
        self.assertCanCreate(root_page, SectionPage, data)
        page = SectionPage.objects.first()
        ser = SectionPageSerializer()
        representation = ser.to_representation(page)
