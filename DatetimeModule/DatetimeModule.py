from datetime import datetime
from datetime import timedelta
#from datetime import date
#from datetime import time
#import datetime
simdi=datetime.now()#güncel bilgiler gelir
result=simdi.year#yıl bilgisi 
result=simdi.month#ay bilgisi
result=simdi.day#gün bilgisi
result=simdi.hour#saat bilgisi
result=simdi.minute#dakika bilgisi
result=simdi.second#saniye bilsi

bugun=datetime.today#bugünün bilgileri(yıl/ay/gün/saat)
result=datetime.ctime(simdi)#f

result=datetime.strftime(simdi,'%Y')#şu anın yıl bilgisi
result=datetime.strftime(simdi,'%X')#şu anın bilgisini verir
result=datetime.strftime(simdi,'%d')#şuanın gün bilgisini verir
result=datetime.strftime(simdi,'%Y %B %A')#yıl ay gün

#t='21 Nisan 2019'
#gun,ay,yil=t.split()#boşluklardan ayır
#print(gun)
#print(ay)
#print(yil)

t='15 April 2019 hour 10:12:30'
dt=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
result=dt.year
print(dt)

birthday=datetime(1983,5,9,12,30,10)#yıl ay gün saat dakika saniye 

result=datetime.timestamp(birthday)#saniye bilgisini verir
result=datetime.fromtimestamp(result)#saniye bilgisini datetime a çevirdik(gün ay yıl saat dakika)
result=datetime.fromtimestamp(0)#1970 bilgisini verir
result=simdi-birthday#gün ay yıl saat farkı
result=simdi+timedelta(days=10)#timedelta kullanarak simdinin üzerine 10 gün eklenmiş olur
result=simdi+timedelta(days=730,minutes=30)#730 gün ve 30 dakika ekledik
print(result)
#print(result)
#datetime python(modül içindeki fonksiyonlara bakabilirsin)
