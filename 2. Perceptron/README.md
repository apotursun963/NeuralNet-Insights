
# Perceptron (Algılayıcı) Nedir ?
**Perceptron, En temel tek katmanlı [Yapay Sinir Ağı](../README.md) modelidir ve yalnızca tek bir nörondan oluşur. `Denetimli öğrenme algoritmasıdır.` Çıktısı 0 veya 1 olan bir lineer sınıflandırıcıdır ve ağırlıklar, hataya dayalı bir güncelleme kuralıyla güncellenir.**


## Temel Özellikler
- **Çıktısı**: 0 veya 1 (ikili sınıflandırma)
- **Temel Bileşenleri**:
    * Girdiler
    * Weight
    * Bias
    * Aktivasyon Fonksiyonu
- **İleri besleme ile çalışır (geri yayılım kullanmaz)** 
- **Ağırlıklar ve bias, hata düzeltme kuralına `(delta)` göre güncellenir.**

## Çalışma Prensibi
Perceptron'un çalışma prensibi, birkaç adımda özetlenebilir. İlk olarak, girdi özellikleri (inputs) alınır. Ardından, her bir girdi, ağırlıklar (weights) ile çarpılır. Çarpımların toplamı hesaplandıktan sonra, bias eklenir. Bu toplam değer, daha sonra aktivasyon fonksiyonuna sokulur. Aktivasyon fonksiyonu, toplam değeri alarak çıktıyı belirler. Sonuç olarak, perceptron, 0 veya 1 olan bir çıktı üretir.

## Perceptron’un Doğrusal (Lineer) ve Doğrusal Olmayan (Non-Lineer) Veriler Üzerindeki Performansı
Perceptron’un doğrusal (lineer) ve doğrusal olmayan (non-lineer) veriler üzerindeki performansını şu şekilde açıklayabiliriz:

### Doğrusal (linear) Veriler
Doğrusal veriler, bir düzlem veya doğru çizgisi ile iki farklı sınıfa ayrılabilen veri setleridir.
Örneğin: Veriler bir düz çizgiyle "sınıf 0" ve "sınıf 1" olarak ayrılabiliyorsa, bu veri doğrusal olarak ayrılabilir demektir.
Perceptron, doğrusal bir sınıflandırıcıdır, yani veriler düz bir çizgi (2D) ya da düzlem (3D ve üzeri) ile ayrılabiliyorsa doğru sonuçlar üretebilir.

- **AND ve OR Problemleri**:
    * AND Problemi: Veriler (1,0)→0, (0,1)→0, (1,1)→1, (0,0)→0 şeklindedir.
    Bu veri kümesi bir doğru ile ayrılabilir. Yani, AND problemindeki sınıflar doğrusal bir çizgi ile kolayca ayrılabilir.

    * OR Problemi: Veriler (1,0)→1, (0,1)→1, (1,1)→1, (0,0)→0 şeklindedir.
    OR probleminin sınıfları da doğrusal bir çizgiyle ayrılabilir.

Sonuç: Hem AND hem de OR problemi doğrusal (lineer) sınıflardır, yani bu veri setlerinin her iki sınıfı (0 ve 1) düz bir sınırla ayrılabilir. Bu da perceptron'un bu tür problemleri başarıyla çözmesini sağlar.

### Doğrusal Olmayan (non-linear) Veriler
Doğrusal olmayan veriler, bir doğru veya düzlem ile ayrılamayan veri setleridir.
Örneğin: Veriler bir dairesel desen ya da karmaşık bir sınır ile ayrılıyorsa, bu veri doğrusal olarak ayrılabilir değildir.
Perceptron, yalnızca doğrusal bir sınır öğrenebilir. Bu nedenle, doğrusal olmayan verilerde başarısız olur.

- **XOR Problemi**:
    XOR Problemi: Veriler (1,0)→1(0,1)→1, (1,1)→0(0,0)→0 şeklindedir.XOR probleminin sınıfları doğrusal bir çizgiyle ayrılamaz. Çünkü (0,1)(0,1) noktaları aynı sınıfta (1), ancak (0,0) ve (1,1) noktaları başka bir sınıfta (0). Bu tür veriler dairesel ya da daha karmaşık bir sınırla ayrılabilir.

Sonuç: XOR problemi doğrusal olmayan bir sınıflandırmadır, yani veriler doğrusal bir sınırla ayrılamaz. Bu durumda perceptron, sınıfları doğru şekilde ayıramaz ve başarısız olur.


![img](https://miro.medium.com/v2/resize:fit:1400/1*9wJLAp_0xxMdyCKxO8_LcQ.jpeg)