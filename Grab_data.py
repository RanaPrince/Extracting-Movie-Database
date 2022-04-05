import requests,json
import os
import pandas as pd

API_Key = "d024caa9d7886c744a8c17f945d8a59e"

#HTTP requests or Methods
""" 
GET = grab data

POST = to add/update data

"""

# end point or a url
#  get/movie/{movie_id}
movie_id = 500
api_version = 3

api_base_url = f"https://api.themoviedb.org/{api_version}/"
endpoint_path = f"movie/{movie_id}"

endpoint = f"{api_base_url}{endpoint_path}?api_key={API_Key}&language=en-US"
print(endpoint)

# res_id = requests.get(endpoint)
# print(res_id.status_code)
# dat = res_id.json()
# #the data is dump in a file
# with open ('./Movie DB- API/dat.json', 'w', encoding='utf8') as f:
#     json.dump(dat, f , ensure_ascii=False)

# print("\nData Fetched from API as JSON")
# print(dat)



##Search any movie - this will return multiple results .based on the avialable search string

#using a bearer token version as per the movie data base uses a version version token not much has been added there yet 

search_string = "Endgame"
search_endpoint_path = f"search/movie"

search_endpoint = f"{api_base_url}{search_endpoint_path}?api_key={API_Key}&query={search_string}"
#  Opeining this available link in browser will also give us the required data in text form,
#  as the browser does the same thing we're to do

print(search_endpoint)
rs = requests.get(search_endpoint)
dats = rs.json()

with open ('./Movie DB- API/dats.json', 'w', encoding='utf8') as f:
    json.dump(dats, f , ensure_ascii=False)



def get_movie_data(movie_id):
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}/"
    endpoint_path = f"movie/{movie_id}"
    endpoint_id = f"{api_base_url}{endpoint_path}?api_key={API_Key}&language=en-US"
    
    response = requests.get(endpoint_id)
    if response.status_code in range(200,299):
        res_json = response.json() 
        return res_json
    else:
        print("Error in the page or the Movie_id entered is unavailable")
        pass   


##Search any movie - this will return multiple results .based on the avialable search string

#using a bearer token version as per the movie data base uses a version version token not much has been added there yet 


def search_movie(word):
    search_string = str(word)
    
    api_base_url = f"https://api.themoviedb.org/{api_version}/"
    search_endpoint_path = f"search/movie"
    search_endpoint = f"{api_base_url}{search_endpoint_path}?api_key={API_Key}&query={search_string}"
    # Opeining this available link in browser will also give us the required data in text form,
    # as the browser does the same thing we're to do

    # print(search_endpoint)

    rs = requests.get(search_endpoint)
    
    x = rs.json()['results']
    
    movie_list = []
    for movie in x:
        mid = movie['id']
        movie_list.append(mid)
    
    movie_data = []
    for m_id in movie_list:
        movie_data.append(get_movie_data(m_id))

    movie_df = pd.DataFrame(movie_data)

    return movie_df



df.to_csv(os.path.join(r'C:\Users\ranap\OneDrive\Desktop\Crawling & API\Movie DB- API',
                            f'Movies-SearchData.csv'),index=False)



#Method we need
