from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import VoltageSample
from .serializers import VoltageSampleSerializer



@api_view(["POST"])
def voltage(request):
	"""Save every sensor data into our DB"""

	reading = VoltageSampleSerializer(data=request.data)
	if not reading.is_valid():
		return Response(reading.errors, status=status.HTTP_400_BAD_REQUEST)
	
	reading.save()
	return Response(reading.data, status=status.HTTP_201_CREATED)
