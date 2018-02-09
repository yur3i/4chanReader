import re
import requests
from random import randint
import html

def cleanhtml(content):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    cleantext = html.unescape(cleantext)
    return cleantext
    

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

def getImages(board, thread):
    print("not yet supported")

def getRandomImage(board, threadno):
    r = requests.get("http://a.4cdn.org/"+board+"/thread/"+threadno+".json")
    threadjson = r.json()
    threadreplies = threadjson["posts"][0]["replies"]
    print(threadreplies)
    i = randint(0, threadreplies)


        
