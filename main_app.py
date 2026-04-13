import streamlit as st

# إعدادات الصفحة - layout="wide" عشان يعطي مساحة زي ترتيل
st.set_page_config(page_title="حبوبة ستوديو - صانع الفيديوهات القرآنية", page_icon="📖", layout="wide")

# كود التجميل الجذري (CSS) ليحاكي تصميم ترتيل ستوديو
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    /* الخلفية الداكنة الفخمة والخط العام */
    .stApp {
        background-color: #0d1117; /* لون خلفية ترتيل الداكن */
        color: #e6edf3;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* العناوين الكبيرة والشيك */
    h1 { color: #ffffff; font-size: 36px !important; text-align: center; font-weight: 700; margin-bottom: 5px; }
    h3 { color: #e6edf3; font-size: 20px !important; font-weight: 600; border-bottom: 2px solid #238636; padding-bottom: 10px; margin-top: 30px;}

    /* تأثيرات الأزرار (Buttons) - نفس ستايل ترتيل */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #238636; /* أخضر ترتيل */
        color: white;
        border: 1px solid rgba(240,246,252,0.1);
        padding: 15px;
        font-weight: bold;
        font-size: 18px;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #2ea043; /* أخضر فاتح عند المرور */
        border-color: #8b949e;
        transform: translateY(-2px); /* حركة خفيفة */
    }

    /* تأثير عند الضغط (Active) */
    .stButton>button:active {
        transform: translateY(1px) scale(0.99);
    }

    /* زر التليجرام المميز */
    .tele-container {
        display: flex;
        justify-content: center;
        margin-bottom: 40px;
    }
    .tele-button {
        background-color: #0088cc;
        color: white !important;
        padding: 12px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-size: 16px;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(0,136,204,0.4);
    }
    .tele-button:hover {
        background-color: #00aaff;
        transform: scale(1.05);
    }

    /* تجميل خانات الاختيار والرفع */
    .stSelectbox label, .stFileUploader label, .stRadio label, .stSlider label {
        font-size: 16px !important;
        color: #8b949e !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 8px;
        background-color: #161b22;
        border: 1px solid #30363d;
    }

    /* تنسيق نظام "التبويبات" (Tabs) ليصبح مثل Steppers ترتيل */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        justify-content: center;
        background-color: #161b22;
        padding: 10px;
        border-radius: 15px;
        border: 1px solid #30363d;
    }
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background-color: transparent;
        border-radius: 10px;
        color: #8b949e;
        padding: 10px 30px;
        font-weight: 600;
        font-size: 16px;
        border: none;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #ffffff;
        background-color: #21262d;
    }
    .stTabs [aria-selected="true"] {
        background-color: #238636 !important;
        color: #ffffff !important;
        box-shadow: 0 4px 10px rgba(35,134,54,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 1️⃣ العنوان الرئيسي
st.title("📖 حبوبة ستوديو لصناعة المقاطع القرآنية ✨")

# 2️⃣ زر التليجرام المميز في المقدمة (لزيادة المشتركين)
st.markdown("""
    <div class="tele-container">
        <a href="https://t.me/اسم_قناتك" class="tele-button">🚀 انضمي لقناة التليجرام الآن</a>
    </div>
""", unsafe_allow_html=True)

st.write("<p style='text-align: center; color: #8b949e;'>استوديو متكامل لتحويل التلاوات الصوتية إلى مرئيات مذهلة. بلمستك الإبداعية.</p>", unsafe_allow_html=True)

# --- نظام الظهور "خطوة خطوة" المستوحى من ترتيل ---

# استخدام التبويبات Tabs كـ Steppers
step1, step2, step3 = st.tabs(["1. الصوت والقارئ 🔊", "2. الخلفية والتصميم 🖼️", "3. النص
