import streamlit as st

# 1. إعداد الصفحة لتكون بعرض كامل وأنيق
st.set_page_config(page_title="Habiba Studio Pro", layout="wide", initial_sidebar_state="collapsed")

# رابط قناة التليجرام الخاصة بكِ (استبدلي الرابط برابط قناتك الحقيقي)
telegram_link = "https://t.me/Quraan_Utla9"

# 2. كود CSS مخصص لشريط التليجرام العلوي والواجهة الاحترافية
st.markdown(f"""
    <style>
    /* شريط التليجرام العلوي الاحترافي */
    .telegram-bar {{
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
    }}
    .telegram-bar:hover {{
        transform: scale(1.01);
        color: #f0f0f0 !important;
    }}

    /* تعديل اتجاه التطبيق للعربية */
    .main {{ direction: rtl; text-align: right; }}
    div[data-testid="stVerticalBlock"] {{ direction: rtl; }}
    
    /* ستايل صندوق المعاينة الطولي (يشبه مقاس الريلز 9:16) */
    .phone-preview {{
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
    }}
    
    /* تحسين شكل التبويبات (Tabs) لتصبح كالأزرار الاحترافية */
    button[data-baseweb="tab"] {{
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
    }}
    </style>
""", unsafe_allowed_html=True)

# --- شريط التليجرام في أعلى الصفحة تماماً ---
st.markdown(f'<a class="telegram-bar" href="{telegram_link}" target="_blank">📢 انضم لقناة التيليجرام الآن واشترك في المحتوى الحصري!</a>', unsafe_allowed_html=True)

# الهيدر العلوي للتطبيق
st.title("🌿 Habiba Studio Pro")
st.caption("استوديو متكامل لتصميم الفيديوهات والآيات القرآنية باحترافية")
st.write("---")

# 3. تقسيم الشاشة لعمودين (المعاينة على اليمين لسهولة الرؤية، والتحكم على اليسار)
col_preview, col_control = st.columns([1, 1.5])

# --- لوحة التحكم (العمود الأيسر المستوحى من Tarteel Studio) ---
with col_control:
    st.subheader("🛠️ خيارات التخصيص")
    
    # تقسيم الإعدادات لتبويبات علوية تماماً مثل الموقع
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
            
        enable_reverb = st.checkbox("إضافة صدى صوت للمسجد (Reverb)")
        if enable_reverb:
            reverb_intensity = st.slider("قوة الصدى:", 0, 100, 40)

    # --- تبويب الخلفية ---
    with tab_bg:
        bg_type = st.radio("نوع الخلفية:", ["رفع فيديو مخصص", "رفع صورة ثابتة"])
        
        if bg_type == "رفع فيديو مخصص":
            uploaded_video = st.file_uploader("ارفع فيديو الخلفية (MP4):", type=["mp4", "mov"])
            bg_opacity = st.slider("تعتيم خلفية الفيديو (Overlay):", 0, 100, 50)
        else:
            uploaded_image = st.file_uploader("ارفع صورة الخلفية (JPG / PNG):", type=["jpg", "png"])
            bg_opacity = st.slider("تعتيم صورة الخلفية (Overlay):", 0, 100, 50)

    # --- تبويب الخطوط ---
    with tab_font:
        font_color = st.color_picker("لون النص الأساسي:", "#FFCC00")
        shadow_color = st.color_picker("لون ظل الخط:", "#000000")
        font_size = st.slider("حجم الخط الأساسي:", 20, 100, 50)
        
        st.write("---")
        st.markdown("**📁 إضافة خطوط مخصصة**")
        uploaded_font = st.file_uploader("ارفع ملف خط من جهازك لتطبيقه (TTF / OTF):", type=["ttf", "otf"])

# --- شاشة المعاينة الحية اللايف (العمود الأيمن) ---
with col_preview:
    st.markdown("<h3 style='text-align: center;'>📺 شاشة المعاينة (9:16)</h3>", unsafe_allowed_html=True)
    
    # صندوق محاكاة الموبايل (الريلز)
    st.markdown(f"""
        <div class="phone-preview">
            <!-- محاكاة التعتيم فوق الخلفية -->
            <div style="position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(0,0,0,{bg_opacity/100}); z-index: 1;"></div>
            
            <!-- النص القرآني المنسق -->
            <div style="z-index: 2; text-align: center; padding: 10px;">
                {"<p style='color:#aaaaaa; font-size:16px;'>بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</p>" if show_basmala else ""}
                <p style="color: {font_color}; font-size: {font_size}px; text-shadow: 2px 2px 8px {shadow_color}; font-weight: bold; line-height: 1.6;">
                    {verse_text}
                </p>
            </div>
        </div>
    """, unsafe_allowed_html=True)
    
    # زر التصدير النهائي أسفل شاشة المعاينة ليصبح التطبيق تفاعلياً
    st.write("")
    if st.button("🎬 تصدير المقطع النهائي", use_container_width=True, type="primary"):
        st.success("جاري تجهيز وتصدير المقطع بأعلى دقة...")



