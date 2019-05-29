from wagtail.core.blocks import BooleanBlock, StreamBlock, StructBlock, ListBlock, CharBlock, TextBlock, URLBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class HeroSectionBlock(StructBlock):
    title = CharBlock(required=False, max_length=100, label='Hero title', default='We are heroes')
    show_in_menus = BooleanBlock(required=False, label='Show in menus', default=False, help_text='If your frontend supports it, create a link to this part of the page.')
    subtitle = TextBlock(
        required=False,
        max_length=400,
        label='Hero subtitle',
        default='The thing we do is better than any other similar thing and this hero panel will \
                convince you of that, just by having a glorious background image.')
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
    linked_in_url = URLBlock(required=False, label='LinkedIn Page')
    twitter_url = URLBlock(required=False, label='Twitter Page')

    class Meta:
        icon = 'user'
        label = 'Team Member'


class TeamSectionBlock(StructBlock):
    title = CharBlock(required=False, max_length=100, label='Section title', default='Our illustrious leaders'),
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
    title = CharBlock(required=False, max_length=80, label='Main text'),
    subtitle = TextBlock(required=False, label='Sub text'),
    more_info_url = URLBlock(required=False, label='Link URL'),

    class Meta:
        icon = 'image'
        label = 'Carousel Image'


class CarouselSectionBlock(StructBlock):
    title = CharBlock(required=False, max_length=100, label='Section title'),
    description = TextBlock(required=False, max_length=100, label='Description')
    images = ListBlock(CarouselImageBlock(), label='Images')

    class Meta:
        icon = 'image'
        label = 'Carousel Section'


class FaqBlock(StructBlock):
    question = CharBlock(required=True, max_length=80, label='Question', help_text="Add a simply worded question, like 'How much will it cost?'")
    answer = TextBlock(required=True, label='Answer', help_text='Provide a short answer in no more than a few lines of text')
    bullet_image = ImageChooserBlock(required=False, label='Bullet image', help_text='Pick an image for use as a bullet point for this question')
    more_info_url = URLBlock(required=False, label='URL', help_text='Add a link to be followed for more information on that question, feature or product')

    class Meta:
        icon = 'help'
        label = 'FAQ'


class FaqSectionBlock(StructBlock):
    heading = CharBlock(required=False, max_length=100, label='Heading'),
    description = TextBlock(required=False, max_length=400, label='Description')
    faqs = ListBlock(FaqBlock(), label='FAQs')

    class Meta:
        icon = 'help'
        label = 'FAQs Section'


class TestimonialBlock(StructBlock):
    person_name = CharBlock(required=False, max_length=100, label='Name'),
    organisation_name = CharBlock(required=False, max_length=100, label='Organisation'),
    quote = TextBlock(required=True, max_length=100, label='Quote')
    logo = ImageChooserBlock(required=False, label='Logo/Picture')

    class Meta:
        icon = 'quote'
        label = 'Testimonial'


class TestimonialSectionBlock(StructBlock):
    heading = CharBlock(required=False, max_length=100, label='Heading', default='Testimonials', help_text='Add a heading at the beginning of this page section'),
    description = TextBlock(required=False, max_length=400, label='Description', default='Our users love us. Look at these rave reviews...')
    testimonials = ListBlock(TestimonialBlock(), label='Testimonials')

    class Meta:
        icon = 'placeholder'
        label = 'Testimonials Section'


class FeatureBlock(StructBlock):
    heading = CharBlock(required=True, max_length=80, label='Feature', help_text="Name of a product feature. Keep it short, like 'Free Chat' or 'Secure'")
    description = TextBlock(required=True, max_length=400, label='Description', help_text='Write a few lines about this feature')
    bullet_image = ImageChooserBlock(required=False, label='Image', help_text='Pick an image for use as a bullet point in this feature')
    more_info_url = URLBlock(required=False, label='URL', help_text='A link to be followed for more information')

    class Meta:
        icon = 'tick-inverse'
        label = 'Product Feature Description'


class FeatureSectionBlock(StructBlock):
    heading = CharBlock(required=False, max_length=100, label='Heading', default='Why our product is best', help_text='Add a heading at the beginning of this page section'),
    description = TextBlock(required=False, max_length=400, label='Description', help_text='This is the paragraph where you can write more details about your product. Keep it meaningful!')
    features = ListBlock(FeatureBlock(), label='Features')

    class Meta:
        icon = 'list-ul'
        label = 'Product Features Section'


class ProductBlock(StructBlock):
    heading = CharBlock(required=True, max_length=80, label='Name', help_text="Name of a product. Keep it short, like 'Free Chat' or 'Secure'")
    description = TextBlock(required=True, max_length=400, label='Description', help_text='Write a few lines about this feature')
    bullet_image = ImageChooserBlock(required=False, label='Image', help_text='Pick an image for use as a bullet point in this feature')
    more_info_url = URLBlock(required=False, label='URL', help_text='A link to be followed for more information')

    class Meta:
        icon = 'tick-inverse'
        label = 'Product Overview'


class ProductSectionBlock(StructBlock):
    heading = CharBlock(required=False, max_length=100, label='Heading', default='Some of our awesome products', help_text='Add a heading at the beginning of this page section'),
    description = TextBlock(required=False, max_length=400, label='Description', help_text='This is the paragraph where you can write more details about your product. Keep it meaningful!')
    features = ListBlock(FeatureBlock(), label='Features')

    class Meta:
        icon = 'list-ul'
        label = 'Products Overview Section'
