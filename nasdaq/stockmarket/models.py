from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

@python_2_unicode_compatible

class Stock(models.Model):
	stock_name = models.CharField(max_length=50)
	ipo_date = models.DateTimeField('initial public offering')
	value = models.IntegerField(default=10)
	stock_code = models.CharField(max_length=4)
	transactions = models.IntegerField(default=0)
	def __str__(self):
		return self.stock_name

	def was_pub_recently(self):
		return self.ipo_date >= timezone.now() - datetime.timedelta(days=5)
