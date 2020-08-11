import pandas as pd
import numpy as np

#Data Quality Report using Python

#dataQuality() Returns a dictionary with two keys 'numeric' and 'categorical'
def dataQuality(data):
    d={}
    def numeric_quality(data):
        def q1(x):
            return x.quantile(0.25)
        def q3(x):
            return x.quantile(0.75)
        def q99(x):
            return x.quantile(0.99)
        def count(x):
            return x.count()
        def miss_per(x):
            return x.isnull().sum()/len(x)
        def unique(x):
            return len(x.unique())
        qr=dict()
        #Select only numeric data types
        data=data.select_dtypes(include=[np.number])
        for i in np.arange(0,len(data.columns),1):
            xi=data.agg({data.columns[i]:[count,unique,miss_per,np.min,np.max,np.mean,np.median,np.std,np.var,q1,q3,q99]})
            qr[data.columns[i]]=xi.reset_index(drop=True)[data.columns[i]]
            df1=pd.DataFrame(qr)
            #df1.index=xi.index
            df1.index=["Count","Unique","Miss_per","Min","Max","Mean","Median","Std","Var","Q1","Q3","q99"]
        return df1.T
    d['numeric']=numeric_quality(data)
    def cat_quality(data):
        def count(x):
            return x.count()
        def miss_per(x):
            return x.isnull().sum()/len(x)
        def unique(x):
            return len(x.unique())
        def freq_cat(x):
            return x.value_counts().sort_values(ascending=False).index[0]
        def freq_cat_per(x):
            return x.value_counts().sort_values(ascending=False)[0]/len(x)
        qr=dict()
        data=data.select_dtypes(include=[object])
        for i in np.arange(0,len(data.columns),1):
            xi=data.agg({data.columns[i]:[count,unique,miss_per,freq_cat,freq_cat_per]})
            qr[data.columns[i]]=xi.reset_index(drop=True)[data.columns[i]]
            df2=pd.DataFrame(qr)
            #df2.index=xi.index
            df2.index=["Count","Unique","Miss_per","Freq_Level","freq_cat_Per"]
        return df2.T
    d['categorical']=cat_quality(data)
    return d