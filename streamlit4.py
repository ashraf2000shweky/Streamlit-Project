import streamlit as st
from PIL import Image
 # هنا المشروع يهدف الى تعديل خصائص ظهورالصورة  

 # سوف نستخدم خصائص لفة css لجعل العنوان في المنتصف 
st.markdown("<h1 style ='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)

# خط فاصل
st.markdown("---")

# تحميل صورة 
image = st.file_uploader("Upload your image", type=['png','jpg','jpeg'])
 
# إنشاء خصائص للصورة
info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:
    # إستخدمنا مكتبة PLT لتعديل على الصورة 
     info.markdown("<h4 style ='text-align: center;'> Information </h4>", unsafe_allow_html=True)
     img = Image.open(image)
     # معلومات عن الصورة                   
     size.markdown(f"<h6> size: {img.size}</h6>",unsafe_allow_html=True)
     mode.markdown(f"<h6> mode: {img.mode}</h6>",unsafe_allow_html=True)
     format_.markdown(f"<h6> format: {img.format} </h6>",unsafe_allow_html=True)
# تعديل ظهور طول وعرض الصورة          
     st.markdown("<h4 style ='text-align: center;'> Resizing </h4>", unsafe_allow_html=True)
     width = st.number_input("width",value=img.width)
     height = st.number_input('height',value=img.height)
     # تدوير الصورة حسب الدرجة التى نريد          
     st.markdown("<h4 style ='text-align: center;'> Rotations </h4>", unsafe_allow_html=True)
     degree = st.number_input("Degree")
     s_btn = st.button("submit")
    # هنا يتم تطبيق التعليمات التى أدخلناها          
     if s_btn:
         ed = img.resize((width,height)).rotate(degree)
     
         st.image(ed)
 
        
             
             
             
             
             
             
             
             
             
             
             
             