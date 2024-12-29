
# Yapay Sinir Ağları (Artificial Neural Networks - ANN)
Yapay Sinir Ağları, derin öğrenmenin temelini oluşturur ve insan beynindeki sinir hücrelerinden esinlenerek geliştirilmiştir. Sinir ağı, çok sayıda nöronun (yapay sinir hücreleri) birbirine bağlı olduğu ve verilerin işlenerek sonuçların üretildiği bir yapıdır. Bu ağ, girdileri alır, işleyerek çıktılar üretir ve öğrenme süreci sayesinde modelin performansını artırır.

## Yapay sinir ağlarının temel bileşenleri
Nöronlar YSA'nın Ana bileşenlerindendir. daha fazla bilgi için [Nöronlar](1.%20Neuron/README.md)

- **Sinaps (Synapse)**: Sinaplar, Nöronlar arasındaki bağlantıları temsil eder. Her bağlantının bir ağırlığı vardır ve bu bağlantıların gücünü belirler. Bağlantılar, bilgi iletimini sağlar ve nöronlar arasındaki etkileşimi düzenler.

- **Katman (Layer)**: YSA, genellikle katmanlardan oluşur. Her katman, belirli sayıda nöron içerir. 
    - Girdi Katmanı (Input Layer): Ham veriyi alan katmandır. Her nöron, bir **giriş özelliğine** karşılık gelir.
    - Gizli Katmanlar (Hidden Layers): Bu katmanlar, ağın derinliğini oluşturur ve veriler üzerinde daha karmaşık dönüşümler yapar. Her gizli katman, bir önceki katmandan gelen bilgiyi işler ve bir sonraki katmana iletir. 
    - Çıktı Katmanı (Output Layer): Bu katman, nihai tahminleri veya sonuçları üretir. Çıkış katmanındaki nöron sayısı, yapılacak göreve (örneğin, sınıflandırma ise sınıf sayısına) bağlıdır. 
- **Aktivasyon Fonksiyonları (Activation function)**: Aktivasyon fonksiyonu, bir nöronun çıkış değerini belirli bir aralıkta sınırlayan veya dönüştüren işlevdir, Aktivasyon fonksiyonları, nöronların çıktısını genellikle 0 ile 1 veya -1 ile 1 arasına sınırlayarak modelin daha stabil ve hızlı öğrenmesini sağlar. Büyük veya çok küçük değerler, ağırlık güncellemelerinde sorun yaratabilir ve eğitimi zorlaştırabilir. Bu sınırlama, öğrenme sürecini daha kararlı ve verimli hale getirir. Bu fonksiyonlarının bazıları çıkışı belirli bir aralıkta sınırlar (sigmoid, tanh, softmax), bazıları ise çıkışı sınırlandırmaz ve sadece negatif değerleri sıfırlar (ReLU).
    * **Sigmoid**: Çıktıyı 0 ile 1 arasında sınırlar. Özellikle ikili sınıflandırma problemlerinde kullanılır.
    * **Tanh**: Çıktıyı -1 ile 1 arasında sınırlar. Sigmoid'e göre daha geniş bir aralık sağlar.
    * **ReLU**: Negatif değerleri sıfırlar, pozitif değerleri ise olduğu gibi bırakır. Ağın gizli katmanlarında kullanılır. 
    * **Softmax**: Her sınıfın çıkış değerini 0 ile 1 arasında bir olasılığa dönüştürür ve tüm sınıfların olasılıklarının toplamı 1 olur. Genellikle Çoklu sınıflandırma problemleri için kullanılır.

## YSA'nın öğrenme süreci
Yapay sinir ağı, weight ve bias güncellenmesiyle öğrenir. Bu süreç, **ileri besleme** ve **geri yayılım** olarak iki ana aşamadan oluşur.
- **İleri Besleme (Feed Forward)**: İnput verileri input katmanından başlayarak ağın son katmanınana kadar ilerler. her bir katmandaki nöronlar aldığı inputları **ağırlıklandırır**, **bias** ekler ve **aktivasyon fonksiyonunu** uygular ve bir çıktı üretir. her nöronun çıktısı bir sonraki katmandaki nöronun inputu olur ve bu işlem ağın son katmanına kadar ilerler. ileri besleme hareketinde bilgi sadece `tek yönlü` ileri doğru yol almaktadır. Bu işlem ağın o andaki tahminini/sonucunu hesaplamak için kullanılır.
- **Geri Yayılım (Backpropagation)**: Ağın öğrenme sürecinde, tahmin edilen çıktılar ile gerçek çıktılar arasındaki **hata** hesaplanır ve bu hata, ağırlıkların ve bias'ların güncellenmesi için kullanılır. Bu süreç, *Gradyan İniş (Gradient Descent)* algoritması ile gerçekleştirilir. 

![YSA](https://media.springernature.com/lw1200/springer-static/image/art%3A10.1038%2Fs41377-024-01590-3/MediaObjects/41377_2024_1590_Fig3_HTML.png)

Öztele, YSA, nöronların birbirleriyle bağlantı kurarak oluşturduğu yapılar olup, insan beynindeki sinir ağlarını taklit eder. *Girdi*, *gizli* ve *çıktı* nöronlarından oluşan katmanlara sahiptir. Nöronlar arasındaki bağlantılar ağırlıklarla ifade edilir ve bu ağırlıklar bağlantının gücünü belirler. Nöronlar, kendilerine gelen girdileri toplar, ağırlıklarla çarpar ve bir sapma ekler. Aktivasyon fonksiyonu ile işlem sonucu elde edilir. YSA'nın öğrenme süreci, ileri yayılım ve geri yayılım aşamalarıyla ağırlıkların ve önyargıların güncellenmesiyle gerçekleşir. Bu sayede YSA, karmaşık problemleri çözebilir.

## Kaynaklar
- **Kitaplar**
    - [Derin Öğreme - lan Goodfellow, Yoshua Bengio, Aaron Courville](https://www.kitapyurdu.com/kitap/derin-ogrenme-ciltli/480279.html?srsltid=AfmBOopJ99_exUs6QL8fJwm9jyqKGUcQxVLEqQ5uvhp04DlwMUp1BzQ4)
    - [Derin Öğrenme - Atınç Yılmaz, Umut Kaya](https://www.kodlab.com/muhendislik/96-derin-ogrenme-9786052118399.html?srsltid=AfmBOopzYaV1_eiyn1E0mtkQw69KwHCYiEFQ74JFMJvLIWywWWdUypLR)

- **Videolar**
    - [But what is a neural network? | Deep learning chapter 1  ](https://www.youtube.com/watch?v=aircAruvnKk&t=186s)
    - [I Built a Neural Network from Scratch](https://www.youtube.com/watch?v=cAkMcPfY_Ns&t=30s)
    - [Building a neural network FROM SCRATCH (no Tensorflow/Pytorch, just numpy & math)](https://www.youtube.com/watch?v=w8yWXqWQYmU&t=83s)

- **Makaleler**
    - [Neural network (machine learning)](https://en.wikipedia.org/wiki/Neural_network_(machine_learning))
    - [What is a Neural Network?](https://aws.amazon.com/what-is/neural-network/)
