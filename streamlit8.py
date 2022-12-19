import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# إنشاء تقرير عن البيانات 

st.title('Data Analysis')
st.subheader('Data Analysis using Python')
upload = st.file_uploader('Upload Your Data set') # csv تحميل أي ملف 
if upload: # التأكد إذ قمنا بعملية التحميل 
    data = pd.read_csv(upload)
    # إظهار أول وأخر 5 سطور في البيانات 
if upload: 
     if st.checkbox('Preview Dataset'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())
     # إظهار نوع المخزن فيه كل عامود    
if upload: 
    if st.checkbox('DataType of Each Column'):
        st.write(dict(data.dtypes))
        
        # إظهار عددالأعمدةو عددالسطور      
if upload:
    data_shape = st.radio('What dimension do you want to check?',('Rows','Columns'))
    if data_shape =='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape =='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])
    # تصوير القيم المفقودة في البيانات إن وجدت  
if upload:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox('Null values in the dataset'):
            fig, ax = plt.subplots()
            sns.heatmap(data.isnull(),ax=ax)
            st.pyplot(fig)
    else:
             st.success('No missing Values')
             
             # معرفة فيما إذ يوجد قيم متكررة في البيانات ثم نترك الخيار للمستخدم لإسقاطها أو تركها 
if upload:
    test = data.duplicated().any()
    if test == True:
        st.warning('This dataset contains some duplicate values')
        dup = st.selectbox('Do you want to remove duplicate values?', \
                           ('Select one','Yes','No'))
        if dup == 'Yes':
            data = data.drop_duplicates()
            st.text('Duplicate Values are Removed')
        if dup == 'NO':
            st.text('OK no problrm')

# معرفة معلومات إحصائية عن البيانات 
if upload:
    if st.checkbox('summaary of Dataset'):
        st.write(data.describe())
     
       # زر الختام  
if st.button('About App'):
    st.text('Built With streamlit')
    st.markdown('*Thanks to Streamlit*')
    
        