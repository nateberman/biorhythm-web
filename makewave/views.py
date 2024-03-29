from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json
import math
from datetime import date, datetime

# Create your views here.
@require_http_methods(["GET"])
def makewave(request, month, day, year):

	# query data conversions for data creation
	month = int(month)
	day = int(day)
	year = int(year)

	# query date creation
	birthday = date(year, month, day)

	# time delta and time conversion
	elapsed_days = date.today() - birthday # time delta
	elapsed_days_float = elapsed_days.total_seconds() # total seconds from query date
	elapsed_days_float /= 60 # seconds to minutes conversion
	elapsed_days_float /= 60 # minutes to hours conversion
	elapsed_days_float /= 24 # hours to days conversion
	
	# calculate biorhythm attributes
	physical = math.sin(2 * math.pi * elapsed_days_float / 23)
	emotional = math.sin(2 * math.pi * elapsed_days_float / 28)
	intellectual = math.sin(2 * math.pi * elapsed_days_float / 33)

	# generate biorhythm attribute dictionary
	biorhythm_wave = {
		'physical': physical,
		'emotional': emotional,
		'intellectual': intellectual
	}

	# convert biorhythm dictionary to json
	data = json.dumps(biorhythm_wave)

	# send http response
	return HttpResponse(data, mimetype='application/json')