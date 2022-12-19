import streamlit as st
import pandas as pd
import  matplotlib.pyplot as plt

# هنا سوف ننشئ تطبيق يصور stocks Price

st.markdown("<h1 style ='text-align: center;'> data visualzation </h1>",unsafe_allow_html=True)
st.markdown("---")
files_names = list()

# رفع ملفات أسواق المال 
files = st.file_uploader("Upload multiple files", type=['xlsx','csv'], accept_multiple_files=True)
# إضافة أسماء الأسواق الى files_names
if files:
    for file in files:
        files_names.append(file.name)
    print(files_names)
    # إختيار سوق المال المراد تصويره    
    selected_files = st.multiselect("select file", options=files_names)
     # إختيار العامود المراد تصويره    
    if selected_files:
        option = st.radio("select entily against date",options=['None','High','Low','Open','Close','Volume','Adj Close'])
         # تصوير العامود المختار        
        if option !='None':
            print(option)
            for file in files:
                if file.name in selected_files:
                    # إستخدام باندس لقراءة الملف الذي تم تحميله                   
                    stocks = pd.read_csv(file,index_col=['Date'],parse_dates=True)
                    print(stocks[option])
                     # سوف نستخدم line chart and histogram                   
                    if option != 'Volume':
                            figure = plt.figure()
                            plt.title(f" {file.name.split('.')[0]} stock")
                            plt.ylabel(option)
                            plt.fill_between(stocks.index,stocks[option],color='skyblue')
                            plt.plot(stocks.index,stocks[option],alpha=0.5)
                    else:
                        figure = plt.figure()
                        plt.title(f" {file.name.split('.')[0]} stock")
                        plt.ylabel(option)
                        plt.grid(True)
                        plt.hist(stocks[option])
                        
                    st.write(figure) # إظهار المخطط