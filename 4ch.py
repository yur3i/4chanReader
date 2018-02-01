#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup as bsoup

helpmsg = "Welcome to yur3i\'s 4chan reader, this help message was displayed because you passed no arguments\nUSAGE: 4ch.py -t/-i <board> <thread>\n-t get all posts in a thread as text.\n-i download all the images from a thread."

def getimages(board, thread):
    print("getting images from www.4chan.org/"+board+"/thread/"+thread+"...")
    r = requests.get("http://www.4chan.org/"+board+"/thread/"+thread)
    site = r.text
    soup = bsoup(site, "html5lib")
    print(site)

def getPosts(board, thread):
    print("getting posts from www.4chan.org/"+board+"/thread/"+thread+"...")
#if no arguments were passed, display the help message
if len(sys.argv) == 1:
    print(helpmsg)
    quit()
if str(sys.argv[1]) in ["-h"]:
    print(helpmsg)
if str(sys.argv[1]) in ["-i"]:
    getimages(board=str(sys.argv[2]),thread = str(sys.argv[3]))
if str(sys.argv[1]) in ["-t"]:
    getPosts(board=str(sys.argv[2]),thread= str(sys.argv[3]))
