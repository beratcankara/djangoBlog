# djangoBlog
Güncelleme Notları:

- Yorum ekleme özelliği eklendi.
- Kullanıcılar artık projenin içeriği hakkında yorum yapabilir.
- Yorumlar, projenin ana sayfasında görüntülenebilir ve paylaşılabilir.
- Yorumları silme ve düzenleme işlevleri de eklendi.

Bu güncellemeyle birlikte projeye interaktif bir tartışma ortamı getirilmiştir. Kullanıcılar, projenin gelişimine katkıda bulunabilir ve geribildirimde bulunabilirler. Yorum özelliği, projenin daha da gelişmesini ve topluluk katılımını teşvik etmeyi amaçlamaktadır.

Detaylı değişiklikleri ve kodu incelemek için commit log'una ve projenin [GitHub repository'sine] göz atabilirsiniz. Sizlerden gelecek geri bildirimleri sabırsızlıkla bekliyoruz!
# Blog Projesi

Bu proje, kullanıcıların makaleler paylaşabileceği bir blog uygulamasıdır.

## Açıklama

Bu projenin amacı, kullanıcıların blog yazılarını paylaşmalarına olanak sağlamaktır. Kullanıcılar kayıt olabilir, giriş yapabilir ve kendi makalelerini oluşturabilir, düzenleyebilir ve silebilirler. Ayrıca, diğer kullanıcıların makalelerini okuyabilir ve yorum yapabilirler.

## Başlangıç

Bu projeyi yerel bir ortamda çalıştırmak ve geliştirmeye başlamak için aşağıdaki adımları izleyin.

### Gereksinimler

Projenin çalışması için aşağıdaki gereksinimlere ihtiyacınız vardır:

- Python 3.x
- Django 3.x

### Kurulum

1. Projeyi klonlayın:

   ```bash
   git clone [https://github.com/kullanici_adi/blog-projesi.git](https://github.com/beratcankara/djangoBlog)
Proje dizinine gidin:

  `bash
  cd blog-projesi`
Sanal bir ortam oluşturun ve etkinleştirin:

``bash
python -m venv env
source env/bin/activate``
Gerekli bağımlılıkları yükleyin:

``bash
pip install -r requirements.txt``
Veritabanını oluşturun:

``bash
python manage.py migrate``
Geliştirme sunucusunu başlatın:

``bash
python manage.py runserver``
Sunucu http://localhost:8000 adresinde çalışacaktır.

Kullanım
Ana sayfada mevcut olan makaleleri görüntüleyebilirsiniz.
Yeni bir makale oluşturmak için "Yeni Makale Oluştur" butonunu tıklayabilirsiniz.
Makalelerin başlıklarına tıklayarak ayrıntılı içeriklerini görüntüleyebilirsiniz.
Makalelerin altında yorum yapabilirsiniz.
Katkıda Bulunma
Bu proje açık kaynaklıdır ve katkıda bulunmaktan mutluluk duyarız. Pull request göndererek, hata düzeltmeleri, yeni özellikler veya geliştirmeler ekleyebilirsiniz. Lütfen önerilerinizi veya sorularınızı "Issues" bölümünde paylaşın.

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakınız.

İletişim
Eğer projemizle ilgili herhangi bir sorunuz veya geri bildiriminiz varsa, bana e-posta yoluyla ulaşabilirsiniz: berat-can-kara@hotmail.com
