#regular expression
import re
result=dir(re)

str="Python Kursu : Python Programla rehberi | 40 Saat"
result=re.findall("Python",str)#bulduğu "Python" yazılarını liste haline getirir
result=len(result)#kaç tane python yazısı var(listenin uzunluğu)
result=re.split(" ",str)#boşlukları atarak kelimeleri liste şekline getirir.

result=re.sub(" ","-",str)#boşluları - ile değiştir. Boşluk yerine \s de yazılabilir.
result=re.search("Python",str)#kaçıncı karakterler arasında pyhon yazısı var (Çıkıtısı:(0,6) gibi olur)

result=re.findall("[abc]",str)#bulduğu a b c karakterlerini liste haline getirir. []içine yazılan herbir karakteri ayrı ayrı arar
result=re.findall("[a-e]",str)#a dan e ye kadar olan karketleri varsa listeler[a,e,a,]..gibi
result=re.findall("[0-4]",str)#ile 4 arasındaki karakterleri arar

result=re.findall("[^abc]",str)#abc dışındaki karakterler
#not: [0-39]=>[01239]şelinde bir arama gerçeklerştirir
result=re.findall("[^0-9]",str)

result=re.findall("...",str)#3 karakter olarak algılar 3 lü karakterlere böler ve listeler
result=re.findall("Py..on",str)

result=re.findall("^P",str)#p ile başlıyorsa çıktısı:['P']
result=re.findall("t$",str)#t ile bitiyormu

result=re.findall("sa*t",str)#a dan 0 yada daha fazla olabilir saat kelimesi gibi
result=re.findall("sa+t",str)#a 1 den daha fazla olmasını sorgular
result=re.findall("sa?t",str)#sadece 0 yada bir karakter olmasını sorgular

result=re.findall("a{2}",str)#a dan 2 tane olanları getir
result=re.findall("[0-9]{2}",str)#2 basamaklı sayıyı ararken

result=re.findall("a|b",str)#a yada b
result=re.findall("(a|b|)xz",str)#a yada b yada c nin arkasında xz karakterleri gelmelidir

result=re.findall("\$a",str)#$karakterinin arkasında a yı arar
result=re.findall("\APython",str)#str ifadesi Python ile mi başlıyor
result=re.findall("saat\Z",str)#saat ile mi bitiyor

print(result)