import folium
import csv
m = folium.Map(location=[52.2332,21.0614], zoom_start=7)
m.show_in_browser()

with open("dane_prezentacja.csv","r") as plik:
        dane=csv.reader(plik,delimiter=";")
        for i in dane:
            if i[0]=="stacja":
                continue
            if float(i[4])>5  :
                folium.Marker([i[1],i[2]],popup=f"<p>{i[3]}</p><p>temp:{i[4]}</p>").add_to(m)
m.show_in_browser()
        
