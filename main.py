import folium
import pandas
from funcs import style_func

volc_data = pandas.read_csv("Volcanoes.txt")
volc_map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg_volcs = folium.FeatureGroup(name="Volcanoes")

pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', 1000)
pandas.set_option('display.max_rows', 100)

lat_lon_dict = {}
for i in range(len(volc_data['LAT'])):
    volc_item = list()
    volc_item.append((volc_data['LAT'][i], volc_data['LON'][i]))
    volc_item.append(volc_data['ELEV'][i])

    lat_lon_dict[volc_data['NAME'][i]] = volc_item

print("Size: " + str(len(lat_lon_dict)))

for volc_name in lat_lon_dict.keys():
    volc_item = lat_lon_dict[volc_name]
    popup_text = volc_name + "\nElev: " + str(volc_item[1]) + "ft"
    marker_color = None

    if volc_item[1] > 3000:
        marker_color = 'red'
    elif volc_item[1] > 2000:
        marker_color = 'green'
    else:
        marker_color = 'blue'

    fg_volcs.add_child(folium.CircleMarker(location=volc_item[0], fill_color=marker_color, popup=popup_text, color='grey',
                                     fill_opacity=0.5))

fg_pop = folium.FeatureGroup("Population")
with open('world.json', 'r', encoding='utf-8-sig') as world_file:
    fg_pop.add_child(folium.GeoJson(data=world_file.read(), style_function=style_func))

volc_map.add_child(fg_volcs)
volc_map.add_child(fg_pop)
volc_map.add_child(folium.LayerControl())
volc_map.save("map.html")
