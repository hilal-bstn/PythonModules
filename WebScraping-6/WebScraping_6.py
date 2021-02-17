import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

#response=requests.get(url)
#content=response.content#yukarıdaki url kodunu contente attık

html=requests.get(url).content#sayfanın html kodları
soup=BeautifulSoup(html,"html.parser")#html kodlarımızı düzenledik

list=soup.find('tbody',{"class":"lister-list"}).find_all("tr",limit=50)#limit ile kaç tane tane tr etiketi getireceğimizi belirtiyoruz
count=1
for tr in list:
    title=tr.find('td',{"class":"titleColumn"}).find("a").text#tr etiketi
    year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating=tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text  
   
    print(f"{count}- film: {title} yıl: {year} değerlendirme: {rating}")
    count+=1