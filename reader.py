from fourchan import *
import sys
from os import system as bash

helpmsg = "Welcome to yur3i\'s 4chan reader!\n\nUSAGE: -t/i <board> <thread>\n-t get all text posts form thread\n-i get all images from the thread and dump them in the current directory\n-ri get a random image from the thread and display it. [only supported on certain terminal emulators]"

if len(sys.argv) == 1:
    print(helpmsg)
    quit()
if sys.argv[1] in ["-h"]:
    print(helpmsg)
if sys.argv[1] in ["-t"]:
    getThread(sys.argv[2], sys.argv[3])
if sys.argv[1] in ["-i"]:
    getImages(sys.argv[2], sys.argv[3])
if sys.argv[1] in ["-ri"]:
    fileext = getRandomImage(sys.argv[2], sys.argv[3])
    bash("./imgrender.sh /tmp/img"+fileext)
if sys.argv[1] in ["-r"]:
    completelyRandom(sys.argv[2])
