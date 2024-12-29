
# Multi-Layer Perceptron (Çok Katmanlı Algılayıcı - MLP)
MLP, birden fazla katmandan oluşan ileri beslemeli bir yapay sinir ağı modelidir. 
Bu Ağı giriş verilerini sadece ileri yönde işleyen sinir ağlarıdır. 
Bu ağlar, bir giriş katmanı, bir veya birkaç gizli katman ve bir çıkış katmanından oluşur. 
Veriler, girişten çıkışa doğru akarken, her katmanda ağırlıklar ve aktivasyon fonksiyonları kullanılarak 
işlenir.


## MLP'nin Çalışma Prensibi
MLP modeli, giriş verilerini alarak her bir girdi ile ağırlıkları çarpar ve bias ekler. Gizli katmandaki nöronlar, aktivasyon fonksiyonu kullanarak çıktıyı hesaplar ve bu işlem çıktı katmanına kadar devam eder. Çıktı katmanında, nöronlar sinyalleri birleştirerek son sınıflandırma sonucunu verir. Hesaplanan hata, gerçek etiketlerle karşılaştırılır ve hata fonksiyonu kullanılarak belirlenir. Geri yayılım algoritması, ağırlıkları hata fonksiyonunun türevlerini hesaplayarak günceller ve bu süreç model eğitimine kadar devam eder.
Detaylı bilgi için `>>>` [Yapay Sinir Ağları](../README.md)

