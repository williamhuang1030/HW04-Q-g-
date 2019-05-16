import pandas as pd
data_m=pd.read_csv("C:\\Users\\User\\Desktop\\month_alpha1.csv")
data_w=pd.read_csv("C:\\Users\\User\\Desktop\\week_alpha1.csv")
etf_m=data_m['name'].tolist()
etf_w=data_w['name'].tolist()
rank=[]
for i in range(1,len(etf)+1):
    rank.append(i)
df_month=pd.DataFrame({'Rank':rank,'Symbol':etf_m})
df_week=pd.DataFrame({'Rank':rank,'Symbol':etf_w})

df_month
df_week
    