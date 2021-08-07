import requests
from bs4 import BeautifulSoup
Poke_name=input("Enter the name of pokemon: ")
content=requests.get("https://www.pokemon.com/us/pokedex/"+Poke_name).text
soup=BeautifulSoup(content,'lxml')

try:
      #getting data where with div and class=dtm-weeknesses
      data=soup.find_all('div',{"class":"dtm-weaknesses"})
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
      print("The Weekness types of "+Poke_name+" are: ")
      for i in range(len(final_weekness)):
            print(i+1,". ",final_weekness[i])


except:
      print("check the spelling of the pokemon")
