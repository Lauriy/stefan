from rest_framework import serializers

from stefan.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    party = serializers.StringRelatedField()

    class Meta:
        model = Vote
        fields = ('party',)
