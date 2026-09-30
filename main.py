import streamlit as st
import time
import os

# Sayfa ayarları
st.set_page_config(page_title="Sadece Senin İçin Güzeller Güzeli Yavrum ❤️", page_icon="🌹", layout="centered")

# Özel CSS ile tüm yazı renklerini özelleştirme
st.markdown("""
    <style>
    /* Arka plan rengi */
    .stApp {
        background-color: #fff0f5; /* Çok açık tatlı pembe */
    }
    
    /* Ana Başlıklar (h1, h2, h3) */
    h1, h2, h3 {
        color: #d63384 !important; /* Koyu Pembe / Fuşya */
        text-align: center;
    }

    /* Normal Yazılar, Paragraflar ve Düz Metinler */
    p, span, div, label {
        color: #4a2e35 !important; /* Koyu Bordo / Çikolata Tonu */
    }

    /* Sekme (Tab) İsimleri */
    .stTabs [data-baseweb="tab"] p {
        color: #c2185b !important; /* Sekme başlıklarının rengi */
        font-weight: bold;
    }

    /* Buton Tasarımı ve Yazı Rengi */
    .stButton>button {
        background-color: #ff69b4 !important; /* Buton arka planı */
        color: white !important; /* Buton içindeki yazı rengi */
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }

    /* Resim Yuvarlama ve Gölge */
    img {
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# Şifre kontrolü için oturum durumu (Session State)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# 1. ADIM: ŞİFRE EKRANI
if not st.session_state["authenticated"]:
    st.title("🔒 Özel Alan")
    st.write("Bu Siteye Sadece Benım Yavrum Girebilir!")
    
    SECRET_PASSWORD = "iskender"  # Küçük harf karşılığı
    
    password_input = st.text_input("Giriş Şifresi:", type="password", placeholder="İpucu: Favori Yemeğim...")
    
    if st.button("Giriş Yap ❤️"):
        # Türkçe karakter hassasiyeti için küçük harf dönüşümü
        clean_input = password_input.strip().replace("İ", "i").replace("I", "ı").lower()
        
        if clean_input == SECRET_PASSWORD:
            st.session_state["authenticated"] = True
            st.success("Şifre doğru! Giriş yapılıyor...")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Yanlış şifre! Tekrar dene bakalım...")

# 2. ADIM: SÜRPRİZ İÇERİK EKRANI (Giriş başarılıysa burası çalışır)
else:
    st.title("💖 Hoş Geldin Bitanem!")
    st.balloons()  # Ekranda balonlar uçar
    
    st.write("---")
    st.write("### Sana Küçük Bir Sürprizim Var...")

    # Sekmeler
    tab1, tab2, tab3 = st.tabs(["💌 Mektup", "📸 Anılarımız", "❓ Özel Test"])
    
    with tab1:
        st.subheader("Sana Özel Bir Not")
        st.write("""
        Sana Sevgimi Belki Belli Edemiyorum, Belki İşim Yok Ama Benim Zor Günlerimde Yanımda
        Olmaya Çalıştığın İçin Teşekkür Ederim. Sana Söylemek İstediğim O Kadar Çok Şey Var Ki
        Kelimelere Dökmeye Çalışırsam Yıllarımı Alır. Neyse, İyi Ki Hayatıma Girdin, İyi Ki
        Benim Hatunum, Yavrum Oldun. İyi Ki Varsın ❤️(Kodlama Okadarda Boş Birşey Değilmiş Dimi? 😅)
        """)
        
    with tab2:
        st.subheader("Bazı Hoşuma Giden Fotoğraflarımız 📸")
        
        # 3 Sütunlu Izgara Galeri Yapısı
        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]
        
        # 1'den 9'a kadar olan fotoğrafları otomatik bulur (.jpeg, .jpg, .png vs.)
        for i in range(1, 10):
            img_path = None
            for ext in ['.jpeg', '.jpg', '.png', '.JPEG', '.JPG', '.PNG']:
                if os.path.exists(f"{i}{ext}"):
                    img_path = f"{i}{ext}"
                    break
            
            target_col = cols[(i - 1) % 3]
            with target_col:
                if img_path:
                    st.image(img_path, caption=f"Anı {i}", use_container_width=True)
                else:
                    st.warning(f"{i}. fotoğraf bulunamadı")
        
    with tab3:
        st.subheader("Beni Ne Kadar Tanıyorsun?")
        st.write("Sadece ikimizin bilebileceği küçük bir soru-cevap oyunu!")
        ans = st.radio("Bizim Yapmayı En Çok Sevdiğimiz Şey Ne?", ["Uyumak", "Yemek YEMEK ", "Film İzlemek"])
        if st.button("Cevabı Gönder"):
            if ans == "Uyumak":
                st.success("Afferim Benim Yavruma Nasılda Biliyor Bizi Tabiiki UYUMAK❤️")
            else:
                st.info("Bu da doğru ama asıl cevap elbette UYUMAK ❤️")

    st.write("---")
    if st.button("Çıkış Yap"):
        st.session_state["authenticated"] = False
        st.rerun()