import streamlit as st
from datetime import time 

# إضافة ألفاظ كلامية بطرق مختلفة
st.title('hi  i am streamlit web app')
st.subheader('hi i am a subheader')
st.header('hi i am a header')
st.text('hi i am text and i will be the best data analysis in the world ')

# إستدخدام تعابير لغة البرمجة markdown 
st.markdown("**hello** world")
st.markdown("*hello* world")
st.markdown("# hello world")
st.markdown("## hello world")
st.markdown("### hello world")
st.markdown("#### hello world")
st.markdown("> hello world")
st.markdown("---")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
# إضافة شرح 
st.caption('i am a caption')

# إستخدام تعابير لفة البرمجة latex  
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
 
# كتابة كود برمجي
code  = """ 
import pandas as pd
data = pd.read_csv('data.csv')
"""
st.code(code,language='python')

# هذه الدالة تأخذ أي شي 
st.write("## H2")

# إظهار metric 
st.metric(label='wind speed', value="120ms^-1",delta="1.4ms^-1")
 
# لنكون DataFrame
import pandas as pd 
table = pd.DataFrame({"column 1": [1,2,3,4,5,6,7],
                     "column 2": [11,12,13,14,15,16,17]})

# طرق عرض DataFrame 
st.table(table)
st.dataframe(table)

# إضافة صورة 
st.image("/Users/Lenovo/New folder/123.png",caption="APPL stock market")
 
# إضافة مقطع صوتي
st.audio("/Users/Lenovo/New folder/001.mp3")
st.caption("سورة الفاتحة ")
# إضافة فيديو
st.video("/Users/Lenovo/New folder/Damascus.mp4")
st.caption("Damascus_Syria ")

# إضافة مربع تحقق يمكن أن يظهر اي شي نحتاجه
state = st.checkbox("checkbox")
if state:
    st.write('hi')
else :
    pass

# إضافة مفتاح إختيار من متعدد
radio_btm= st.radio("where are you from", options=('Syria','US'),)

# إضافة زر
btn = st.button("chick me")
if btn:
    st.write('hello')
else:
    pass

# صناديق إختيار
select  = st.selectbox("do you love python ", ('yes','no'))
mul_select = st.multiselect("what is your favourite Tech brand", ('FB','APPLE','TESLA'))

st.write(mul_select)

# تحميل ملفات 
st.title('uploading files')
st.markdown("---")

# تحميل ملف واحد
img = st.file_uploader("place upload image", type=['pnd','jpg'])
if img is not None:
    st.image(img)
    
# تحميل أكثر من ملف
imgs = st.file_uploader("place upload images", type=['pnd','jpg'],accept_multiple_files=True)
if imgs is not None:
         st.image(imgs)
# تحميل شريط تمرير 
val = st.slider("this is slider",min_value=50,max_value=150,value=100)
print(val)

# كتابة نص 
val = st.text_input("enter your course title",max_chars=100)
print(val)

val = st.text_area("course desription")
print(val)

# إدخال تاريخ
val = st.date_input("enter your date")
print(val)

# إدخال وقت 
val = st.time_input("enter your date",value=time(0,0,0))
             
     
        
     
        
     
        
     
        
     
        
     
        
     
        
     
        
     