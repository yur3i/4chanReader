from fourchan import *
import sys


helpmsg = "Welcome to yur3i\'s 4chan reader!\n\nUSAGE: -t/i <board> <thread>\n-t get all text posts form thread\n-i get all images from the thread and dump them in the current directory"

if len(sys.argv) == 1:
    print(helpmsg)
    quit()
if sys.argv[1] in ["-h"]:
    print(helpmsg)
if sys.argv[1] in ["-t"]:
    getThread(sys.argv[2], sys.argv[3])
if sys.argv[1] in ["-i"]:
    getImages(sys.argv[2], sys.argv[3])

