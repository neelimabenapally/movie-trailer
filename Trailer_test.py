import httplib
import json
import urllib2
import Movie_names_instance
import Movie_info

movie_details = Movie_info.Movie_information()
conn = httplib.HTTPSConnection("api.themoviedb.org")
movies = [Movie_names_instance.jack_reacher,Movie_names_instance.me_before_you,Movie_names_instance.thor,Movie_names_instance.proposal,Movie_names_instance.dresses]
for movie in movies:

        url="/3/search/movie?api_key=bbb3d12e8c29321d17cd591a3fdacc49&query="+movie.name+"&year="+movie.year
        print(url)
        response = urllib2.urlopen("https://api.themoviedb.org/3/search/movie?api_key=bbb3d12e8c29321d17cd591a3fdacc49&query="+movie.name+"&year="+movie.year)

        json_obj = json.load(response)
        # print(json_obj)
        for i in json_obj['results']:

            # print ("poster path is:"+i['poster_path'])
            # print ("movie id is:" + str(i['id']))
            id = str(i['id'])
            path = i['poster_path']
            movie_details.posterpath = i['poster_path']

            video_url = urllib2.urlopen("https://api.themoviedb.org/3/movie/"+id+"/videos?api_key=bbb3d12e8c29321d17cd591a3fdacc49&language=en-US")
            json_obj1 = json.load(video_url)
            # print(json_obj1)
            for i in json_obj1['results']:
                key = i['key']
                key1 = key[0:]
                print (key1)
            # print ("youtube key is:"+key)
            movie_details.youtubekey = key1
            movie_details.movienames = movie.name

            moviesval = {movie.name: [key,path] }
            print ("info is"+str(moviesval))


# movies=dict([('Me+Before+You',2016)])
#
#
# for key, value in movies.iteritems():
#
#         url="/3/search/movie?api_key=bbb3d12e8c29321d17cd591a3fdacc49&query="+str(key)+"&year="+str(value)
#         print(url)
#         response = urllib2.urlopen("https://api.themoviedb.org/3/search/movie?api_key=bbb3d12e8c29321d17cd591a3fdacc49&query="+str(key)+"&year="+str(value))
#
#         json_obj = json.load(response)
#         print(json_obj)
#         for i in json_obj['results']:
#             print ("poster path is:"+i['poster_path'])
#             print ("movie id is:" + str(i['id']))




# for key, value in movies.iteritems():
#     # i=0
#     # while(i<=len(movies)):
#         url="/3/search/movie?api_key=bbb3d12e8c29321d17cd591a3fdacc49&query="+str(key)+"&year="+str(value)
#         print(url)
#
#         # conn.request("GET", "/3/movie/296096/images?language=en-US&api_key=bbb3d12e8c29321d17cd591a3fdacc49", payload)
#         conn.request("GET", "/3/search/movie?api_key=bbb3d12e8c29321d17cd591a3fdacc49&query="+str(movies.keys())+"&year="+str(movies.values()), payload)
#
#         res = conn.getresponse()
#         # data = res.read()
#
#         # print(data.decode("utf-8"))
#
#         json_obj = json.load(res)
#         print(json_obj)
#         for i in json_obj['results']:
#             print ("poster path is:"+i['poster_path'])
#             print ("movie id is:" + str(i['id']))
#         # i+=1
#
#