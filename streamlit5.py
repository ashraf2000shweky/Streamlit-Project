import streamlit as st
import pyshorteners as pyst # تسمح لنا بإحضار الرابط القصير 
import pyperclip # لنسخ الرابط
 


# تعريف متغير للرابط القصير 
shortner = pyst.Shortener()

st.markdown("<h1 > URL Shortner </h1>",unsafe_allow_html=True)

# إنشاء أيقونة 
form = st.form("name")
url = form.text_input("URL HERE")
s_btn = form.form_submit_button("Short")

# نقوم بالعمليات التالية عن الضغط على Short
if s_btn:
    shorted_url = shortner.tinyurl.short(url) # إحضار الرابط القصير 
    print(shorted_url) 
   # طباعة الرابط القصير       
    st.markdown("<h4> Short url </h4>",unsafe_allow_html=True)
    st.markdown(f"<h6 style ='text-align: center;'> {shorted_url} </h6>",unsafe_allow_html=True)
# دالة تقوم بنسخ الرابط 
def copying():
    pyperclip.copy(shorted_url)
     # إستخدام دالة copying لسنخ الرابط       
    c_btn = st.button("Copy",on_click=copying)

    
        