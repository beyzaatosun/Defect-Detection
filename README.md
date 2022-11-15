# Defect-Detection
:triangular_flag_on_post: Ürün kalitesinin izlenmesi; üretici firmalar açısından kritik, maliyeti belirleyen ve zaman alan bir süreçtir. Kişiye bağlı kalite kontrolü; düşük doğruluk, zaman kaybı, yüksek işgücü ve kaynak israfı gibi verimsizliklere neden olmaktadır.  Bununla birlikte, yüzey kusur tespiti, aydınlatma, ışık yansıması ve ürün malzemesi gibi birçok çevresel faktörden kolayca etkilenir. Bu faktörler, yüzey kusur tespitinin zorluğunu önemli ölçüde artırır. 

:pushpin: Bu çalışmada NEU veri setine ek olarak KolektorSDD, Magnetic-Tile ve BSData veri setleri kullanılacaktır. Kusur tespiti için metal yüzeylerdeki hatalara yönelik geliştirdiğimiz B2Net adlı algoritma görsel verilerden yararlanmaktadır. B2Net, veri çoğaltma adımında bir çekişmeli-üretici ağ ile çeşitli klasik yöntemleri sentezlerken ve yüzey kusurlarının yerini ve türünü tahmin eden çıktılar üretmektedir. Böylece üretim hatalarının otomatik tespiti için yapay zekanın kullanılması, üretim maliyetinin, hızının azaltılmasına olanak tanır. 

:book: Veri Setleri

1-NEU Veri Seti bu bağlantı kullanılarak indirilebilir.
Toplam 1800 adet 200x200 boyutunda gri tonlamalı görüntüden oluşmaktadır. Altı sınıf mevcuttur ve her sınıfta 300 örnek vardır. Sınıflar, haddelenmiş ölçek (rolled-in scale (RS)), yamalar (patches (Pa)), çatlama (crazing (Cr)), çukurlu yüzey (pitted surface (PS)), kalıntı (inclusion (In)) ve çizikler (scratches (Sc)) oluşmaktadır. 
![image](https://user-images.githubusercontent.com/48567287/201970817-8e6a6d0a-c96e-4a3f-85cf-6a2c102f7e86.png)

2-BSData Veri Seti bu bağlantı kullanılarak indirilebilir.
Bu sınıf çukurlaşma (pitting) hataları içermektedir. Toplamda 1104 RGB görüntü ve 394 açıklamalı (annotation) RGB görüntü içermektedir.  Açıklama aracı etiketiyle yapılan açıklamalar JSON formatında mevcuttur. 

3-Magnetic Tile Veri Seti bu bağlantı kullanılarak indirilebilir.
Magnetic Tile veri seti beş kusur sınıf türünden oluşmaktadır. Bu sınıflar hava deliği (blowhole), çatlak (crack), kırılma (break), yıpranma (fray) ve düzensiz (uneven) hataları içermektedir. Hava deliği (blowhole) 115 görüntü, çatlak (crack) 85 görüntü, kırılma (break) 57 görüntü, yıpranma (fray) 32 görüntü ve düzensiz (uneven) 103 görüntü içermektedir. Toplamda 392 görüntü ve 392 açıklamalı (annotation) görüntü içermektedir. 

4-DAGM 2007 Veri Seti bu bağlantı kullanılarak indirilebilir.
DAGM2007 veri kümesi, her biri bir kusur sınıfına karşılık gelen 10 alt kümeden oluşmaktadır. Her sınıf, 512×512 boyutunda doku arka planlarında bir kusurlu 1000 hatasız görüntü ve 150 hatalı görüntüye sahiptir.


