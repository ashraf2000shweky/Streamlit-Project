import streamlit as st

# هنا قد تم الإستفادة من لفة css إخفاء أيقونة الأعدادات والتلميح السفلي   
st.markdown("""
             <style>
             .css-9s5bis.edgvbvh3
             {
                 visibility: hidden;
             }
             .css-1q1n0ol.egzxvld0
             {
                 visibility: hidden;
             }
             </style>
             """,unsafe_allow_html=True)
   
# إنشاء أيقونة تسجيل دخول 
st.markdown("<h1>  User Registration  </h1>",unsafe_allow_html=True)
form =st.form("Form 1 ")    
form.text_input("first name")
form.form_submit_button("submit")

st.markdown("# ")
st.markdown("# ")
st.markdown("# ")

# إنشاء أيقونات متعددة مع with 
st.markdown("<h1> User Registration  </h1>",unsafe_allow_html=True)
with st.form("form 2"):
    col1,col2 = st.columns(2)
    f_name = col1.text_input("first  name")
    print(f_name)
    l_name = col1.text_input("last  name")
    print(l_name)
    st.text_input("Email address")
    st.text_input("password")
    st.text_input("confine password")
    day,month,year = st.columns(3)
    day.text_input('day')
    day.text_input('month')
    day.text_input('year')
    s_stata = st.form_submit_button("submit")
    if f_name == '' or l_name == '':
        st.warning('Please fill above fields')
    else:
        st.success("Submitted successfully")
    
    
    
    
    
 
    
    
    
    
    
    
    
    
    
    