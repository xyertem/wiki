from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django import forms
import markdown2

from . import util

class editForm(forms.Form):#this is crerated a form with from class with multiple field
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea)
        
            
       
def newEntry(request):

    if request.method == 'POST':
        
        form = editForm(request.POST)

        if form.is_valid():

           title = form.cleaned_data["title"]

           content = form.cleaned_data["content"]

           util.save_entry(title,content)

           return HttpResponseRedirect(reverse("encyclopedia:index"))
   
        else:
            
            return render(request, "encyclopedia/newPage.html", {
            "form": form
            }) 
    
    return render(request, "encyclopedia/newPage.html", {
            "form": editForm()
            })  

def editpage(request):
    return None

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    try:
        return render(request,"encyclopedia/EntryPage.html",{# Here, I converted md file to html
            "page": markdown2.markdown(util.get_entry(title)),
            "entry_title": title #I got page title  with this variable that i used in entrypage.html to display title name of page.
    })
    except:
        return HttpResponseNotFound("Entry Does not exist")

   
  
      
        

    

    
     
