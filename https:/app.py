import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Quraan_Utla9", page_icon="📖")

# كود التجميل والتأثيرات (CSS)
st.markdown("""
    <style>
    /* تأثير حركة للأزرار */
    .stButton>button {
        background: linear-gradient(45deg, #0088cc, #005f8d);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,136,204,0.4);
        color: #ffeb3b;
    }
    /* تحسين شكل خانات الرفع */
    .stFileUploader {
        border: 2px dashed #0088cc;
        border-radius: 15px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Quraan_Utla9")
st.subheader("✨ أداة حبوبة الاحترافية")

# شريط جانبي (قناة التليجرام)
with st.sidebar:
    st.markdown("### 📢 قناة المشروع")
    st.link_button("انضمي لـ Quraan_Utla9 🚀", "https://t.me/YourChannelLink")

# --- الخطوة 1: الملفات الأساسية ---
st.write("### 1️⃣ ارفع الوسائط")
col1, col2 = st.columns(2)
with col1:
    bg = st.file_uploader("صورة الخلفية", type=["jpg", "png"])
with col2:
    audio = st.file_uploader("ملف الصوت", type=["mp3", "wav"])

# --- الخطوة 2: ميزة الخطوط المخصصة ---
st.write("### 2️⃣ الخطوط والتصميم")
custom_font = st.file_uploader("لو عندك خط معين حابه تضيفيه (اختياري)", type=["ttf", "otf"])
if custom_font:
    st.success(f"تم اعتماد الخط: {custom_font.name} ✅")

# --- الخطوة 3: التخصيص ---
mode = st.radio("طريقة العرض:", ["آية كاملة", "كلمة بكلمة"])

# زر التنفيذ مع تأثيرات
if st.button("توليد الفيديو السحري 🎬"):
    if bg and audio:
        st.balloons()
        st.success("أداة حبوبة بدأت السحر.. جاري المعالجة! ✨")
    else:
        st.warning("يا حبوبة، محتاجين الصورة والصوت الأول 😅")
