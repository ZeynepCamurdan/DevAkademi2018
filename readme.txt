
Sizden ald���m t�m veriyi (all_data 3.json) excel format�na �evirdikten sonra istedi�im �zellikleri kullanarak, Ekim ay�nda reklamlardan elde edilecek g�nl�k b�t�enin
tahminlenmesi i�in machine learning algoritmas� ile prediction uygulamas� yazd�m. 

all_data dosyas�n� file1 ve file2 olmak �zere iki dosyaya ay�rd�m. file1 train dosyas� olup tahminleme i�in prediction mod�l�ne g�nderdi�im datalar� i�eriyor. (31.12.2017 - 30.09.2018)
file2, test dosyas� olup tahminleyece�im datalar� i�eriyor. (01.10.2018-17.10.2018) . Tahminledi�im datalar ile file2'deki datalar�n k�yaslamas�, tahminlemenin ger�ek de�erlere ne kadar 
yak�n oldu�unu ifade ediyor. 

Not: Linear regression algoritmas�n� kulland���m i�in string olan �zellikleri de numeric olarak ifade ettim. File1 ve File2 dosyalar�n� github'ta bulabilirsiniz. 




