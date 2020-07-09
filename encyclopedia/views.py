from django.shortcuts import render
from django.http import HttpResponse

from . import util
import datetime
from datetime import datetime


import markdown2
from markdown2 import Markdown

import os, random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request,page):
    try:

        mdcontents, mybool = util.get_entry(page)
        markdowner = Markdown()
        htmlcontents = markdowner.convert(mdcontents)
     
        return render(request,"encyclopedia/entrypage.html",{
            "title":page,
            "htmlcontent" : htmlcontents
        })
    except TypeError:
        return render(request,"encyclopedia/errorpage.html")


def mysearch(request):
    
    results = []
    query_searched = request.POST['q']
    entries = util.list_entries()
    
    for entry in entries:
        if(entry.find(query_searched)==-1):
            pass
        else:
            results.append(entry)


    return render(request,"encyclopedia/search_results.html",{
              "results" : results
             
        })
   


def new(request):
    return render(request,"encyclopedia/newpage.html")


def saveentry(request):
    if request.method == 'POST':
        title = request.POST['title']
        textarea = request.POST['textarea']
        x, mybool = util.get_entry(title)
            
        if(mybool):
            return HttpResponse('oops the entry already exists!')
            
        else:
            f = open(f'/home/pravallika/Desktop/wiki/entries/{title}.md','w+')
            f.write(textarea)
            f.close()   
            markdowner = Markdown()
            htmlcontents = markdowner.convert(textarea)
            return HttpResponse(htmlcontents) 

def randompage(request):
    filename = random.choice(os.listdir("/home/pravallika/Desktop/wiki/entries"))
    print(filename)
    title = os.path.splitext(filename)[0] 

    mdcontents, mybool = util.get_entry(title)
    markdowner = Markdown()
    htmlcontents = markdowner.convert(mdcontents)
    
    return render(request,"encyclopedia/entrypage.html",{
    "title":title,
    "htmlcontent" : htmlcontents
    })
    
def editpage(request, title):

    mdcontents, mybool = util.get_entry(title)
    markdowner = Markdown()
    htmlcontents = markdowner.convert(mdcontents)
    

    return render(request, "encyclopedia/editpage.html",{
        "title" : title,
        "mdcontent" : mdcontents
    })
    

def resave(request):
    title = request.POST['title']
    textarea = request.POST['textarea']
    f = open(f'/home/pravallika/Desktop/wiki/entries/{title}.md','w+')
    f.write(textarea)
    f.close()   
    markdowner = Markdown()
    htmlcontents = markdowner.convert(textarea)
    
    return render(request, "encyclopedia/entrypage.html",{
        "title" : title,
        "htmlcontent" : htmlcontents
    })
    



