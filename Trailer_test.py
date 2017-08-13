import httplib
import json
import urllib2
import Movie_names_instance
import fresh_tomatoes


conn = httplib.HTTPSConnection("api.themoviedb.org")
moviesval = {}

# Fetching movie details from  Movie_names_instance class
movies = [Movie_names_instance.avengers,Movie_names_instance.jack_reacher,Movie_names_instance.thor,Movie_names_instance.proposal,Movie_names_instance.planet_of_apes,Movie_names_instance.strange]
for movie in movies:
        # API to fetch movie poster
        url="/3/search/movie?api_key=bbb3d12e8c29321d17cd591a3fdacc49&query="+movie.name+"&year="+movie.year
        print(url)
        response = urllib2.urlopen("https://api.themoviedb.org/3/search/movie?api_key=bbb3d12e8c29321d17cd591a3fdacc49&query="+movie.name+"&year="+movie.year)

        json_obj = json.load(response)
        for i in json_obj['results']:
            id = str(i['id'])
            path = i['poster_path']

            # API to fetch movie youtube trailer id
            video_url = urllib2.urlopen("https://api.themoviedb.org/3/movie/"+id+"/videos?api_key=bbb3d12e8c29321d17cd591a3fdacc49&language=en-US")
            json_obj1 = json.load(video_url)
            for j in json_obj1['results']:
                key = j['key']
        movie_name = movie.name.replace('+',' ')

        # Dict with movie name as key and list(youtube_id, poster_image) as value
        moviesval[movie_name] = [key,path]
print ("info is"+str(moviesval))

# sending the moviesval(dict) to open the movie trailer page
fresh_tomatoes.open_movies_page(moviesval)

