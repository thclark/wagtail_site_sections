import logging
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import CharBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from wagtail_site_sections.blocks import section_blocks


logger = logging.getLogger(__name__)


class SectionPage(Page):
    """ SectionPage has the normal page content and SEO panels.
    Its content additionally includes the field 'body' which can contain any number of sections via a streamfield.

    You can add stream fields other than just section blocks to the body, for example:
    ```
    from wagtail_site_sections import blocks
    body = StreamField([
        ('heading', CharBlock(required=False, label='Heading', max_length=120, help_text='', icon='arrow-right')),
        ('subheading', CharBlock(required=False, label='Subheading', max_length=120, help_text='', icon='arrow-right')),
        ('image', ImageChooserBlock(required=False, label='Image', help_text='')),
        ('quote', BlockQuoteBlock(required=False, label='Quote', help_text='')),
        ('paragraph', TextBlock(required=False, label='Paragraph', help_text='')),
    ] + blocks.section_blocks, blank=True, help_text='')
    ```

    Or you could choose only some blocks to enable for a page like so:
    ```
    body = StreamField([
        ('team_section', blocks.TeamSectionBlock()),
        ('faq_section', blocks.FaqSectionBlock()),
        ('testimonial_section', blocks.TestimonialSectionBlock()),
    ])
    ```
    """

    body = StreamField(section_blocks + [
        ('heading', CharBlock(required=False, label='Heading', max_length=120, help_text='', icon='arrow-right')),
    ], blank=True, help_text='Add sections to the page')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', heading='Page sections'),
    ]

    class Meta:
        verbose_name = 'Section Page'
        verbose_name_plural = 'Section Pages'
