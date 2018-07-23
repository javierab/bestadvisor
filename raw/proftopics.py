#!/usr/bin/python

# get professors and their topics from csail website
# and write them into a file for future processing.

import requests
import functools
from sets import Set

names = []
research = []
alltopics = Set()

tableStart = "views-infinite-scroll-content-wrapper clearfix"
tableEnd = "research-result third-column views-row spacing-only"

name1 = "field field--name-title field--type-string field--label-hidden"
name2 = "</span>\n"

areas1 = "field field--name-field-summary field--type-string-long field--label-hidden field__item"
areas2 = "<div class=\"circle-crop person-image"

div = "</div>"
br = "<br />"
infoblock = "<div class=\"info-block\">"

#fetch content
req = requests.get("https://www.csail.mit.edu/people?person%5B0%5D=role%3A300" )
content = str(req.content)

#focus on the data table
cn = content[content.find(tableStart):content.find(tableEnd)]

#now iterate through it

while cn.find(name1) > 0 :

	#go to data section
	cn = cn[cn.find(infoblock):]

	#get name
	name = cn[cn.find(name1)+len(name1)+2 : cn.find(name2)]
	names.append(name)

	#get topics
	area = cn[cn.find(areas1)+len(areas1)+2 : cn.find(areas2)]
	area = area[0:area.find(div)].replace(br,'').replace("&amp;","and")
	research.append(area)

	#add to full list
	alltopics.update(list(map(lambda x : x.strip(' \t\n.').lower(), area.split(','))))

	#move forward
	cn = cn[cn.find(areas2)+len(areas2):]


#print the names and topics to files

tbp = open("topicsbyprof","w") 
at = open("alltopics","w")

for i in range(0,len(names)):
	tbp.write("('" + names[i] + "':" + research[i] + ")\n")

for topic in alltopics: 
	at.write(topic)

tbp.close()
at.close()