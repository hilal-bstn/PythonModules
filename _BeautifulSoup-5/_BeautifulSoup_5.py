html_doc='''
<!DOCTYPE html>
<html lang="en">
<head>(otomatik)()
<meta charset="UTF-8">
<meta name=viewport content="with=device-width,initial-source=>

     <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title>Başlık bilgisi yer alır</title>
</head>     
<body>
   
<h1>
          Python Kursu(Sayfaya başlık koyduk)(Ana başlıklar h1 ile)
   </h1>
   <div class="grup1">
      <h2>
          Alt başlık
      </h2>
      <ul>
          <li>Menü 1 </li>
          <li>Menü 2 </li>
      </ul>
   </div>
   <img src="fred.jpg" alt="">
   <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
   <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
   <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>
</body>
</html>
'''
from bs4 import BeautifulSoup

soup=BeautifulSoup(html_doc,'html.parser')
result=soup.prettify()#string olarak verdiğimiz html kodunu düzenler bu kod
result=soup.title#title etiketi içindeki html kodalarını getirir
result=soup.head#head etiketi altındaki html kodlarını bize verir
result=soup.title.name#sadece etiket ismi gelir title
result=soup.title.string#title etiketindeki string ifade gelir

result=soup.h2#sadece ilk h2 etiketi bilgilerini getirir
result=soup.find_all('h2')#bütün h2 etiketleri gelir

#result=soup.find_all('div')[1].ul.find_all('li')#1. divin altındaki li etiketini getir

#result=soup.div.findChildreen()#her etiket altındaki childreen etiket, aynı hizada blunan etiketler siblings 

#result=soup.div.findNextSibling().findNextSiblig()
result=soup.find_all('a')#a etiketi
for link in result:
    print(link.get('href'))
print(result)