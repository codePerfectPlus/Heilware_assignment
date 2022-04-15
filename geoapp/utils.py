from heligeo import heliGeoprocessingService

# api key for heligeo, using it directly for assignment purposes
apikey = 'jhyterfvdrwesuyt'

def get_polygon_data(polygon1, polygon2):
    polygon_list = [polygon1, polygon2]
    union_data = heliGeoprocessingService.Union(apikey, polygon_list)
    return union_data