from django.db import models


SHORT_TEXT = 16


class VoltageSample(models.Model):
    cell_id = models.CharField(max_length=SHORT_TEXT)
    voltage = models.DecimalField(decimal_places=2, max_digits=4)
    timestamp = models.DateTimeField(auto_now=True)
