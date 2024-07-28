# Proje Adı: TIKLAGIY

Bu proje, kullanıcılara vücut ölçülerine uygun kıyafet bulma ve satın alma süreçlerini kolaylaştırmak için geliştirilmiş kapsamlı bir platformdur. Kullanıcıların detaylı vücut ölçülerini kaydedip, bu ölçülere en uygun ürünleri bulmalarını sağlamak amacıyla tasarlanmıştır.

## Özellikler

### 1. Kullanıcı Yönetimi ve Kimlik Doğrulama

- **Özel Kullanıcı Modeli:** Django'nun varsayılan kullanıcı modelini genişleterek özelleştirilmiş bir kullanıcı modeli oluşturulmuştur.
- **Kayıt/Giriş/Şifre Sıfırlama:** Kullanıcıların platforma kaydolması, giriş yapması ve şifrelerini sıfırlamaları için gerekli işlevler.
- **E-posta Doğrulama:** Kullanıcıların e-posta adreslerini doğrulama sistemi.
- **Sosyal Medya Girişi:** Facebook, Google gibi sosyal medya hesaplarıyla giriş yapabilme.

### 2. Profil ve Ölçü Sistemi

- **Detaylı Ölçü Kaydı:** Kullanıcılar profillerine detaylı vücut ölçülerini kaydedebilir.
- **Çoklu Ölçü Profili:** Birden fazla ölçü profili oluşturabilme.
- **Fotoğraf Analizi ile Otomatik Ölçü Tahmini:** Yapay zeka destekli sistem, fotoğraflardan vücut ölçülerini tahmin eder.
- **Kullanıcı Tercihleri:** Favori markalar, stil tercihleri gibi bilgiler kaydedilebilir.

### 3. Gelişmiş Ürün Arama ve Filtreleme

- **Uygunluk Oranı Hesaplama:** Kullanıcının ölçülerine göre ürün uygunluk oranı hesaplanır.
- **Çoklu Kriterlere Göre Sıralama/Filtreleme:** Ürünler fiyat, beden uyumu, marka, kategori, kumaş türü, renk, desen, sezon gibi kriterlere göre sıralanabilir ve filtrelenebilir.
- **Vücut Tipine Göre Filtreleme:** Vücut tipine göre ürünleri filtreleyebilme.
- **Tercih Edilen Mağazalarda Arama:** Belirli mağazalarda ürün arama.

### 4. Kişiselleştirilmiş Ürün Önerileri

- **Yapay Zeka Destekli Öneriler:** Kullanıcının vücut tipi, ölçüleri, geçmiş aramaları, beğenileri, stil ve renk tercihlerine göre kişiselleştirilmiş ürün önerileri sunar.

### 5. Karşılaştırma ve Favori Listesi

- **Ürün Karşılaştırma:** Seçilen ürünleri karşılaştırabilme.
- **Favori Listesi:** Beğenilen ürünleri favori listesine ekleyebilme.
- **Hızlı Liste:** İlgi duyulan ürünleri hızlı bir şekilde kaydetme.

### 6. Mağaza Entegrasyonu ve Yönlendirme

- **Doğrudan Mağaza Yönlendirmesi:** Beğenilen ürünün linkine tıklayarak ilgili mağazaya yönlendirme.
- **Alışveriş Sonrası Bilgi Güncelleme:** Satın alınan ürünlerle ilgili ek bilgileri sisteme girme.
- **Mağaza Değerlendirme Sistemi:** Mağazaları puanlayıp yorumlayabilme.

### 7. Dinamik Beden ve Ölçü Sistemi

- **Marka Bazlı Beden Profilleri:** Her marka için özel beden profilleri oluşturma.
- **Detaylı Ürün Ölçüleri:** Her ürünün detaylı ölçüleri sisteme kayıtlı.
- **Kullanıcı Geri Bildirimiyle Ölçü Doğrulama:** Kullanıcı geri bildirimleriyle ölçü doğruluğunu artırma.
- **Sezonluk Ölçü Değişimi Takibi:** Sezonlar arasında farklı ölçüler kullanılması durumunda bu değişiklikleri takip etme.

### 8. Veri Analizi ve Trendler

- **Marka Ölçü Değişimi Analizi:** Markaların zaman içinde ölçülerinde yaptıkları değişikliklerin analizi.
- **Sezonluk Trend Takibi:** Hangi ürünlerin hangi sezonda popüler olduğunu belirleme.
- **Popüler Ürün/Stil Analizi:** Kullanıcı davranışlarına göre popüler ürün ve stillerin analizi.

### 9. Kullanıcı Geri Bildirimi ve Topluluk Özellikleri

- **Ürün Yorum/Puanlama Sistemi:** Kullanıcılar ürünleri puanlayabilir ve yorum yapabilir.
- **Kullanıcı Deneyimi Paylaşımı:** Satın alınan ürünler hakkında deneyim paylaşımı.
- **Topluluk Forumu:** Moda ve stil hakkında sohbet edilebilecek bir forum.
- **Kullanıcı İçerik Oluşturma:** Stil önerileri, kombinler gibi içeriklerin kullanıcılar tarafından oluşturulması.

### 10. Çoklu Dil ve Birim Desteği

- **Çoklu Dil Seçeneği:** Platform farklı dillerde kullanılabilir.
- **Otomatik Ölçü Birimi Dönüşümü:** Tercih edilen ölçü birimlerini kullanabilme.
- **Yerel Para Birimi Desteği:** Farklı ülkelerden kullanıcılar için yerel para birimleri kullanılabilir.

### 11. API ve Mobil Uygulama

- **API-First Yaklaşımı:** Mobil uygulamalar ve diğer sistemlerle entegrasyon için kapsamlı bir API sağlama.
- **E-Ticaret Entegrasyonları:** Büyük e-ticaret platformlarıyla entegrasyon sağlama.
- **Mobil Uygulama Geliştirme:** Platformun mobil uygulaması.

### 12. Veri Güvenliği ve KVKK Uyumluluğu

- **Kullanıcı Veri Güvenliği:** Kullanıcı verilerinin korunması için gerekli güvenlik önlemleri.
- **KVKK Uyumu:** Türkiye'nin Kişisel Verilerin Korunması Kanunu (KVKK) ile uyumlu.

### 13. Ürün Takip ve Geri Bildirim Sistemi

- **Satın Alınan Ürünleri Takip Etme:** Satın alınan ürünlerin teslimat durumunu takip edebilme.
- **Alışveriş Sonrası Bilgi Güncelleme:** Satın alınan ürünler hakkında geri bildirim sağlama.
- **Ürün Teslim Bildirimleri:** Ürün teslim alındığında bildirim gönderme.

### 14. Kullanıcı Doğrulama Sistemi

- **Ürün Özelliklerini Doğrulama:** Ürün açıklamalarının doğruluğunu teyit edebilme.
- **Çoklu Kullanıcı Geri Bildirimiyle Veri Güvenilirliği:** Benzer geri bildirimlerle bilginin güvenilirliğini artırma.

### 15. Ödül Sistemi

- **Kullanıcı Katkı Puanları:** Sisteme katkılardan puan kazanma.
- **Özel Unvanlar ve Rozetler:** Belirli bir puana ulaşan kullanıcılara özel unvanlar ve rozetler.

### 16. Ürün Varyasyonları

- **Renk ve Desen Varyasyonları Yönetimi:** Aynı ürünün farklı renk veya desen varyasyonlarını yönetebilme.
- **Varyasyonlar Arası Ölçü Farkı Takibi:** Farklı varyasyonlar arasında ölçü farklarını takip etme.

### 17. Fotoğraf ve Video Geri Bildirimi

- **Kullanıcı Ürün Fotoğrafları/Videoları:** Satın alınan ürünlerin fotoğraf ve videolarını yükleyebilme.
- **Gerçek Ürün Görünümü Paylaşımı:** Ürünün gerçek görünümü hakkında bilgi sağlama.

### 18. Dinamik Fiyat Takibi

- **Otomatik Fiyat Kontrolü:** Takip listesindeki ürünlerin fiyatlarını düzenli olarak kontrol etme.
- **Fiyat Değişikliği Bildirimleri:** Fiyat değişikliklerinde bildirim gönderme.

### 19. Satın Alma Deneyimi Değerlendirmesi

- **Ürün ve Mağaza Puanlama:** Ürün ve mağazaları puanlayabilme.
- **Detaylı Alışveriş Deneyimi Geri Bildirimi:** Kargo hızı, paketleme kalitesi, müşteri hizmetleri gibi konularda geri bildirim sağlama.

### 20. Ürün Ömrü ve Dayanıklılık Takibi

- **Uzun Vadeli Ürün Değerlendirmesi:** Ürünü uzun süre kullandıktan sonra geri bildirim sağlama.

### 21. Yapay Zeka Destekli Analiz

- **Kullanıcı Geri Bildirim Analizi:** Yapay zeka ile kullanıcı geri bildirimlerinin analizi.
- **Ürün Tutarsızlık Tespiti:** Ürün açıklamaları ve kullanıcı geri bildirimleri arasındaki tutarsızlıkları tespit etme.
- **Marka Ölçülendirme Eğilimi Analizi:** Markaların zaman içinde ölçülendirme eğilimlerini analiz etme.

### 22. Mağaza ve Marka İşbirliği

- **Anonim Veri Paylaşımı
