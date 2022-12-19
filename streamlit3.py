import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import numpy as np

# تشكيل عناصر لتصوير البيانات 
x =np.linspace(0,10,100)
y = np.array([1,2,3,4,5])
# هنا سوف نستخدم sidebar المكان الذي يسمح لنا بإضافة خيارت على التقرير أي يصبح تفاعلي 


with st.sidebar:
    selected = option_menu("select my graph", options=('line','bar','h-bar')
                           ,orientation='horizontal')


if selected == 'line':    
    st.title('Line Chart')
    fig = plt.figure()
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x))
    st.write(fig)
elif selected =='bar':
      st.title('Bar Chart')
      fig = plt.figure()
      plt.bar(y,y*10)
      st.write(fig)
else :
      st.title('H-Bar Chart')
      fig = plt.figure()
      plt.barh(y*10,y)
      st.write(fig)