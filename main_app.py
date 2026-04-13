import streamlit as st
import time

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Habiba Studio | حبوبة ستوديو", page_icon="🌿", layout="centered")

# كود التجميل (CSS) - تصميم أبيض نظيف بلمسة احترافية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    .stApp {
        background-color: #ffffff;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* اسم الأداة */
    .main-title {
        color: #2e7d32;
        font-size: 30px;
        font-weight: 700;
        text-align: center;
        margin-top: 15px;
    }

    /* زر التليجرام باسم قناتك الجديد */
    .tele-btn {
        display: block;
        width: fit-content;
        margin: 10px auto 30px auto;
        background-color: #0088cc;
        color: white !important;
        padding: 12px 25px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        font-size: 16px;
        box-shadow: 0 4px 12px rgba(0, 136, 204, 0.3);
        transition: 0.3s;
    }
    .tele-btn:hover { transform: scale(1.05); background-color: #0077b5; }

    /* إطار المعاينة الحية */
    .preview-container {
        background-color: #111;
        border-radius: 20px;
        padding: 40px 15px;
        margin: 20px auto;
        max-width: 320px;
        min-height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 6px solid #222;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }

    /* الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: #2e7d32;
        color: white;
        padding: 15px;
        font-weight: 700;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# 1️⃣ العنوان وزر التليجرام (تم تحديث الرابط لاسم قناتك)
st.markdown('<div class="main-title">Habiba Studio 🌿</div>', unsafe_allow_html=True)
st.markdown('<a href="https://t.me/Quraan_Utla9" class="tele-btn">📢 انضم لقناة التليجرام الآن</a>', unsafe_allow_html=True)

# 2️⃣ شاشة المعاينة
st.write("<h5 style='text-align:center; color:#555;'>📺 معاينة التصميم الحالية</h5>", unsafe_allow_html=True)

col_cfg, col_view = st.columns([1, 1.2])

with col_cfg:
    txt = st.text_area("نص الآية:", "فَاصْبِرْ صَبْرًا جَمِيلًا", height=80)
    f_size = st.slider("حجم الخط", 20, 80, 40)
    f_color = st.color_picker("لون الخط", "#FFD700")

with col_view:
    st.markdown(f"""
        <div class="preview-container">
            <p style="color: {f_color}; font-size: {f_size}px; text-align: center; font-weight: bold;">
                {txt}
            </p>
        </div>
    """, unsafe_allow_html=True)

# 3️⃣ الخيارات
st.write("---")
t1, t2 = st.tabs(["🔊 الصوت", "📏 المقاس"])
with t1:
    st.selectbox("اختر القارئ:", ["المنشاوي", "عبد الباسط", "الحصري", "تلاوة خاصة"])
with t2:
    st.radio("مقاس الفيديو:", ["9:16 (Reels/TikTok)", "1:1 (Post)"])

# 4️⃣ محاكاة التحميل
if st.button("🎬 ابدأ بصناعة المقطع الآن"):
    bar = st.progress(0, text="جاري تجهيز مقطعك بجودة HD...")
    for p in range(100):
        time.sleep(0.02)
        bar.progress(p + 1)
    
    st.balloons()
    st.success("✨ الفيديو جاهز!")
    st.download_button("⬇️ تحميل الفيديو الآن", data="file", file_name="Quran_Video.mp4")


