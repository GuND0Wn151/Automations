import requests
from bs4 import BeautifulSoup

print("___________________________Welcome_____________________________")
product_name=input("Enter the product name Without spaces ")

content=requests.get("https://www.amazon.in/s?k="+product_name).text

soup=BeautifulSoup(content,'lxml')



list_product=[]
price_product=[]
try:
      for i in soup.find_all('div', { "class":"a-section a-spacing-none"}):
            t=i.text
            list_product.append(t)
      count1=0
      count2=0

      for i in soup.find_all('span',{'class':'a-offscreen'}):
            t=i.text
            price_product.append(t)    
      print(list_product)
      print(price_product)
      for i in soup.find_all('div',{'class':"a-section a-spacing-none"}):
           print(i.h2.a)
      print(list_product)
      print(price_product)

      print("-----------------------------products found-----------------------")
      for i in list_product:
            count1+=1
            print(i)
            if count1==6:
                  break
      print("-----------------------------prices found-------------------------")
      for i in price_product:
            count2+=1
            print(i)
            if count2==6:
                  break

      print("--------------------------------listing---------------------------")
      print("Item\t\tprice")
      for i in range(5):
            print(list_product[i],"\t\t",price_product[i])
except:
      print("Error Encountered try to relaucnh the code")
