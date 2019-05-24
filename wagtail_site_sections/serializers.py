import logging
from rest_framework import serializers
from wagtail.api.v2.serializers import StreamField

from .models import SectionPage


logger = logging.getLogger(__name__)


class SectionPageSerializer(serializers.ModelSerializer):

    body = StreamField()

    class Meta:
        model = SectionPage
        fields = (
            'title',
            'slug',
            'body',
        )
        read_only_fields = fields
