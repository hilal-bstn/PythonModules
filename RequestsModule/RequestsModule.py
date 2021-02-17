import requests#html,json gibi bilgileri çekebiliyoruz 
import json
result=requests.get("https://jsonplaceholder.typicode.com/todos")
#result=result.text
#print(result)#html kodlarını yazdırdık

result=json.loads(result.text)#sözlük tipine çevirdik
for i in result:
    if i["userId"]==1:
          print(i["title"])#title olanları yazdırdık

print(type(result))#string tipi olarak çıkar
