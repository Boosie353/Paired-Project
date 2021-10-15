from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import FashionContent, CelebrityContent, FinanceContent, PoliticsContent, SportsContent, ReceipesContent
from .apps import AppConfig

import feedparser


# Create your views here.
def updatefashion(request):
    #-------python----------------
    url = feedparser.parse(
            "https://www.zando.co.za/blog/"
        )
    for i in range(10):
        info = url.entries[i]
        content= FashionContent()
        content.headline= info.title
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)
 
        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')
 
def updatecelebrity(request):
    #-------python----------------
    url = feedparser.parse(
            "https://www.celebgossip.co.za/"
        )
    for i in range(10):
        info = url.entries[i]
        content= CelebrityContent()
        content.headline= info.title
        print("################################")
        print(content.headline)
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)
 
        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')
 
def updatefinance(request):
    #-------python----------------
    url = feedparser.parse(
            "https://www.news24.com/fin24"
        )
    for i in range(10):
        info = url.entries[i]
        content= FinanceContent()
        content.headline= info.title
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)
 
        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')
 
def updatepolitics(request):
    #-------python----------------
    url = feedparser.parse(
            "https://theconversation.com/africa/topics/south-african-politics-8463"
        )
    for i in range(10):
        info = url.entries[i]
        content= PoliticsContent()
        content.headline= info.title
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)
 
        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')

def updatesports(request):
    #-------python----------------
    url = feedparser.parse(
            "https://www.thesouthafrican.com/sport/"
        )
    for i in range(10):
        info = url.entries[i]
        content= SportsContent()
        content.headline= info.title
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)
 
        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')


def updatereceipes(request):
    #-------python----------------
    url = feedparser.parse(
            "https://www.whatsfordinner.co.za/"
        )
    for i in range(10):
        info = url.entries[i]
        content= ReceipesContent()
        content.headline= info.title
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)
 
        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')
 
def home(request):
    fashioncontent = FashionContent.objects.all()
    celebritycontent = CelebrityContent.objects.all()
    financecontent = FinanceContent.objects.all()
    politicscontent = PoliticsContent.objects.all()
    sportscontent = SportsContent.objects.all()
    receipescontent = ReceipesContent.objects.all()
    context = { 
        'fashioncontent': fashioncontent,
        'celebritycontent': celebritycontent,
        'financecontent': financecontent,
        'politicscontent': politicscontent,
        'sportscontent': sportscontent,
        'receipescontent': receipescontent
    }
    return render(request,'app/home.html',context)