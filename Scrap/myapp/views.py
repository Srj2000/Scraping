from abc import abstractstaticmethod
from django.shortcuts import render
from django.http import HttpResponse
import time
import requests
from bs4 import BeautifulSoup
from .models import NRI
def scrapdata():
        
        url='https://news.google.com/search?q=nri&hl=en-IN&gl=IN&ceid=IN%3Aen'

        resp=requests.get(url)
    
        soup=BeautifulSoup(resp.content, 'html.parser')
        product=soup.find('main', attrs={'class':"HKt8rc CGNRMc"})
        article=product.find_all('div', attrs={'class':'NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc'})
        for i in article:
            detail=i.find('a', attrs={'class':'DY5T1d RZIKme'})
            print(detail)
            details=detail.string
            des=detail.get('href')
            print(des)
            publish=i.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'}).string
            print(publish)
            image=i.find('img', attrs={'class':'tvs3Id QwxBBf'})
            imglink=image.get('srcset')
            print(image.get('srcset'))
            nri=NRI(details=details, des=des, publish=str(publish), image=imglink, posttime=time.time())
            nri.save()

def timeduration():
    obj=NRI.objects.all()
    if  len(obj)==0  :
        scrapdata()
        
        
    else:
        ctime=time.time()
    
        post_time=ctime-obj[0].posttime
        print(post_time)
        if post_time>=3600:
            
            obj.delete()
            scrapdata()



def scraping(request):
    
    timeduration()
    
    # ctime=time.time()
    
    # left_time=obj[0].posttime-ctime
    

  


        
    return render(request, 'scrap/index.html')

def news(request):
    obj=NRI.objects.all()
    timeduration()
    
    return render(request, 'scrap/news.html',{'obj':obj} )
    
    
# Create your views here.
