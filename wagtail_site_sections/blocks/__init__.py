from .blocks import HeroSectionBlock, TeamMemberBlock, TeamSectionBlock, CarouselImageBlock, CarouselSectionBlock, \
    FaqBlock, FaqSectionBlock, TestimonialBlock, TestimonialSectionBlock # noqa

# noqa avoids unused imports in __init__.py bug with flake8


# Simply add this to any existing list of streamfield blocks in a content panel to enable creation of sections
section_blocks = [
    ('hero_section', HeroSectionBlock()),
    ('team_section', TeamSectionBlock()),
    ('carousel_section', CarouselSectionBlock()),
    ('faq_section', FaqSectionBlock()),
    ('testimonial_section', TestimonialSectionBlock()),
]
