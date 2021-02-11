from django.shortcuts import render
import markdown2
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    return render(request,"encyclopedia/EntryPage.html",{# Here, I converted md file to html
        "entries": markdown2.markdown(util.get_entry(title)),
        "entry_title": title #I got page title by user with this variable that i used in entrypage.html to display title name of page.
    })

"""
def search_bar(request, title):
    
    ent_name = util.list_entries()
    list_ent = []
    for name in range(len(ent_name)):
        list_ent.append(ent_name[name])
        if title == list_ent[name]:
            return render(request,"encyclopedia/EntryPage.html",{
                "entries": util.get_entry(title),
                "entry_title": title 
                })
        else:
            return render(request,"encyclopedia/index.html")       
"""
    

    
     
