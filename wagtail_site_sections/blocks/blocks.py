from wagtail.core.blocks import StreamBlock, StructBlock, ListBlock, CharBlock, TextBlock, URLBlock, ChoiceBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from .base import SectionBlock
from .material_icons import IconChoiceBlock


class HeroSectionBlock(SectionBlock):
    heading = CharBlock(required=False, max_length=100, label='Hero title', default='We are heroes')
    description = TextBlock(
        required=False,
        max_length=400,
        label='Hero subtitle',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.'
    )
    image = ImageChooserBlock(required=False, label='Hero image')
    content = StreamBlock([
        ('button', StructBlock([
            ('text', CharBlock(required=False, max_length=80, label='Label')),
            ('url', URLBlock(required=False, label='URL')),
        ], required=False, label='Call to action', help_text='A "call-to-action" button, like "Sign Up Now!"')),
        ('video', EmbedBlock(required=False, label='Video')),
        ('quote', StructBlock([
            ('text', TextBlock()),
            ('author', CharBlock(required=False)),
        ], required=False, label='Quote', help_text='An inspiring quotation, optionally attributed to someone'))
    ], required=False, block_counts={'button': {'max_num': 1}, 'video': {'max_num': 1}, 'quote': {'max_num': 1}})

    class Meta:
        icon = 'placeholder'
        label = 'Hero Section'


class TeamMemberBlock(StructBlock):
    name = CharBlock(required=True, max_length=80, label='Name')
    image = ImageChooserBlock(required=True, label='Photo')
    role = CharBlock(required=True, max_length=80, label='Role / Job Title')
    biography = TextBlock(required=False, label='Bio')
    linkedin = URLBlock(required=False, label='LinkedIn Page')
    twitter = URLBlock(required=False, label='Twitter Page')

    class Meta:
        icon = 'user'
        label = 'Team Member'


class TeamSectionBlock(SectionBlock):
    heading = CharBlock(required=False, max_length=100, label='Heading', default='Our illustrious leaders'),
    description = TextBlock(
        required=False,
        max_length=100,
        label='Description',
        default='Here is a list of our Head Peeps. They look glorious rendered in HTML but are probably just normal, mortal humans.'
    )
    members = ListBlock(TeamMemberBlock(), label='Team Members')

    class Meta:
        icon = 'group'
        label = 'Team Section'


class CarouselImageBlock(StructBlock):
    image = ImageChooserBlock()
    heading = CharBlock(required=False, max_length=80, label='Main text', help_text='Add an image subtitle'),
    description = TextBlock(required=False, label='Description', help_text='Add some descriptive information with your image'),
    more_info_url = URLBlock(required=False, label='Link URL'),

    class Meta:
        icon = 'image'
        label = 'Carousel Image'


class CarouselSectionBlock(SectionBlock):
    heading = CharBlock(required=False, max_length=100, label='Heading', help_text='Add a heading at the beginning of this page section'),
    description = TextBlock(required=False, max_length=100, label='Description', help_text='Provide a slightly more detailed description of what this carousel section is for')
    images = ListBlock(CarouselImageBlock(), label='Images')

    class Meta:
        icon = 'image'
        label = 'Carousel Section'


class FaqBlock(StructBlock):
    question = CharBlock(required=True, max_length=80, label='Question', help_text="Add a simply worded question, like 'How much will it cost?'")
    answer = TextBlock(required=True, label='Answer', help_text='Provide a short answer in no more than a few lines of text')
    icon = IconChoiceBlock(required=True, label='Icon', help_text='Pick an icon (see https://material.io/tools/icons/) for a bullet point')
    more_info_url = URLBlock(required=False, label='URL', help_text='Add a link to be followed for more information on that question, feature or product')

    class Meta:
        icon = 'help'
        label = 'FAQ'


class FaqSectionBlock(SectionBlock):
    heading = CharBlock(required=False, max_length=100, label='Heading', help_text='Add a heading at the beginning of this page section'),
    description = TextBlock(required=False, max_length=400, label='Description')
    faqs = ListBlock(FaqBlock(), label='FAQs')

    class Meta:
        icon = 'help'
        label = 'FAQs Section'


class TestimonialBlock(StructBlock):
    name = CharBlock(required=True, max_length=100, label='Name', help_text='Name of the person making the recommendation'),
    role = CharBlock(required=False, max_length=100, label='Role', help_text='Job title of the person making the recommentation, if any'),
    organisation = CharBlock(required=False, max_length=100, label='Organisation', help_text='Name of the organisation the person is part of, if any'),
    quote = TextBlock(required=True, max_length=100, label='Quote', help_text='The nice things they have to say')
    image = ImageChooserBlock(required=False, label='Logo/Picture', help_text="Add either a company logo or a person's mugshot")
    stars = ChoiceBlock(required=True, choices=[
        (None, 'No rating'),
        (0, '0 Stars'),
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars')
    ], icon='pick')

    class Meta:
        icon = 'pick'
        label = 'Testimonial'


class TestimonialSectionBlock(SectionBlock):
    heading = CharBlock(required=False, max_length=100, label='Heading', default='Testimonials', help_text='Add a heading at the beginning of this page section'),
    description = TextBlock(required=False, max_length=400, label='Description', default='Our users love us. Look at these rave reviews...')
    testimonials = ListBlock(TestimonialBlock(), label='Testimonials')

    class Meta:
        icon = 'pick'
        label = 'Testimonials Section'


class FeatureBlock(StructBlock):
    heading = CharBlock(required=True, max_length=80, label='Feature', help_text="Feature name. Keep it short, like 'Free Chat' or 'Secure'")
    description = TextBlock(required=True, max_length=400, label='Description', help_text='Write a few lines about this feature')
    icon = IconChoiceBlock(required=True, label='Icon', help_text='Pick an icon (see https://material.io/tools/icons/) for a bullet point')
    more_info_url = URLBlock(required=False, label='URL', help_text='A link to be followed for more information')

    class Meta:
        icon = 'tick-inverse'
        label = 'Product Feature Description'


class FeatureSectionBlock(SectionBlock):
    heading = CharBlock(required=False, max_length=100, label='Heading', default='Why our product is best', help_text='Add a heading at the beginning of this page section'),
    description = TextBlock(required=False, max_length=400, label='Description', help_text='This is the paragraph where you can write more details about your product. Keep it meaningful!')
    image = ImageChooserBlock(required=False, label='Image', help_text='Pick an image (e.g. of the product) for the side panel of a feature list')
    features = ListBlock(FeatureBlock(), label='Features')

    class Meta:
        icon = 'list-ul'
        label = 'Product Features Section'


class ProductBlock(StructBlock):
    heading = CharBlock(required=True, max_length=80, label='Name', help_text="Name of a product. Keep it short, like 'Mega Kit Pro' or 'Cloud Manager'")
    description = TextBlock(required=True, max_length=400, label='Description', help_text='Write a few lines about this product')
    image = ImageChooserBlock(required=False, label='Image', help_text='Pick an image to represent this product')
    more_info_url = URLBlock(required=False, label='URL', help_text='A link to be followed for more information')

    class Meta:
        icon = 'tick-inverse'
        label = 'Product Overview'


class ProductSectionBlock(SectionBlock):
    heading = CharBlock(required=False, max_length=100, label='Heading', default='Some of our awesome products', help_text='Add a heading at the beginning of this page section'),
    description = TextBlock(required=False, max_length=400, label='Description', help_text='This is the paragraph where you can write more details about your product. Keep it meaningful!')
    features = ListBlock(FeatureBlock(), label='Features')

    class Meta:
        icon = 'list-ul'
        label = 'Products Overview Section'
