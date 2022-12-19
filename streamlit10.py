
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 

# هنا نقوم بتغيير أيقونة  
st.set_page_config(page_title='Sales Dashboard',page_icon=':bar_chart:',layout='wide' )   
 
# قراءة البيانات على النحو المطلوب 
df =  pd.read_excel('C:/Users/Lenovo/New folder/supermarket_sales.xlsx',
                  usecols='B:R',
                  nrows=1000)

# تغير أسم العامود لأنه سوف يتسبب في مشكلة لاحقاً
df = df.rename(columns={'Customer type':'Customer_type'} )
st.dataframe(df)

# إنشاء صندوق إختيار من متعدد ووضع القيم الإفضراضية هي عناصر العامود المحدد
city = st.sidebar.multiselect(
    'Select the City',
     options = df['City'].unique(),
     default = df['City'].unique()
    )

# إنشاء صندوق إختيار من متعدد ووضع القيم الإفضراضية هي عناصر العامود المحدد
customer_type = st.sidebar.multiselect(
    'Select the Customer_type',
     options = df['Customer_type'].unique(),
     default = df['Customer_type'].unique()
    )

# إنشاء صندوق إختيار من متعدد ووضع القيم الإفضراضية هي عناصر العامود المحدد
gender = st.sidebar.multiselect(
    'Select the Gender',
     options = df['Gender'].unique(),
     default = df['Gender'].unique()
    )
 


# هنا إن لم نغير أسم العامود لن يعمل الكود
# سوف نستخدم هذه الخطوة ليكون المخطط تفاعلي
# تم إستخدام @ لإشارة إلى المتغير  
df_selection = df.query("City == @city & Customer_type == @customer_type & Gender == @gender")



st.title(":bar_chart: Sales Dashboard")
st.markdown('##')

# حساب بعض المعلومات عن البيانات 
total_sales = int(df_selection['Total'].sum())
average_rating = round(df_selection['Rating'].mean(),1)
star_rating = ':star:' * int(average_rating) # إظهار التقيم بشكل نجوم 
average_sale_by_transaction = round(df_selection['Total'].mean(),2)
                                    
 
                           # إظهار المعلومات السابقة         
left_column , middle_column, right_column = st.columns(3)

with left_column:
    st.subheader('Total Sales:')
    st.subheader(f"US $ {total_sales}")

with middle_column:
    st.subheader('Average Rating:')
    st.subheader(f"{average_rating} {star_rating}")

with right_column:
    st.subheader('Average Sales by Transaction:')
    st.subheader(f"{average_sale_by_transaction}")    


st.markdown('---')

# تجميع البيانات بإستخدام أحد الأعمدة 
sales_by_product_line = df_selection.groupby(['Product line']).sum()[['Total']].sort_values(by='Total')             

 # تصوير البيانات بشكل تفاعلي 
  # عند التلاعب بالمنغيرات الثلاثة سوف يتم إعادة تشكيل df_selection بالتالي سوف يؤثر على المخطط 
fig , ax = plt.subplots() 
sns.barplot(x=sales_by_product_line['Total'],y=sales_by_product_line.index,ax=ax)
st.pyplot(fig)



# دعواتكم..........