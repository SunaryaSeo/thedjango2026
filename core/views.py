from django.shortcuts import render
import pandas as pd
import folium
from pathlib import Path


# Create your views here.
BASE_PATH = Path(__file__).resolve().parent

#csv_path = BASE_PATH / "static" / "data" / "data_populasi.csv"
csv_path = BASE_PATH / "data" / "data_populasi.csv"
df=pd.read_csv(csv_path)
names=df['nama'].dropna().unique().tolist()



def home(request):
    return render(request, 'core/home.html')

def map(request):
    minPol=0
    keyword=''
    name=''
    if request.method=='POST':
        try:
             minPol=int(request.POST.get('minPol', 0))
        except (ValueError, TypeError):
            minPol=0
        keyword=request.POST.get('keyword',"")
        name=request.POST.get('name',"")

    filtered=df[
        (df["populasi"]>=minPol) &
        (df["nama"].str.contains(keyword, case=False, na=False)) &
        (df["nama"].str.contains(name, case=False, na=False))
    ]
    
        #filtered=df[(df['populasi'] >=minPol) & (df['nama'].str.contains(keyword))]
    m=folium.Map(location=[-6.5, 107.0], zoom_start=8, width="100%",height="700px")
    for _, row in filtered.iterrows():
        popup=f"{row['nama']} <br> Populasi:{row['populasi']:,}"
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=popup,
            tooltip=row["nama"]
        ).add_to(m)

    #Menyimpan map to HTML string
    map_html=m._repr_html_()


    return render (request, 'core/map.html', {'map_html': map_html, 'minPol':minPol, 'keyword':keyword, 'names':names,})

def hki(request):
    return render(request, 'core/hki.html')

def certification(request):
    return render(request, 'core/certification.html')

def journal(request):
    return render(request, 'core/journal.html')

def conference(request):
    return render(request, 'core/conference.html')