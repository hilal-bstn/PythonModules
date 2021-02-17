import requests
import json
api_url="https://api.exchangeratesapi.io/latest?base="
bozulan_doviz=input("Bozulan döviz türü: ")
alinan_doviz=input("Alınan döviz türü: ")
miktar=int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

result=requests.get(api_url+bozulan_doviz)
result=json.loads(result.text)
#print(result)#yukarıda websitenin döviz kısmını boş bıraktık ve kullanıcıdan istedik
#kullanıcı girdikten sonra websiteye ekledik
#daha sonrasında ise json modülünü kullanarak web sitedeki json bilgilerini sözlüğe çevirdik
#bu sözlük bilgilerinde {rates{USD="",TRY="",EUR=""...}} bu şekilde oluğundan websitedeki [rates] kısmının[alınan_doviz] kime karşılık geliyorsa onu getirttik
print("1 {0}={1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz],alinan_doviz))
print("{0} {1}={2} {3}".format(miktar,bozulan_doviz,miktar*result["rates"][alinan_doviz],alinan_doviz))