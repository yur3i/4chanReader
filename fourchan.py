import re
import requests
from random import randint
import html
from os import system as bash

def cleanhtml(content):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    cleantext = html.unescape(cleantext)
    return cleantext
    
# gets all the posts in the thread
def getThread(board, threadno):
    r = requests.get("http://a.4cdn.org/"+board+"/thread/"+threadno+".json")
    threadjson = r.json()
    threadreplies = threadjson["posts"][0]["replies"]
    i = 0
    for i in range(0, threadreplies+1):
        postnum = threadjson["posts"][i]["no"]
        postcontent = str(threadjson["posts"][i]["com"])
        parsedContent = cleanhtml(postcontent)
        print("\n>"+str(postnum)+"\n"+str(parsedContent)+"\n")

        #gets all the images in a thread
def getImages(board, threadno):
    r = requests.get("http://a.4cdn.org/"+board+"/thread/"+threadno+".json")
    threadjson = r.json()
    threadreplies = threadjson["posts"][0]["replies"]
    filestoget = [ ]
    for post in threadjson["posts"]:
        if "tim" in post:
            filestoget.append(str(post["tim"])+post["ext"])
                    
    for image in filestoget:
        url = "http://i.4cdn.org/"+board+"/"+image
        bash("wget "+url)
#gets a random image from a thread
def getRandomImage(board, threadno):
    r = requests.get("http://a.4cdn.org/"+board+"/thread/"+threadno+".json")
    threadjson = r.json()
    threadreplies = threadjson["posts"][0]["replies"]
    filename = " "
    while 1:
        i = randint(0, threadreplies)
        if "tim" in threadjson["posts"][i]:
            break
    filename = str((threadjson["posts"][i]["tim"]))
    fileext  = str((threadjson["posts"][i]["ext"]))
    fileurl  = "http://i.4cdn.org/"+board+"/"+filename+fileext
    bash("wget "+fileurl)


