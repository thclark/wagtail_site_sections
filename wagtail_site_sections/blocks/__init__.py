from .base import HashBlock, SectionBlock  # noqa
from .blocks import HeroSectionBlock, TeamMemberBlock, TeamSectionBlock, CarouselImageBlock, CarouselSectionBlock  # noqa
from .blocks import FaqBlock, FaqSectionBlock, TestimonialBlock, TestimonialSectionBlock  # noqa
from .blocks import ProductBlock, ProductSectionBlock, FeatureBlock, FeatureSectionBlock  # noqa
from .material_icons import IconChoiceBlock  # noqa

# noqa avoids "unused imports in __init__.py" error when using flake8


# Simply add this to any existing list of streamfield blocks in a content panel to enable creation of sections
section_blocks = [
    ('carousel_section', CarouselSectionBlock()),
    ('faq_section', FaqSectionBlock()),
    ('feature_section', FeatureSectionBlock()),
    ('product_section', ProductSectionBlock()),
    ('hero_section', HeroSectionBlock()),
    ('team_section', TeamSectionBlock()),
    ('testimonial_section', TestimonialSectionBlock()),
]
