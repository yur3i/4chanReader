import re
import requests

def cleanhtml(content):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    return cleantext
    

def getThread(board, threadno):
    r = requests.get("http://a.4cdn.org/"+board+"/thread/"+threadno+".json")
    threadjson = r.json()
    threadreplies=threadjson["posts"][0]["replies"]
    i = 0
    for i in range(0, threadreplies+1):
        postnum = threadjson["posts"][i]["no"]
        postcontent = str(threadjson["posts"][i]["com"])
        parsedContent = cleanhtml(postcontent)
        print("\n>"+str(postnum)+"\n"+str(parsedContent)+"\n")

def getImages(board, thread):
    print("kek, dis shit ain\'t supported yet nigga")

