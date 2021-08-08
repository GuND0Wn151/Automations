import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import PIL.Image as Image
a_set = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
name=input('Enter the Name: ')
content=requests.get("https://www.pokemon.com/us/pokedex/"+name).text
soup= BeautifulSoup(content,'lxml')
soup2=BeautifulSoup(content,'lxml')

def changeImage(image):
      width,height=image.size
      n_height=int((height/width)*50)
      re_image=image.resize((50,n_height))


      #grayscaleing here
      re_image=re_image.convert("L")


      #converting here
      data=list(re_image.getdata())
      char=''.join(a_set[i//25] for i in data)
      return char

try:
      data=soup.find_all('div',{'class':'profile-images'})
      x=[]
      for i in data[0]:
            
            if i!='\n':
                  x.append(i)
                  break
      url=str(x[0]).split('"')[-2]
      image=Image.open(urlopen(url))
      print(url)
      image_data=changeImage(image)
      a_image='\n'.join(image_data[i:(i+50)] for i in range(0,len(image_data),50))
      print(a_image)
      
      #######################################
      #this part is for finding the weekness
      #######################################
      data=soup2.find_all('div',{"class":"dtm-weaknesses"})
      clean_data=data[0].text.split(' ')
      weekness=[]
      #print(clean_data)


      #this are if for cleaning the unneccasary data
      for i in clean_data:
            if i!='' and i!='\n':
                  weekness+=i
      t=''
      for i in weekness:
            if i.isalpha():
                  t+=i
            else:
                  if t!='':
                        weekness.append(t)
                        t=''


      #print(weekness[::-1][:10])
      #this will be the final weekness types
      final_weekness=[] 
      for i in weekness:
            if len(i)>2 and i!='Weaknesses':
                  final_weekness.append(i)
      print("The Weekness types of "+name+" are: ")
      for i in range(len(final_weekness)):
            print(i+1,". ",final_weekness[i])
      
except:
      print("Some Error Has Occured \nCheck for spelling")
