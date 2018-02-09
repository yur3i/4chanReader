import requests

def getThread(board, threadno):
    r = requests.get("http://a.4cdn.org/"+board+"/thread/"+threadno+".json")
    threadjson = r.json()
    threadreplies=threadjson["posts"][0]["replies"]
    i = 0
    for i in range(0, threadreplies+1):
        postnum = threadjson["posts"][i]["no"]
        postcontent = threadjson["posts"][i]["com"]
        print("\n>"+str(postnum)+"\n"+postcontent+"\n")

def getImages(board, thread):
    print("kek, dis shit ain\'t supported yet nigga")
    
