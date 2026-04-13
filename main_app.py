import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="حبوبة ستوديو الاحترافي", page_icon="🌿", layout="centered")

# كود التجميل والتأثيرات (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .main {
        background-color: #f0f4f0; 
    }
    
    h1 { color: #1b5e20; font-size: 30px !important; text-align: center; margin-bottom: 5px; }
    
    /* تأثيرات الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        background: linear-gradient(135deg, #4caf50, #2e7d32);
        color: white;
        border: none;
        padding: 12px;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }

    /* زر التليجرام العلوي */
    .tele-container {
        display: flex;
        justify-content: center;
        margin-bottom: 30px;
    }
    .tele-button {
        background-color: #0088cc;
        color: white !important;
        padding: 10px 25px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-size: 14px;
        transition: 0.3s;
        box-shadow: 0 4px 10px rgba(0,136,204,0.3);
    }
    .tele-button:hover {
        background-color: #006699;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# العنوان
st.title("🌿 حبوبة ستوديو لصناعة المقاطع القرآنية ✨")

# --- قسم التليجرام في أول الصفحة ---
st.markdown("""
    <div class="tele-container">
        <a href="https://t.me/Quraan_Utla9" class="tele-button">📢 انضمي لقناة التليجرام الآن</a>
    </div>
""", unsafe_allow_html=True)

st.write("<p style='text-align: center; color: #555;'>مساحتك الإبداعية لنشر كلام الله بأجمل صورة</p>", unsafe_allow_html=True)

# الخطوات
with st.expander("1️⃣ اختر القارئ (أصوات جاهزة أو ارفع ملفك)", expanded=True):
    qari_option = st.selectbox("القائمة الصوتية:", ["المنشاوي (مجود)", "عبد الباسط (مرتل)", "الحصري (المصحف المعلم)", "رفع تلاوة من جهازي"])
    if qari_option == "رفع تلاوة من جهازي":
        st.file_uploader("ارفع ملف MP3", type=["mp3"])

with st.expander("2️⃣ اختر التصميم والخلفية"):
    bg_style = st.radio("ستايل الخلفية:", ["مناظر طبيعية هادئة", "مخطوطات إسلامية", "خلفية سوداء فخمة"])
    st.slider("وضوح الخط القرآني", 20, 100, 80)

# زر التشغيل
st.write("---")
if st.button("🎬 ابدأ بصناعة المقطع الآن"):
    st.balloons()
    st.success("جاري دمج الصوت مع الصورة.. ثواني ويكون مقطعك جاهزاً!")

