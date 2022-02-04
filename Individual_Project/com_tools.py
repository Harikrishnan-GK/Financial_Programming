#==============================================================================
# Tab 1
#============================================================================================================================================================
# Initiating
#==============================================================================
#Importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score, r2_score, mean_absolute_error
import statsmodels.api as sm
from numpy                import random
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics      import auc
from sklearn.metrics      import roc_auc_score
from matplotlib           import pyplot
# calculate accuracy measures and confusion matrix
from sklearn import metrics
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import streamlit as st

from sklearn.inspection import PartialDependenceDisplay

def tab1():
    # Add dashboard title and description
    st.title("Telecommunication dashboard")
    
    st.header('Insights')
      #Reading data
    churn_df = pd.read_csv("churn_train.csv")
    # Let us look at the target column which is 'churn' to understand how the data is distributed amongst the various values
    churn_df.groupby(["churn"]).count()
    
    
    
    
    
    
#==============================================================================
# Main body
#==============================================================================
  
def run():
    
    # Add the ticker selection on the sidebar
    # Get the list of stock tickers from S&P500
    global churn
    #feature_list = ['-'] + si.tickers_sp500()
    #churn = st.sidebar.selectbox("Select a model", )

  
    
    # Add a radio box
    select_tab = st.sidebar.radio("Select tab", ['Insights', 'Models','Feature Selection','Analysis','Interpretation'])
    
    
    if select_tab == 'Insights':
        # Run tab 1
        tab1()
    elif select_tab == 'Models':
        # Run tab 2
        tab2() 
    elif select_tab == 'Feature Selection':
        # Run tab 2
        tab3() 
    elif select_tab == 'Analysis':
        # Run tab 2
        tab4()    
    elif select_tab == 'Interpretation':
        # Run tab 2
        tab5()    
       
        
    
  
if __name__ == "__main__":
    run()    
    