from django.shortcuts import render
import requests
# Create your views here.
def get_country_data():
    url = "https://restcountries.com/v3.1/all"  # JSON verisi içeren URL'yi buraya girin
    response = requests.get(url)
    if response.status_code == 200:
        json_datas = response.json()
        return json_datas
    else:
        return None
def countries(request):    
    country_list = []

    for country in get_country_data():
        country_name = country['name']['common']
        official_name = country['name']['official']
        flag_url = country['flags']['png']

        country_info = {
            'country_name': country_name,
            'official_name': official_name,
            'flag_url': flag_url
        }

        country_list.append(country_info)

    context = {
        'countries': country_list
    }

    return render(request, 'countries.html', context)