# MultiThreading in Big Data

Bu proje, müşteri şikayetleri içeren büyük bir veri setinde benzer kayıtları tespit etmek ve bu kayıtları bir masaüstü uygulamasında göstermek amacıyla geliştirilmiştir. Proje, veriler arasında benzerliklerin tespitinde **multithreading** kullanarak arama süresini azaltmayı hedefler.

## İçindekiler

- [Multithreading](#multithreading)
- [Veri Seti](#veri-seti)
- [Özellikler](#özellikler)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Yazarlar](#yazarlar)
- [Ekran Görüntüleri](#ekran-görüntüleri)

## Multithreading
Multithreading (çok iş parçacıklı çalışma) , bir merkezi işlem biriminin (CPU) (veya çok çekirdekli bir işlemcideki tek bir çekirdeğin) aynı anda işletim sistemi tarafından desteklenen birden fazla yürütme iş parçacığı sağlama yeteneğidir. Bu tür programlamada birden fazla iş parçacığı aynı anda çalışır. Çok iş parçacıklı model, sorgulamalı olay döngüsü kullanmaz. CPU zamanı boşa harcanmaz ve boşta kalma süresi minimumdur. Bu, daha verimli programlarla sonuçlanır. Herhangi bir nedenle bir iş parçacığı duraklatıldığında, diğer iş parçacıkları normal şekilde çalışır.

## Veri Seti
Bu veri seti, finansal ürünler ve hizmetler hakkında alınan gerçek dünya şikayetlerini içermektedir. Veri seti, müşterilerin Kredi Raporları, Öğrenci Kredileri, Para Transferi gibi finans sektöründeki birden fazla ürün ve hizmet hakkında yaptığı şikayetlerin farklı bilgilerini içermektedir.

Kullanılacak veri setine bu linkten ulaşabilirsiniz:
https://www.kaggle.com/datasets/selener/consumer-complaint-database
## Özellikler

- **Veri İşleme:** Şikayetler veri seti, null değerler, noktalama işaretleri ve stopword'lerden temizlenmiştir.
- **Benzerlik Tespiti:** Multithreading kullanılarak veriler arasındaki benzerlik oranları hesaplanmıştır.
- **Grafik Arayüz:** Kullanıcı dostu bir masaüstü uygulaması ile verilerin ve benzerlik oranlarının görselleştirilmesi sağlanmıştır.

<table style="border-spacing: 0; border-collapse: collapse;">
  <tr>
    <td style="padding: 0; vertical-align: middle">
      <img src="https://github.com/user-attachments/assets/5587cfb1-4f7e-4cae-947b-7086799d914a" width="400" />
    </td>
    <td style="padding: 0; vertical-align: middle;">
      <img src="https://github.com/user-attachments/assets/43c7cdc8-b045-47c5-b464-ff6d652838f8" width="400" />
    </td>
  </tr>
</table>

## Kullanılan Teknolojiler

- **Programlama Dili:** Python
- **GUI Araçları:** Qt Designer
- **Kütüphaneler:**
  - `nltk` - Stopword'leri kaldırmak için
  - `PyQt5` - Grafik arayüzü oluşturmak için
  - `threading` - Multithreading işlemleri için

## Kurulum

1. **Gerekli Kütüphaneleri Yükleyin:**
   Gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:
   ```bash
   pip install nltk pyqt5

2. **Stopword Veritabanını İndirin:**
   NLTK kütüphanesi tarafından kullanılan stopword veritabanını indirmek için Python komutunu çalıştırın:
   ```python
   import nltk
   nltk.download('stopwords')

3. **Proje Dosyalarını İndirin:**
   Proje dosyalarını GitHub'dan klonlayın veya indirin:
   ```bash
   git clone https://github.com/mevlutayilmaz/multithreading-in-big-data.git

4. **Uygulamayı Çalıştırın:**
   Proje dizininde `main.py` dosyasını çalıştırarak uygulamayı başlatın:
   ```python
   python main.py

5. **GUI'yi Dönüştürün:**
   Qt Designer ile oluşturulmuş `.ui` dosyasını Python koduna dönüştürün:
   ```python
   pyuic5 -o convertGui.py untitled.ui
   ```

   Bu adım, Qt Designer'da oluşturduğunuz grafik arayüzün Python koduna dönüştürülmesini sağlar. `convertGui.py` dosyasını proje dizininde bulabilirsiniz.

6. **Veri Setini Hazırlayın:**
   Proje dizininde `rows.csv` ve `rows2.csv` dosyalarını kullanarak veri setinizi hazırlayın. Bu dosyalar, benzerlik tespiti işlemleri için kullanılacaktır.

7. **Proje Yapılandırmasını Kontrol Edin:**
   `main.py`, `convertGui.py`, ve `Gui.py` dosyalarının doğru yapılandırıldığından emin olun. Her dosya, uygulamanızın doğru çalışması için gerekli olan kodu içermelidir.

8. **Test ve Geliştirme:**
   Uygulamanızı test edin ve gerekli geliştirmeleri yapın. Uygulama işleyişi ve kullanıcı arayüzü ile ilgili her türlü değişiklik bu aşamada yapılmalıdır.

## Kullanım
Uygulamanız açıldıktan sonra, kullanıcı arayüzü üzerinden veri setinizi yükleyebilir ve benzerlik tespiti işlemlerini başlatabilirsiniz.

## Ekran Görüntüleri
<table style="border-spacing: 0; border-collapse: collapse;">
  <tr>
    <td style="padding: 0; vertical-align: middle; border: none;">
      <img src="https://github.com/user-attachments/assets/ee9906a8-672b-4ee1-b784-4242f1e141ef" width="400" />
    </td>
    <td style="padding: 0; vertical-align: middle; border: none;">
      <img src="https://github.com/user-attachments/assets/96a98933-3b7a-4dcd-a94b-932dd3942a21" width="400" />
    </td>
  </tr>
  <tr>
    <td style="padding: 0; vertical-align: middle; border: none;">
      <img src="https://github.com/user-attachments/assets/94101795-b0c9-44da-9df8-c97125126c7a" width="400" />
    </td>
    <td style="padding: 0; vertical-align: middle; border: none;">
      <img src="https://github.com/user-attachments/assets/3d0ea4c1-a584-4bf9-9eb8-175da30cb9e8" width="400" />
    </td>
  </tr>
</table>

