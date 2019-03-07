# Original Author: Mark Leyva, 2019
#
# This scripts pulls the latest Weekly Shounen Jump Rankings
# from https://weeklyjump.livejournal.com/ and saves them in
# a CSV file

import requests
from bs4 import BeautifulSoup
import re
import csv
import datetime

page = requests.get("https://weeklyjump.livejournal.com/")

soup = BeautifulSoup(page.content,'html.parser')

# Get just the entries
entry_text = soup.find_all('div',class_='entry_text')

# Get the latest WSJ rankings
text = entry_text[0].find_all(text=True)
# Remove the last 13 indexes since this are not related to the rankings
text = text[1:len(text)-13]
# Remove all series with a Cover Page, CP, New Series, or Absent
text = [i for i in text if not re.search("Cover|Lead CP|New Series|CP|Absent",i)]

# Add the proper ranking
rankings = list(enumerate(text,start=1))
rankings.insert(0,("Ranking","Title"))

filename = "./Latest_WSJ_Rankings_{:%Y%m%dT%H%M%S}.csv".format(datetime.datetime.now())
     
with open(filename, 'w', encoding='utf-8', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
     wr.writerows(rankings)