import streamlit as st

import streamlit as st

# إعدادات الصفحة - العرض الكامل
st.set_page_config(page_title="حبوبة ستوديو - جنة الإبداع", page_icon="🌿", layout="wide")

# كود التجميل (CSS) - خلفية طبيعية وتنسيق احترافي للموبايل
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    /* خلفية طبيعية مريحة للعين (جنة) */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)), 
                    url('https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&q=80&w=1000');
        background-size: cover;
        background-attachment: fixed;
    }

    html, body, [class*="st-"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* تنسيق الخطوات (Tabs) لتكون واضحة ومبهرة */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 15px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 10px;
        color: #2e7d32;
        font-weight: bold;
        padding: 10px 20px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #2e7d32 !important;
        color: white !important;
    }

    /* زر التليجرام المبهر */
    .tele-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .tele-button {
        background-color: #0088cc;
        color: white !important;
        padding: 12px 25px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,136,204,0.4);
        transition: 0.3s;
    }

    /* الأزرار الخضراء */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: #2e7d32;
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 1️⃣ العنوان
st.title("🌿 حبوبة ستوديو الاحترافي ✨")

# 2️⃣ أيقونة التليجرام في أول الصفحة (طلبك الأساسي)
st.markdown("""
    <div class="tele-container">
        <a href="https://t.me/Quraan_Utla9" class="tele-button">📢 انضمي لقناة التليجرام الآن</a>
    </div>
""", unsafe_allow_html=True)

st.write("<p style='text-align: center; color: #1b5e20; font-weight: bold;'>صممي مقطعك القرآني خطوة بخطوة</p>", unsafe_allow_html=True)

# 3️⃣ نظام الخطوات (التبويبات)
step1, step2, step3 = st.tabs(["🔊 القارئ", "🖼️ الخلفية", "✍️ الخط والآيات"])

with step1:
    st.subheader("اختر التلاوة")
    qari = st.selectbox("اسم القارئ:", ["المنشاوي (مجود)", "عبد الباسط (مرتل)", "الحصري", "رفع ملف خاص"])
    if qari == "رفع ملف خاص":
        st.file_uploader("ارفع ملف الصوت (MP3)", type=["mp3"])

with step2:
    st.subheader("تصميم المشهد")
    bg = st.radio("نوع الخلفية:", ["طبيعة خلابة", "مخطوطات إسلامية", "رفع صورة خاصة"])
    if bg == "رفع صورة خاصة":
        st.file_uploader("ارفع صورتك")
    st.slider("تعتيم الخلفية", 0, 100, 40)

with step3:
    st.subheader("تخصيص الآيات (طلبك الخاص)")
    col1, col2 = st.columns(2)
    with col1:
        font_type = st.selectbox("نوع الخط:", ["العثماني (حفص)", "خط النسخ", "الخط الأميري"])
        font_color = st.color_picker("لون الخط", "#ffffff")
    with col2:
        font_size = st.slider("حجم الخط", 20, 100, 50)
        display_type = st.radio("ظهور الآيات:", ["كلمة بكلمة", "آية كاملة"])

# زر الإنتاج النهائي
st.write("---")
if st.button("🎬 ابدأ بصناعة المقطع"):
    st.balloons()
    st.success("تم استلام طلبك! استوديو حبوبة بدأ العمل..")

