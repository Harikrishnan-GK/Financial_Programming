#==============================================================================
# Tab 1
#============================================================================================================================================================
# Initiating
#==============================================================================

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta,date
import yahoo_fin.stock_info as si
import streamlit as st
import pandas_datareader.data as web
import datetime as dt
import numpy as np
import mplfinance as mpf



def tab1():
    
    # Add dashboard title and description
    st.title("Financial dashboard-Yahoo Finance")
    st.write("Data source: Yahoo Finance")
    st.header('Summary')
    
    # Add table to show stock data
    @st.cache
    def GetQuoteTable(ticker):
     return si.get_quote_table(ticker)
 
    def GetStockData(tickers, start_date , end_date):
     return pd.concat([si.get_data(tick, start_date, end_date) for tick in tickers])
    
        # Add selection box
 

     
    days = st.sidebar.selectbox('time', ['1M','3M','6M','YTD', '1Y', '3Y', '5Y','MAX'])
    yr = datetime.today().date().year
    ytd = datetime.today().date()-datetime(yr, 1, 1).date()
    
   
    
    # Add select begin-end date
 
    col1,col2 = st.sidebar.columns(2)
    if days == '1M':
        start_date = col1.date_input("Start date", datetime.today().date() - timedelta(days=30))
    elif days == '3M':
        start_date = col1.date_input("Start date", datetime.today().date() - timedelta(days=90))
    elif days == '6M':
        start_date = col1.date_input("Start date", datetime.today().date() - timedelta(days=180))
    elif days == 'YTD':
        start_date = col1.date_input("Start date", datetime.today().date() - ytd.days)
    elif days == '1Y':
        start_date = col1.date_input("Start date", datetime.today().date() - timedelta(days=365)) 
    elif days == '3Y':
        start_date = col1.date_input("Start date", datetime.today().date() - timedelta(days=1095))  
    elif days == '5Y':
        start_date = col1.date_input("Start date", datetime.today().date() - timedelta(days=1825))  
    elif days == 'MAX':
        start_date =col1.date_input("Start date", datetime.today().date() - timedelta(days=365*70))
        
        
    end_date = col2.date_input("End date", datetime.today().date())
    
    # Add a check box
    show_data = st.checkbox("Show data")
    
    if ticker != '-':
       Qt = si.get_quote_table(ticker, dict_result = False)
       Qt = pd.DataFrame(Qt, columns=['attribute', 'value'])
       Qt=Qt.astype(str)
       if show_data:
            st.write('Summary')
            st.table(Qt)
        
    
    #if ticker != '-':
    stock_price = GetStockData([ticker], start_date, end_date)
        
        
    # Add a plot
    if ticker != '-':
        st.write('Adjusted close price')
        fig, ax = plt.subplots(figsize=(15, 5))
        for tick in [ticker]:
        
            plt.fill_between(stock_price.index,stock_price['close'],label=tick,color = "green", alpha = 0.87)
            ax.legend()
            st.pyplot(fig)

#==============================================================================
# Tab 2
#============================================================================================================================================================
# Initiating
#==============================================================================




def tab2():
    
    # Add dashboard title and description
    st.title("Financial dashboard-Yahoo Finance")
    st.write("Data source: Yahoo Finance")
    st.header('Chart')
    
    # Add table to show stock data
    @st.cache
    def GetStockData(tickers, start_date , end_date):
     return pd.concat([si.get_data(tick, start_date, end_date) for tick in tickers])
 
    Time_period = st.sidebar.selectbox('time', ['1M','3M','6M','YTD', '1Y', '3Y', '5Y','MAX'])
    yr = datetime.today().date().year
    dt1 = datetime.today().date()-datetime(yr, 1, 1).date()
   
    
    #Seperate columns
    
    col1,col2 = st.sidebar.columns(2)
    if Time_period== '1M':
        nd=30
    elif Time_period == '3M':
        nd = 90
    elif Time_period == '6M':
        nd = 180
    elif Time_period == 'YTD':
        nd= dt1.days
    elif Time_period == '1Y':
        nd = 365 
    elif Time_period == '3Y':
        nd = 1095  
    elif Time_period == '5Y':
        nd = 1825  
    elif Time_period == 'MAX':
        nd = 365*70
        
        
    start_date = col2.date_input("Start date", datetime.today().date() - timedelta(days=nd))    
    end_date = col2.date_input("End date", datetime.today().date())
    Plot = st.selectbox('Graph Type', ['Line', 'Candle stick Plot'])
    stock_price = GetStockData([ticker], start_date, end_date)
  
    # Add a line plot
    if ticker != '-':
        
        if Plot =='Line':# Line Plot
            st.set_option('deprecation.showPyplotGlobalUse', False)#Top avoid Assertion error
            st.pyplot(mpf.plot(stock_price,type='line'))
        else: #Box Plot
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(mpf.plot(stock_price,type='candle',mav=(3,6,9),volume=True))
            

def tab3():
    
     # Add dashboard title and description
    st.title("My simple financial dashboard")
    st.write("Data source: Yahoo Finance")
    st.header('Statistics')
    
    def GetStatsV(ticker):
        return si.get_stats_valuation(ticker)
    
    def GetStats(ticker):
        return si.get_stats(ticker)
    
    
    if ticker != '-':
        st1 = GetStatsV(ticker)
        st2 = GetStats(ticker)
        st.write('Statistics')
        st.dataframe(st1)
        st.dataframe(st2)  

def tab4():
    
     # Add dashboard title and description
    st.title("Financial dashboard-Yahoo Finance")
    st.write("Data source: Yahoo Finance")
    st.header('Financials')
    
    def GetFinancials(ticker):
        return si.get_financials(ticker, yearly = True, quarterly = True)
         
    
    Fin = st.sidebar.selectbox('Show', ['Income Statement','Balance Sheet','Cash flow'])
    Timeline = st.sidebar.selectbox('Period', ['Annual','Quarterly'])
    
  
        
    
    if ticker != '-':
        
       if Fin == 'Balance Sheet':
        if Timeline == 'Annual':
         yearly = GetFinancials(ticker)
         #yearly = yearly.astype(dict)
         st.write('Balance sheet-Annual')
         yearly["yearly_balance_sheet"]
         
        else:
         quarterly = GetFinancials(ticker)
         st.write('Balance sheet-Quarterly')
         quarterly["quarterly_balance_sheet"]
         
       if Fin == 'Income Statement':
        if Timeline == 'Annual':
         yearly = GetFinancials(ticker)
         #yearly = yearly.astype(dict)
         st.write('Income Statement-Annual')
         yearly["yearly_income_statement"]
         
        else:
         quarterly = GetFinancials(ticker)
         st.write('Income Statement-Quarterly')
         quarterly["quarterly_income_statement"]
         
       if Fin == 'Cash flow':
        if Timeline == 'Annual':
         yearly = GetFinancials(ticker)
         #yearly = yearly.astype(dict)
         st.write('Cash Flow-Annual')
         yearly["yearly_cash_flow"]
         
        else:
         quarterly = GetFinancials(ticker)
         st.write('Cash Flow-Quarterly')
         quarterly["quarterly_cash_flow"]
        
    
    




def tab5():
    
     # Add dashboard title and description
    st.title("Financial dashboard-Yahoo Finance")
    st.write("Data source: Yahoo Finance")
    st.header('Analysis')
    
    def GetAnalysisInfo(ticker):
        return si.get_analysts_info(ticker)
    

    
    
    if ticker != '-':
        GAI = GetAnalysisInfo(ticker)
        st.write('Analysis')
        st.table(GAI["Earnings Estimate"])
        st.table(GAI["Revenue Estimate"])
        st.table(GAI["Earnings History"])
        st.table(GAI["EPS Trend"])
        st.table(GAI["EPS Revisions"])
        st.table(GAI["Growth Estimates"])
     

def tab6():
     # Add dashboard title and description
    st.title("Financial dashboard-Yahoo Finance")
    st.write("Data source: Yahoo Finance")
    st.header('Monte Carlo Simulation')



    
    #Defining the function and checking for the Apple stock
    start_date = dt.datetime(2018, 1, 1)
    end_date = dt.datetime(2018, 11, 15)
    stock_price = web.DataReader('AAPL', 'yahoo', start_date, end_date)
    stock_price.tail()
    
    
    close_price = stock_price['Close']
    
    # The returns ((today price - yesterday price) / yesterday price)
    daily_return = close_price.pct_change()
    
    
    # The volatility (high value, high risk)
    daily_volatility = np.std(daily_return)
    daily_volatility
    
    
    # Take the last close price
    last_price = close_price[-1]
    
    # Generate the stock price of next 30 days
    time_horizon = 30
    next_price = []
    
    #time_horizon = (30,60,90)
    #n_simulation=(200,500,1000)
    th_days = st.sidebar.selectbox('Time horizon', ['30','60','90'])
    n_sim = st.sidebar.selectbox('Number of simulations', ['200','500','1000']) 
    if th_days == '30':
      time_horizon=30
    elif th_days == '60':
      time_horizon=60
    else: 
      time_horizon=90
    if n_sim == '200' :
      n_simulation = 200
    elif n_sim == '500':
      n_simulation= 500
    else: 
      n_simulation=1000
        
    
    if ticker != '-':  
        for n in range(time_horizon):
            
            # Generate the random percentage change around the mean (0) and std (daily_volatility)
            future_return = np.random.normal(0, daily_volatility)
            
            # Generate the random future price
            future_price = last_price * (1 + future_return)
            
            # Save the price and go next
            next_price.append(future_price)
            last_price = future_price
            
        print(next_price)
        
        # Setup the Monte Carlo simulation
        np.random.seed(123)
        n_simulation = 200
        time_horizone = 30
        
        # Run the simulation
        simulation_df = pd.DataFrame()
        
        for i in range(n_simulation):
            
            # The list to store the next stock price
            next_price = []
            
            # Create the next stock price
            last_price = close_price[-1]
            
            for j in range(time_horizone):
                # Generate the random percentage change around the mean (0) and std (daily_volatility)
                future_return = np.random.normal(0, daily_volatility)
        
                # Generate the random future price
                future_price = last_price * (1 + future_return)
        
                # Save the price and go next
                next_price.append(future_price)
                last_price = future_price
            
            # Store the result of the simulation
            simulation_df[i] = next_price
            
            
        # Plot the simulation stock price in the future
        fig, ax = plt.subplots()
        fig.set_size_inches(15, 10, forward=True)
        
        plt.plot(simulation_df)
        plt.title('Monte Carlo simulation for AAPL stock price in next 30 days')
        plt.xlabel('Day')
        plt.ylabel('Price')
        
        plt.axhline(y=close_price[-1], color='red')
        plt.legend(['Current stock price is: ' + str(np.round(close_price[-1], 2))])
        ax.get_legend().legendHandles[0].set_color('red')
        st.pyplot(fig)
        plt.show()
#==============================================================================
# Main body
#==============================================================================
  
def run():
    
    # Add the ticker selection on the sidebar
    # Get the list of stock tickers from S&P500
    global ticker
    ticker_list = ['-'] + si.tickers_sp500()
    ticker = st.sidebar.selectbox("Select a ticker", ticker_list)

  
    
    # Add a radio box
    select_tab = st.sidebar.radio("Select tab", ['Summary', 'Chart','Statistics','Financials','Analysis','Monte_Carlo_Simulation'])
    
    
    if select_tab == 'Summary':
        # Run tab 1
        tab1()
    elif select_tab == 'Chart':
        # Run tab 2
        tab2() 
    elif select_tab == 'Statistics':
        # Run tab 2
        tab3() 
    elif select_tab == 'Financials':
        # Run tab 2
        tab4()    
    elif select_tab == 'Analysis':
        # Run tab 2
        tab5()    
    elif select_tab == 'Monte_Carlo_Simulation':
        # Run tab 2
        tab6()    
        
    
  
if __name__ == "__main__":
    run()
    
###############################################################################
# END
###############################################################################
                     