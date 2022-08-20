from glob import glob
from bs4 import BeautifulSoup
from PIL import Image
import os
import csv



imgDir = glob("../assets/images/people/*")
    
quotes = dict()
with open('../assets/text/sd.csv', mode='r') as inp:
    reader = csv.reader(inp)
    quotes = {rows[0]:rows[1] for rows in reader}

html = BeautifulSoup("<!--Autogenerated HTML--><div class='container card-deck' style='margin:auto;'></div>", 'html.parser')
for j in imgDir:
    print(j.split("_"))
    try:
        _,first, last, _ = j.split("_")
    except ValueError:
        first = "Person"
        last = ""
    flip = html.new_tag('div')
    flip['class'] = "flip-card"

    inner = html.new_tag('div')
    inner['class'] = "flip-card-inner"
        
    front = html.new_tag('div')
    front['class'] = "flip-card-front"
        
    img = html.new_tag('img')
    img['class'] = 's'
    img['src'] = j
    front.append(img)
        
    back = html.new_tag('div')
    back['class'] = "flip-card-back"
        
    name = html.new_tag("h1")
    name.append(first + " " + last)
        
    quote = html.new_tag("p")
    quote.append(quotes.get(first+"."+last, "Loves to write about themselves"))

    back.append(name)
    back.append(quote)
        
    inner.append(front)
    inner.append(back)
        
    flip.append(inner)
        
    html.find("div").append(flip)
    with open('../templates/' + 'teamcards.html', 'w') as f:
        f.write(str(html.prettify()))
