# Import dependancies
import folium
import pandas


# Read data from txt file with pandas and store varibles with list passing the column name
data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

# Define function to generate colors to the background of the volcanoes markers depending on the elevation(column)
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# Starts variable map and Define the starting latitude, longitude and zoom of the map
map = folium.Map(location=[39.49, -117.06], zoom_start=6)

# Define variable with feature group name for volcanoes and loop through it passing the columns lat lon and elev
# Pass the add child to add to the feature group the circle marker passing the formating arguments of the marker
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+'m', fill_color=color_producer(el), color='grey', fill_opacity=0.7))


# Define variable with feature group name for population, add child to fg, open the json file with the encoding
# start local unamed function (lambda) to colorize the background based on the population of the country
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 200000000 else 'red'}))


map.add_child(fgv) # add child to the map
map.add_child(fgp) # add child to the map
map.add_child(folium.LayerControl()) # add control layer to the map

map.save('Map1.html') # save and send map to html file
