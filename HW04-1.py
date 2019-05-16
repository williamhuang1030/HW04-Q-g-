import pandas as pd 
import numpy as np
df_n= pd.read_csv(r"C:\Users\User\Desktop\0320\ETF\HW01-all.csv")  
name=df_n['Symbol'].tolist()
name.remove('XRT')
name.remove('PRN')
name.append('_PRN')
for n in name:
    df = pd.read_csv("C:\\Users\\User\\Desktop\\0320\\ETF\\"+str(n)+".csv")  
    x = (df['Close']/df['Close'].shift(5))- 1.0
    x
    y = (df['Close']/df['Close'].shift(20))- 1.0
    lx=len(x)
    ly=len(y)
    A=[]
    B=[]
    for i in range(5,lx):
        A.append(x[i])
    for i in range(20,ly):
        B.append(y[i])
    df['return_week']=pd.Series(A)
    df['return_month']=pd.Series(B)
    df.to_csv("C:\\Users\\User\\Desktop\\skew\\ETF\\"+str(n)+".csv")
def newt(alphag):
    l=len(rwe)
    expt=list(map(lambda x :math.exp(-x*alphag),rwe))
    ans=np.mean(expt)
    return(ans)
name_w=[]
name_m=[]
ans_w=[]
ans_m=[]
import math
for no in name:
    df = pd.read_csv("C:\\Users\\User\\Desktop\\skew\\ETF\\"+str(no)+".csv")
    rw=df['return_month']
    rwe=rw.dropna().tolist()
    x = 100
    h = 0.1**(6)
    xh=x+h
    n=1000
    for i in range(n):
        f = newt(x) - 1          
        if f **2 > 0.1** (12):
            xh=x+h
            x = x - f / (((newt(xh) - newt(x)) / h)) 
    name_m.append(no)
    ans_m.append(x)
for no in name:
    df = pd.read_csv("C:\\Users\\User\\Desktop\\skew\\ETF\\"+str(no)+".csv")
    rw=df['return_week']
    rwe=rw.dropna().tolist()
    x = 100
    h = 0.1**(6)
    xh=x+h
    n=1000
    for i in range(n):
        f = newt(x) - 1          
        if f **2 > 0.1** (12):
            xh=x+h
            x = x - f / (((newt(xh) - newt(x)) / h)) 
    
    name_w.append(no)
    ans_w.append(x)

month={'name':name_m,'alpha':ans_m}
month=pd.DataFrame(month)
month.to_csv("C:\\Users\\User\\Desktop\\month_alpha1.csv")


week={'name':name_w,'alpha':ans_w}
week=pd.DataFrame(week)
week.to_csv("C:\\Users\\User\\Desktop\\week_alpha1.csv")



month_list=pd.read_csv("C:\\Users\\User\\Desktop\\month_alpha.csv")
week_list=pd.read_csv("C:\\Users\\User\\Desktop\\week_alpha.csv")
rank_month=month_list['name']
rank_week=week_list['name']
rank_month
rank_week
