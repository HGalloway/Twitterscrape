#!/bin/python3
import sys
import requests
from bs4 import BeautifulSoup

print ("You are currently running %s" % (sys.argv[0]))

if len(sys.argv) < 2:
    print("You should supply the name of a html file to extract the text from")
    sys.exit()
else:
    text = open(sys.argv[1], "r")

print("Reading in %s " % str(sys.argv[1]))

soup = BeautifulSoup(text, 'html.parser')
tweets = [p.text for p in soup.findAll('p')]
txt = ' '.join(tweets)

for t in tweets:
    print(t)

with open('output.txt', 'w') as f:
    for t in tweets:
        f.write(t + "\n")
