from wagtail.core.blocks import StreamBlock, StructBlock, ListBlock, CharBlock, TextBlock, URLBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class HeroSectionBlock(StructBlock):
    title = CharBlock(required=False, max_length=100, label='Hero title', default='We are heroes')
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
        default="These people are not incredibly wise. They're just normal. But because they're all \
                `Chief Something Officer` or they gave the startup loads of cash, they're definitely \
                important enough to be on our website..."
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
    question = CharBlock(required=True, max_length=80, label='Question')
    answer = TextBlock(required=True, label='Answer')
    bullet_image = ImageChooserBlock(required=False, label='Bullet image')
    more_info_url = URLBlock(required=False, label='URL', help_text='A link to be followed for more information on that question, feature or product')

    class Meta:
        icon = 'help'
        label = 'FAQ'


class FaqSectionBlock(StructBlock):
    title = CharBlock(required=False, max_length=100, label='Section Title'),
    description = TextBlock(required=False, max_length=100, label='Description')
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
    heading = CharBlock(required=False, max_length=100, label='Section Title'),
    description = TextBlock(required=False, max_length=100, label='Description')
    testimonials = ListBlock(TestimonialBlock(), label='Testimonials')

    class Meta:
        icon = 'placeholder'
        label = 'Testimonials Section'
