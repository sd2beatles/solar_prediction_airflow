import pandas as pd
import re


def extract_stamp(date):
    #extract relevant date information
    date=re.search("fmt:'?([0-9]{,4})'?\s*mft:'?([0-9]{,2})'?\s*dft:'?([0-9]{,2})'?\s*T([\d]{,2}:[\d]{,2}:[\d]{,2})",date).groups()
    stamp='-'.join(date[:3])+' '+date[3]
    if not stamp:
        return None
    return stamp

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



def interpolation(df,col,method="linear"):
    new_df=pd.DataFrame()
    new_df[col]=pd.date_range(start=df[col].iloc[0],end=df[col].iloc[-1],\
        freq='H')
    new_df[col]=new_df[col].astype(str)
    new_df=pd.merge(new_df,df,on=col,how='outer')
   
    return new_df.interpolate()


def weather_preprocess(**context):
    #obtain weather_pre
    df=pd.read_csv(context['params']['start_path'])
    
    #create two columns
    df['Forecast_Time']=df.apply(lambda x:extract_stamp(x['locdatetime']),axis=1)
    
    #interporlate
    #the weather forecast is made on every other hour.Our enegry record is made
    #on hour basis. To deal with the mismatch in values between the two tables,
    #we will run a simple linear interpolation method. 
    df=interpolation(df=df,col="Forecast_Time")
    
    #save the preprocessed_file
    df.to_csv(context['params']['dest_path'])
    
    
def angle_to_float(angle):
    angle = angle.split('˚')
    angle = int(angle[0]) + int(angle[1].split('´')[0])*0.01
    return angle
     

def geography_preprocess(**context):
    #obtain weather_pre
    df=pd.read_csv(context['params']['start_path'])
    exclude=["Unnamed: 0","locdate","location","updated_date"]
    columns=[col for col in df.columns if col.strip() not in exclude]
    
    print(columns)
    #change angle to numerica values
    for col in columns:
        df[col]=df[col].map(angle_to_float)
    
    #save the preprocessed_file
    df.to_csv(context['params']['dest_path'])
    

def energy_preprocess(**context):
    energy=pd.read_csv(context['params']['start_path'])
    
    energy["year_date"]=energy["Forecast_Time"].map(lambda x:str(x).split(" ")[0])
    group_sum=energy.groupby("year_date")["energy"].sum()
    #identify index whose total sum is zero
    _zero_energy=group_sum[group_sum<=0].index
    
    #delete any correspoding records
    energy=energy[~energy.year_date.isin(_zero_energy)]
    
    energy.to_csv(context['params']['dest_path'])

