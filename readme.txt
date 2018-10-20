
Sizden aldýðým tüm veriyi (all_data 3.json) excel formatýna çevirdikten sonra istediðim özellikleri kullanarak, Ekim ayýnda reklamlardan elde edilecek günlük bütçenin
tahminlenmesi için machine learning algoritmasý ile prediction uygulamasý yazdým. 

all_data dosyasýný file1 ve file2 olmak üzere iki dosyaya ayýrdým. file1 train dosyasý olup tahminleme için prediction modülüne gönderdiðim datalarý içeriyor. (31.12.2017 - 30.09.2018)
file2, test dosyasý olup tahminleyeceðim datalarý içeriyor. (01.10.2018-17.10.2018) . Tahminlediðim datalar ile file2'deki datalarýn kýyaslamasý, tahminlemenin gerçek deðerlere ne kadar 
yakýn olduðunu ifade ediyor. 

Not: Linear regression algoritmasýný kullandýðým için string olan özellikleri de numeric olarak ifade ettim. File1 ve File2 dosyalarýný github'ta bulabilirsiniz. 




