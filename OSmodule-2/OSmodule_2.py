import datetime
import os
result=dir(os)#os modülü ile işletim sistemiyleilgili bilgileri öğrenebilirz,dosyalarla alakalı bazı işlemleri yapabiliriz.
result=os.name#işletim sisteminin ismi

#result=os.getcwd()#bu dasya hankında bilgi verir konumu gibi
#os.chdir('c:\\')#dosyanın oluşturulacağı konumu veriyoruz
#os.mkdir("newdirectory")#klasör oluşturur
#os.rename("newdirectory","yeniklasör")#newdirectory isimli klasörün ismini yeniklasör olarak değiştirir
#os.rmdir("newdirectory")#klasörü siler
#os.removedirs("yeniklasör/yeniklasör")#yeniklasördeki yeniklasör dosyasını sil

#os.makedirs("newdirectory/yeniklasör")#newdirectory klasörünün içine yeniklasör oluşturduk Not:başına C:\\ yazarsan C nin içindeki newdirectory nin içine oluşturacaktı

#listeleme
#result=os.listdir()#içindeki klasörleri listeler
#result=os.listdir('C:\\')#Cnin içindeki klasörleri listeler

#.py uzantılı dosyaları listeledik:
#for dosya in os.listdir():
#    if dosya.endswith(".py"):
#        print(dosya)

#result=os.stat("OSmodule-2")#dosyaya erişilme zamanını gibi bilgileri veriyor.
#result=result.st_size/1024

#result=datetime.datetime.fromtimestamp(result.st_ctime)#dosyanın oluşturulma tarihi
#result=datetime.datetime.fromtimestamp(result.st_atime)#son erişilme tarihi
#result=datetime.datetime.fromtimestamp(result.st_mtime)#değiştirilme tarihi


#os.system("notepad.exe")#bu kod çalıtırıldığında notdefteri açılır 


result=os.path.abspath("OSmodule-2.py")#doyanın adresini verir
result=os.path.dirname(os.path.abspath("OSmodule-2.py"))
result=os.path.exists("OSmodule-2.py")#Aranan konumda dosya var mı ( True-False değeri geri döner)
result=os.path.isdir("OSmodule-2.py")#Klasör mü(true false değeri geri döndürür)
result=os.path.join("C:\\","deneme","deneme1")#C de deneme klasöründeki deneme1

print(result)