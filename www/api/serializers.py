from rest_framework import serializers

from .models import VoltageSample


class VoltageSampleSerializer(serializers.ModelSerializer):
	class Meta:
		model = VoltageSample
		fields = ("cell_id", "voltage", "timestamp",)
