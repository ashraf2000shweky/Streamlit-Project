import streamlit as st

# مراجعة الأساسيات 

# كتابة النصوص بطرق مختلفة
title = st.title("Web App")

st.header('Header')
st.subheader('Subheader')
st.text('raw text')
st.caption('caption')
st.markdown(' # *heading1*')
st.write("<h3> This is normal writing </h3>",unsafe_allow_html = True)

st.markdown('---')

# إضافة الأزرار 
btn = st.button('Click')
if btn:
    st.write("I was clicked")

# هنا نقوك بتحميل صورة
with open('C:/Users/Lenovo/New folder/123.png','rb') as file:  
    st.download_button('download_image',data=file,file_name='APPL.png',mime='png')

# صندوق إختبار     
ch = st.checkbox('I agree with the terms')
if ch:
    st.write('Thanks for agree')
    # أزرار إختيار
r = st.radio('chosse a gategory',('business','politics','sports'))
if r:
    st.write('you chose',r)

# صناديق إختيار     
st.selectbox("choose a gategory",['business','politics','sports'] )
st.multiselect("choose a gategory",['business','politics','sports'])

# شريط رقمي 
sl = st.slider('choose a range',0,100)
st.write('you chosse',sl)

# شريط أسماء  
ss = st.select_slider('choose',['jack','john','mary','alex','rob'])
st.write('you chosse',ss)

st.markdown('---')

# عدة أشياء مفيدة 
col1,col2 = st.columns([1,3]) #  في تقسيم حيز العناصر list هنا إٍستفدنا من 
with col1:
    st.text_input('your name here')
with col2:
    st.text_area('your message')
st.number_input('your age')
st.time_input('time here')
st.date_input('date')
st.color_picker('color')

st.markdown('---')

# عرض الجداول بطرق مختلفة 
df = { 'name':['jack','john','mary','alex','rob'],
      'age':[23,32,26,40,31]}
st.dataframe(df)
st.table(df)

# تقسيم عدة خلايا 
col1,col2,col3 = st.columns(3)
with col1:  
     st.metric('temperature',"26 'c" ,-4)  
with col2:    
     st.metric('temperature',"23 'c" ,1)
with col3:
     st.metric('temperature',"20 'c" ,8)
     
# أيقونة إخفاء إظهار المحتوى
with st.expander('Click here'):
    col1,col2,col3 = st.columns(3)
    with col1:  
         st.metric('temperature',"26 'c" ,-4)  
    with col2:    
         st.metric('temperature',"23 'c" ,1)
    with col3:
         st.metric('temperature',"20 'c" ,8)

st.markdown('---')

# إستخدام الجانب اليساري 
st.sidebar.title('This is sidebar')
btn = st.sidebar.button('enter')
if btn:
    st.write("I was clicked")

    
