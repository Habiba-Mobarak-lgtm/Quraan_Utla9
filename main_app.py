import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="Habiba Studio Pro", layout="wide", initial_sidebar_state="collapsed")

# رابط قناة التليجرام الخاص بكِ
telegram_link = "https://t.me/Quraan_Utla9"

# 2. كود CSS مخصص (تم إزالة الـ f-string لتجنب أخطاء الأقواس)
st.markdown("""
    <style>
    /* شريط التليجرام العلوي */
    .telegram-bar {
        background: linear-gradient(90deg, #0088cc, #00a2ed);
        color: white !important;
        text-align: center;
        padding: 12px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        margin-bottom: 25px;
        display: block;
        text-decoration: none !important;
        box-shadow: 0px 4px 15px rgba(0, 136, 204, 0.3);
        transition: transform 0.2s;
    }
    .telegram-bar:hover {
        transform: scale(1.01);
        color: #f0f0f0 !important;
    }

    /* تعديل الاتجاه */
    .main { direction: rtl; text-align: right; }
    div[data-testid="stVerticalBlock"] { direction: rtl; }
    
    /* صندوق المعاينة */
    .phone-preview {
        border: 4px solid #262730;
        border-radius: 25px;
        background-color: #000000;
        width: 320px;
        height: 560px;
        margin: 0 auto;
        position: relative;
        overflow: hidden;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }
    
    button[data-baseweb="tab"] {
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
    }
    </style>
""", unsafe_allowed_html=True)

# --- شريط التليجرام في أعلى الصفحة ---
st.markdown(f'<a class="telegram-bar" href="{telegram_link}" target="_blank">📢 انضم لقناة التيليجرام الآن واشترك في المحتوى الحصري!</a>', unsafe_allowed_html=True)

# الهيدر العلوي للتطبيق
st.title("🌿 Habiba Studio Pro")
st.caption("استوديو متكامل لتصميم الفيديوهات والآيات القرآنية باحترافية")
st.write("---")

# 3. تقسيم الشاشة لعمودين (استخدام أرقام صحيحة لتجنب أي أخطاء في الـ Layout)
col_preview, col_control = st.columns([1, 2])

# --- لوحة التحكم (العمود الأيسر) ---
with col_control:
    st.subheader("🛠️ خيارات التخصيص")
    
    tab_text, tab_audio, tab_bg, tab_font = st.tabs(["📝 النص", "🎵 الصوت والقراء", "🎬 الخلفية", "🎨 الخطوط"])
    
    # --- تبويب النص ---
    with tab_text:
        verse_text = st.text_area("أدخل نص الآية الكريمة:", value="فَاصْبِرْ صَبْرًا جَمِيلًا", height=100)
        show_basmala = st.checkbox("إظهار البسملة في الأعلى", value=False)
        
    # --- تبويب الصوت والقراء ---
    with tab_audio:
        audio_source = st.radio("مصدر الصوت:", ["اختر قارئ أونلاين", "ارفع ملف صوتي خاص بك"])
        
        if audio_source == "اختر قارئ أونلاين":
            reader = st.selectbox("اختر القارئ:", [
                "محمد صديق المنشاوي (مرتل)", 
                "عبد الباسط عبد الصمد (مجود)", 
                "ماهر المعيقلي", 
                "مشاري راشد العفاسي"
            ])
            st.caption(f"سيتم تشغيل صوت {reader} تلقائياً عند التصدير.")
        else:
            uploaded_audio = st.file_uploader("اختر ملف الصوت من جهازك (MP3 / WAV):", type=["mp3", "wav"])

    # --- تبويب الخلفية ---
    with tab_bg:
        bg_type = st.radio("نوع الخلفية:", ["رفع فيديو مخصص", "رفع صورة ثابتة"])
        
        if bg_type == "رفع فيديو مخصص":
            uploaded_video = st.file_uploader("ارفع فيديو الخلفية (MP4):", type=["mp4", "mov"])
        else:
            uploaded_image = st.file_uploader("ارفع صورة الخلفية (JPG / PNG):", type=["jpg", "png"])
            
        bg_opacity = st.slider("تعتيم الخلفية (Overlay):", 0, 100, 50)

    # --- تبويب الخطوط ---
    with tab_font:
        font_color = st.color_picker("لون النص الأساسي:", "#FFCC00")
        shadow_color = st.color_picker("لون ظل الخط:", "#000000")
        font_size = st.slider("حجم الخط الأساسي:", 20, 100, 50)
        
        st.write("---")
        st.markdown("**📁 إضافة خطوط مخصصة**")
        uploaded_font = st.file_uploader("ارفع ملف خط من جهازك لتطبيقه (TTF / OTF):", type=["ttf", "otf"])

# --- شاشة المعاينة (العمود الأيمن) ---
with col_preview:
    st.markdown("<h3 style='text-align: center;'>📺 شاشة المعاينة (9:16)</h3>", unsafe_allowed_html=True)
    
    # تجهيز المتغيرات قبل دمجها لتجنب أي أخطاء برمجية
    opacity_value = bg_opacity / 100
    basmala_html = "<p style='color:#aaaaaa; font-size:16px;'>بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</p>" if show_basmala else ""
    
    # صندوق محاكاة الموبايل
    preview_html = f"""
        <div class="phone-preview">
            <!-- التعتيم فوق الخلفية -->
            <div style="position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(0,0,0,{opacity_value}); z-index: 1;"></div>
            
            <!-- النص القرآني -->
            <div style="z-index: 2; text-align: center; padding: 10px;">
                {basmala_html}
                <p style="color: {font_color}; font-size: {font_size}px; text-shadow: 2px 2px 8px {shadow_color}; font-weight: bold; line-height: 1.6;">
                    {verse_text}
                </p>
            </div>
        </div>
    """
    
    st.markdown(preview_html, unsafe_allowed_html=True)
    
    st.write("")
    if st.button("🎬 تصدير المقطع النهائي", use_container_width=True, type="primary"):
        st.success("جاري تجهيز وتصدير المقطع بأعلى دقة...")
