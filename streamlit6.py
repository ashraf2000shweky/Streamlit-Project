import streamlit as st
import pandas as pd
import  matplotlib.pyplot as plt
import mplfinance as mpf
import pandas_ta as ta

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
                    stocks = pd.read_csv(file,index_col=['Date'],parse_dates=['Date'])
                    stocks.index = pd.to_datetime(stocks.index ,utc =True)
                    print(stocks[option])
                     # سوف نستخدم line chart and histogram                   
                    if option != 'Volume':
                            figure = plt.figure()
                            plt.title(f" {file.name.split('.')[0]} stock")
                            plt.ylabel(option)
                            plt.fill_between(stocks.index,stocks[option],color='skyblue')
                            plt.plot(stocks.index,stocks[option],alpha=0.5)
                            
                            macd = stocks.ta.macd()
                            fig , ax =plt.subplots(3,1,sharex=True,figsize=(7,10),gridspec_kw= {'height_ratios':[3,2,2]})
                            
                            fig.set_edgecolor('k')
                            fig.set_linewidth(4)
                            fig.set_facecolor('cyan')
                            ax3 = ax[2].twinx()
                            
                            p2 = [ mpf.make_addplot(stocks['High'],color='g',ax=ax[2]),  
                                   mpf.make_addplot(stocks['Low'],color='b',ax=ax[2]),
                                   mpf.make_addplot(macd['MACD_12_26_9'],ax=ax3,color='r')] 
                                                     
                                                     
                            mpf.plot(stocks,type='candle',ax=ax[0], addplot=p2 ,style='blueskies',volume=ax[1],mav=(6,9))
                            fig.suptitle(file.name.split('.')[0])
                            
                            ax[0].legend(labels=['_nolegend_','_nolegend_','mav6','mav9'])
                            ax[2].legend(['High','Low'])
                            ax3.legend(['MACD'],bbox_to_anchor=[0.7,0.2])
                            ax[2].grid(False)
                            ax[0].set_ylabel('Price',fontsize=15,labelpad=30,color='r')
                            ax[1].set_ylabel('Volume',fontsize=10,labelpad=35,color='r')
                            
                            plt.tight_layout()
                            plt.show()                    
                            
                    else:
                        figure = plt.figure()
                        plt.title(f" {file.name.split('.')[0]} stock")
                        plt.ylabel(option)
                        plt.grid(True)
                        plt.hist(stocks[option])
                        
                        macd = stocks.ta.macd()
                        fig , ax =plt.subplots(3,1,sharex=True,figsize=(7,10),gridspec_kw= {'height_ratios':[3,2,2]})
                        
                        fig.set_edgecolor('k')
                        fig.set_linewidth(4)
                        fig.set_facecolor('cyan')
                        ax3 = ax[2].twinx()
                        
                        p2 = [ mpf.make_addplot(stocks['High'],color='g',ax=ax[2]),  
                               mpf.make_addplot(stocks['Low'],color='b',ax=ax[2]),
                               mpf.make_addplot(macd['MACD_12_26_9'],ax=ax3,color='r')] 
                                                 
                                                 
                        mpf.plot(stocks,type='candle',ax=ax[0], addplot=p2 ,style='blueskies',volume=ax[1],mav=(6,9))
                        fig.suptitle(file.name.split('.')[0])
                        
                        ax[0].legend(labels=['_nolegend_','_nolegend_','mav6','mav9'])
                        ax[2].legend(['High','Low'])
                        ax3.legend(['MACD'],bbox_to_anchor=[0.7,0.2])
                        ax[2].grid(False)
                        ax[0].set_ylabel('Price',fontsize=15,labelpad=30,color='r')
                        ax[1].set_ylabel('Volume',fontsize=10,labelpad=35,color='r')
                        
                        plt.tight_layout()
                        plt.show()    
                        
                    
                    st.markdown("#")
                    st.markdown("#")
                    st.write(figure)
                    st.pyplot(fig) 

                    
                    
                    
                    
                    
                    