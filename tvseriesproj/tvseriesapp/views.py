
from django.template import loader
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from datetime import datetime
from tvseriesapp import fetch
from .models import Video
import json

def index(request):
    assert isinstance(request, HttpRequest)
    data = fetch.fetch.fetchTvshowInfo()
    seasonNums = data[0]
    seasonNames = data[1]
    seasonPosters = data[2]
    epiNumb = data[3]
    seasNumb = data[4]
    tvName = data[5]
    tagLine = data[6]
    voted = data[7]
    genreId = data[8]
    genreName = data[9]
    castData = fetch.fetch.fetchGetCast()
    charNames = castData[0]
    profilePics = castData[1]
    actorIds = castData[2]
    videoData = fetch.fetch.fetchGetVideos()
    id = videoData[0]
    myVidName = videoData[1]
    myVideos = videoData[2]
    return render(request, 'pages/index.html', {
        'title': 'DjangoProj-Home Page',
        'show_name': 'The Good Doctor',
        'seasonDetails': zip(seasonNums,seasonNames,seasonPosters),
        'castInfo': zip(charNames,profilePics,actorIds),
        'EpisNum': epiNumb,
        'SeasNum': seasNumb,
        'TvName': tvName,
        'TagLine': tagLine,
        'Voted': voted,
        'genresDetail': zip(genreId,genreName),
        'id': id,
        'MyVidName': myVidName,
        'MyVideo': myVideos,
        #'Vid': vid
    })

def episodes(request,seasonNumber):
    assert isinstance(request,HttpRequest)
    data = fetch.fetch.fetchEpisodes(seasonNumber)
    names = data[0]
    airDates = data[1]
    episNumbers = data[2]
    posters = data[3]
    overviews = data[4]
    ids = data[5]
    votedEp = data[6]
    return render(request, 'pages/episodes.html',{
        'title': 'Episodes',
        'showName': 'The Good Doctor',
        'Episodes': zip(names,airDates,episNumbers,posters,overviews,ids,votedEp),
        'SeasonNumb': seasonNumber,
    })
    
def episDetails(request,seasonNumber,epNum):
    print(seasonNumber+"="+epNum)
    assert isinstance(request,HttpRequest)
    data = fetch.fetch.fetchEpisDetails(seasonNumber,epNum)
    episName = data[0]
    overview = data[1]
    voted = data[2]
    stillPath = data[3]
    airDate = data[4]
    profImg = data[5]
    workerNam = data[6]
    jobs = data[7]
    guestName = data[8]
    guestChar = data[9]
    age = data[10]
    popularity = data[11]
    profPaths = data[12]
    return render(request, 'pages/details.html',{
        'title': 'Episode Details',
        'showName': 'The Good Doctor',
        'Production': zip(profImg,workerNam,jobs,guestName,guestChar,age,popularity,profPaths),
        'SeasonNum': seasonNumber,
        'EpisNum': epNum,
        'EpisName': episName,
        'Overview': overview,
        'Voted': voted,
        'StillPath': stillPath,
        'AirDate': airDate,
        
        #'details': zip(names,airDates,episNumbers,posters,overviews,ids),
    
    })
    
def actors(request):
    return render(request, 'pages/actors.html')
    
def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')



