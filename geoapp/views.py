import json
import folium

from django.shortcuts import render
from .utils import get_polygon_data

# Create your views here.
def indexView(request):
	if request.method == 'POST':
		# get form data
		json_data = request.POST['JsonData']
		data = json.loads(json_data)

		polygon1 = data['polygon1']
		polygon2 = data['polygon2']

		union_data = get_polygon_data(polygon1, polygon2)
		
		cords = union_data['features'][0]['geometry']['coordinates'][0]

		reversed_cord = []
		for cord in cords:
			reversed_cord.append(cord[::-1])
		
		map = folium.Map(location=reversed_cord[0], zoom_start=12)

		for cord in reversed_cord:
			folium.Marker(location=cord).add_to(map)
		
		map = map._repr_html_()
		context = {'map': map, 'title': 'Union Polygon'}
	
		return render(request, 'geoapp/show_folium_map.html', context)
	
	context = {'title': 'HomePage '}
	return render(request, 'geoapp/index.html', context=context)


