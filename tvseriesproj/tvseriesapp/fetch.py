
from django.http import HttpRequest
import requests
import json

class fetch():
    
    def fetchTvshowInfo():
        #https://api.themoviedb.org/3/tv/71712?api_key=b5a5beafd36eebba20564e5ee6a1fbf1
        fullData = []
        seasonNums = []
        seasonNam = []
        posters = []
        genresId = []
        genresName = []
        showId = '71712'
        apiKey = "b5a5beafd36eebba20564e5ee6a1fbf1"
        url = "https://api.themoviedb.org/3/tv/"+showId+"?api_key="+apiKey
        response  = requests.get(url)
        if(response.ok):
            JData = json.loads(response.content)
            numOfEpisodes = JData['number_of_episodes']
            numOfSeasons = JData['number_of_seasons']
            tvName = JData['name']
            tagline = JData['tagline']
            voted = JData['vote_average']
            data = JData['seasons']
            for i in range(len(data)):
                seasonNums.append(data[i]['season_number'])
                seasonNam.append(data[i]['name'])
                posters.append(data[i]['poster_path'])
            data = JData['genres']
            for i in range(len(data)):
                genresId.append(data[i]['id'])
                genresName.append(data[i]['name'])
            fullData.append(seasonNums)
            fullData.append(seasonNam)
            fullData.append(posters) 
            fullData.append(numOfEpisodes)
            fullData.append(numOfSeasons) 
            fullData.append(tvName)  
            fullData.append(tagline)
            fullData.append(voted)
            fullData.append(genresId)
            fullData.append(genresName)
        else:
            JData = None
        return fullData
    
    def fetchEpisodes(seasonNum):
        #https://api.themoviedb.org/3/tv/71712/season/1?api_key=b5a5beafd36eebba20564e5ee6a1fbf1
        fullData = []
        names = []
        airDates = []
        episNumbers = []
        posters = []
        overviews = []
        ids = []
        votedEpis = []
        showId = '71712'
        apiKey = "b5a5beafd36eebba20564e5ee6a1fbf1"
        url = "https://api.themoviedb.org/3/tv/"+showId+"/season/"+seasonNum+"?api_key="+apiKey
        response  = requests.get(url) 
        if(response.ok):
            JData = json.loads(response.content)
            data = JData['episodes']
            for i in range(len(data)):
                names.append(data[i]['name'])
                airDates.append(data[i]['air_date'])
                episNumbers.append(data[i]['episode_number'])
                posters.append(data[i]['still_path'])
                overviews.append(data[i]['overview'])
                ids.append(data[i]['id'])
                votedEpis.append(data[i]['vote_average'])
            fullData.append(names)
            fullData.append(airDates)
            fullData.append(episNumbers) 
            fullData.append(posters) 
            fullData.append(overviews)
            fullData.append(ids)
            fullData.append(votedEpis)
        else:
            JData = None
        return fullData

    def fetchEpisDetails(seasonNum,episNumber):
        print(seasonNum+"--"+episNumber)
        #https://api.themoviedb.org/3/tv/71712/season/4/episode/1?api_key=b5a5beafd36eebba20564e5ee6a1fbf1
        fullData = []
        profileImgs = []
        workerNames = []
        jobs = []
        guestName = []
        guestChar = []
        age = []
        popularity = []
        profPaths = []
        #----------------------------------------
        showId = '71712'
        apiKey = "b5a5beafd36eebba20564e5ee6a1fbf1"
        url = "https://api.themoviedb.org/3/tv/"+showId+"/season/"+seasonNum+"/episode/"+episNumber+"?api_key="+apiKey
        response  = requests.get(url)
        if(response.ok):
            JData = json.loads(response.content)
            epNames = JData['name']
            overview = JData['overview']
            vote = JData['vote_average']
            stillPath = JData['still_path']
            airDate = JData['air_date']
            crew = JData['crew']
            for i in range(len(crew)):
                profileImgs.append(crew[i]['profile_path'])
                workerNames.append(crew[i]['name'])
                jobs.append(crew[i]['job'])
            data = JData['guest_stars']
            for i in range(len(data)):
                guestName.append(data[i]['name'])
                guestChar.append(data[i]['character'])
                age.append(data[i]['order'])
                popularity.append(data[i]['popularity'])
                profPaths.append(data[i]['profile_path'])
            fullData.append(epNames)
            fullData.append(overview)
            fullData.append(vote)
            fullData.append(stillPath)
            fullData.append(airDate)
            fullData.append(profileImgs)
            fullData.append(workerNames)
            fullData.append(jobs)
            fullData.append(guestName)
            fullData.append(guestChar)
            fullData.append(age)
            fullData.append(popularity)
            fullData.append(profPaths)
        else:
            JData = None
        return fullData

    def fetchGetCast():
        #https://api.themoviedb.org/3/tv/71712/credits?api_key=b5a5beafd36eebba20564e5ee6a1fbf1
        fullData = []
        charNames = []
        profilePics = []
        actorIds = []
        showId = '71712'
        apiKey = "b5a5beafd36eebba20564e5ee6a1fbf1"
        url = "https://api.themoviedb.org/3/tv/"+showId+"/credits?api_key="+apiKey
        response  = requests.get(url)
        if(response.ok):
            jData = json.loads(response.content)
            data = jData['cast']
            for i in range(len(data)):
                charNames.append(data[i]['character'])
                profilePics.append(data[i]['profile_path'])
                actorIds.append(data[i]['id'])
            fullData.append(charNames)
            fullData.append(profilePics)
            fullData.append(actorIds)
        else:
            jData = None
        return fullData
    
    def fetchGetVideos():
        #https://api.themoviedb.org/3/tv/71712/videos?api_key=b5a5beafd36eebba20564e5ee6a1fbf1
        fullData = []
        name = []
        videoKey = []
        showId = '71712'
        apiKey = "b5a5beafd36eebba20564e5ee6a1fbf1"
        url = "https://api.themoviedb.org/3/tv/"+showId+"/videos?api_key="+apiKey
        response  = requests.get(url)
        if(response.ok):
            JData = json.loads(response.content)
            id = JData['id']
            video = JData['results']
            name = video[0]['name']
            videoKey = video[0]['key']
            fullData.append(id)
            fullData.append(name)
            fullData.append(videoKey)
        else:
            JData = None
        return fullData
    
    
    