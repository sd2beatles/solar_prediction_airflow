import pandas as pd
import re


def extract_stamp(date1,time):
    #extract relevant date information
    date=re.search("yft:'([0-9]{4})'\s*mft:'([0-9]{,2})'\s*dft:'([0-9]{,2})'",date1.strip()).groups()
    time=time[1:]
    
    return '-'.join(date)+' '+time


def interpolation(df,method="linear"):
    new_df=pd.DataFrame()
    new_df['Forecast_Time']=pd.date_range(start=df['Forecast_Time'].iloc[0],end=df['Forecast_Time'].iloc[-1],
                                     freq='H')
    new_df=pd.merge(new_df,df,on="Forecast_Time",how="outer")
    new_df["Forecast_Time"]=new_df["Forecast_Time"].astype(str)
    return new_df.interpolate()
   
   
 
def column_preprocessing(function):
    def inner_function(data):
        column_names=['dangjin',"super"]
        cols=list(data.columns.isin(column_names))
        if max(cols):
            col=cols.index(True)
            data.rename({col:"energy"},inplace=True)
        return function(data)
    return inner_function

            
@column_preprocessing
def preproces_energy(df):
    df["year_date"]=df["year_date"]=df["Forecast_Time"].map(lambda x:str(x).split(" ")[0])
    group_sum=df.groupby("year_date")["energy"].sum()
    #identify index whose total sum is zero
    _zero_energy=group_sum[group_sum<=0].index
    #drop any corresponding records
    df=df[~df.year_date.isin(_zero_energy)]
    return df 


