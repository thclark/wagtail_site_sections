# Generated by Django 2.1.4 on 2019-05-24 17:16

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('hero_section', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='We are heroes', label='Hero title', max_length=100, required=False)), ('subtitle', wagtail.core.blocks.TextBlock(default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', label='Hero subtitle', max_length=400, required=False)), ('content', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Label', max_length=80, required=False)), ('url', wagtail.core.blocks.URLBlock(label='URL', required=False))], help_text='A "call-to-action" button, like "Sign Up Now!"', label='Call to action', required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(label='Video', required=False)), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.CharBlock(required=False))], help_text='An inspiring quotation, optionally attributed to someone', label='Quote', required=False))], block_counts={'button': {'max_num': 1}, 'quote': {'max_num': 1}, 'video': {'max_num': 1}}, required=False))])), ('team_section', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.TextBlock(default="These people are not incredibly wise. They're just normal. But because they're all `Chief Something Officer` or they gave the startup loads of cash, they're definitely important enough to be on our website...", label='Description', max_length=100, required=False)), ('members', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(label='Name', max_length=80, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Photo', required=True)), ('role', wagtail.core.blocks.CharBlock(label='Role / Job Title', max_length=80, required=True)), ('biography', wagtail.core.blocks.TextBlock(label='Bio', required=False)), ('linked_in_url', wagtail.core.blocks.URLBlock(label='LinkedIn Page', required=False)), ('twitter_url', wagtail.core.blocks.URLBlock(label='Twitter Page', required=False))]), label='Team Members'))])), ('carousel_section', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.TextBlock(label='Description', max_length=100, required=False)), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())]), label='Images'))])), ('faq_section', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.TextBlock(label='Description', max_length=100, required=False)), ('faqs', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.CharBlock(label='Question', max_length=80, required=True)), ('answer', wagtail.core.blocks.TextBlock(label='Answer', required=True)), ('bullet_image', wagtail.images.blocks.ImageChooserBlock(label='Bullet image', required=False)), ('more_info_url', wagtail.core.blocks.URLBlock(help_text='A link to be followed for more information on that question, feature or product', label='URL', required=False))]), label='FAQs'))])), ('testimonial_section', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.TextBlock(label='Description', max_length=100, required=False)), ('testimonials', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock(label='Quote', max_length=100, required=True)), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Logo/Picture', required=False))]), label='Testimonials'))])), ('heading', wagtail.core.blocks.CharBlock(help_text='', icon='arrow-right', label='Heading', max_length=120, required=False))], blank=True, help_text='Add sections to the page')),
            ],
            options={
                'verbose_name': 'Section Page',
                'verbose_name_plural': 'Section Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
