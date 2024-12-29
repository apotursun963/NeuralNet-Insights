
# Beynimizdeki Nöronlar Temelde Nasıl Çalışıyor ?
Nöronlar Birbirleriyle ağlar (iletişim) kurararak beyin fonksionlarını yerine getirir.
Beynimizdeki nöronların temel işlevi, Bilginin İşlenmesi ve Bilgi İletimi. 
Nöronlar, elektriksel ve kimyasal sinyallerle birbirleriyle iletişim kurar, bilgi aktarır ve beyin fonksiyonlarını yönetir. Bu süreç, düşünme, öğrenme, hafıza, hareket ve duygular gibi birçok beyin fonksiyonunu destekler.


## Biyolojik Nöron Nedir ?
Sinir hücresi ya da nöron sinir sisteminin temel fonksiyonel birimidir. Temel görevi, bilgi iletimini sağlamktır. insanın beyninde yaklaşık olarak 80 ila 100 milyar arasında nöron olduğu tahmin edilmektedir. Bu nöronlar bilgi işleme ve iletiminden sorumludur.

### Nöronun Temel Anatomik Yapısı
Nöronlar, sinir hücreleridir ve üç ana bileşenden oluşur:
- **Dendrit**: Diğer nöronlardan gelen elektriksel veya kimyasal sinyalleri sinapslar adı verilen bağlantı noktaları aracılığı ile alır ve hücre gövdesine iletir. Çok dallı yapısı sayesinde bir nöron, birçok farklı kaynaktan sinyal alabilir.

- **Hücre Gövdesi (Soma)**: Dendritler'den gelen sinyalleri toplar ve işler. Hücre gövdesinde bir dizi biyokimyasal işlem gerçekleşir. Bu işlemler sonucunda, **aksiyon potansiyeli** adı verilen bir elektrik sinyali üretilir. İçerisinde hücre çekirdeği ve metabolik faaliyetlerden sorumlu organeller bulunur.

- **Akson**: Oluşan aksiyon potansiyeli, akson boyunca ilerler. Akson, sinyalin hedef hücreye ulaşmasını sağlar. İşlenmiş sinyalleri hücre gövdesinden alıp sinapslar aracılığı ile diğer nöronlara iletir.

### Dinamik Değişim ve Öğrenme
Nöronlar arasındaki bağlantıların (sinapsların) gücü zamanla değişir. Bu değişim, öğrenme ve hafıza süreçlerinin temelidir. **Sinaptik plastisite** olarak bilinen bu süreç, sinapsların gücünün arttığı veya azaldığı durumları kapsar. Sinapsların gücü, nöronlar arasındaki iletişimin etkinliğini belirler.
Örneğin, sık kullanılan sinapslar **güçlenir** ve bu, bilgilerin daha hızlı ve etkili bir şekilde iletilmesini sağlar. Diğer yandan, kullanılmayan sinapslar **zayıflar** ve bu da unutmayı veya bilgilerin zamanla kaybolmasını sağlar. 

### Beynimizdeki Nöronların Muhteşem İşlevi
Beynimizdeki milyarlarca nöron, birbirleriyle karmaşık ağlar oluşturarak `görme`, `işitme`, `düşünme`, `mantık kurma`, `refleksler`, `hatırlama`, `öğrenme` ve `unutma` gibi işlevleri gerçekleştirir. Nöronların birbirleriyle binlerce bağlantı kurabilmesi, beynin karmaşık işlevlerini gerçekleştirmesine olanak tanır. 
Bu geniş ve karmaşık ağ, beynin çeşitli bilgileri işleyebilmesini, öğrenme ve hafıza süreçlerini yönetebilmesini ve çevremizle etkili bir şekilde etkileşime geçmesini sağlar.


## Yapay Nöron Nedir ?
Yapay Nöronlar, sinir ağlarının temel **bilgi işleme** birimidir ve insan beynindeki biyolojik nöronlardan esinlenerek geliştirilmiştir. Yapay nöronlar aslında *matematiksel fonksiyon* modelidir. fonksiyon işlevini görürler. Nöronlar, Birden Fazla girdileri alır, işlemler yapar ve tek bir çıktı üretir. 

### Nöronların Temel Bileşenleri
Her bir nöronun iki ana bileşeni vardır: Weight ve Bias
- **Ağırlık (Weight)**: Ağırlıklar, her bir girdiye atanan ve o girdinin nöronun çıktısına ne kadar katkıda bulunacağını belirleyen değerlerdir. Ağırlıklar, iki nöron arasındaki bağlantının gücünü belirler. Ağırlık değeri ne kadar büyükse, **bağlantı** o kadar güçlüdür, ağırlık değeri ne kadar düşükse, bağlantı o kadar zayıftır. Ağırlıklar, sinyalin ne kadar güçlü veya zayıf iletileceğini kontrol eder ve modelin öğrenme sürecinde güncellenir.

- **Sapma (Bias)**: Biaslar, yapay sinir ağlarındaki nöronların çıktısını ayarlamak için kullanılan ek terimlerdir. Bias, nöronun çıkışını belirli bir seviyede tutmak için eklenen bir sabittir.

### Nöronların Çalışma Mantığı
Birden fazla `girdi alınır` ve bu girdiler, her biri için belirlenmiş `ağırlıklarla (weights) çarpılır`. Çarpımların sonuçları toplanarak bir toplam elde edilir. Bu toplam değere bir `bias (sapma) eklenir` ve sonuç olarak nöronun çıkışı hesaplanır. Son olarak, bu toplam değer bir `aktivasyon fonksiyonu` aracılığıyla işlenir ve nöronun nihai çıktısı elde edilir. Matematiksel olarak, bu süreç şu şekile ifade edilebilir:
`Neuron Output = f(∑(Input × Weight) + Bias)`


![Nöron](https://media.geeksforgeeks.org/wp-content/uploads/20230410104038/Artificial-Neural-Networks.webp)
