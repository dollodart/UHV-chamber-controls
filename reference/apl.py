import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('elem_aes.csv',delimiter=',')
l=range(len(df))
plt.figure()
df=df.sort_values(by='Peak')
plt.plot(l,df['Peak'])

#this code was written somewhere else, but I can't find it
def find_peak(E):
    df=pd.read_csv('elem_aes.csv',delimiter=',')
    df['ediff']=abs(df['Peak']-E)
    df=df.sort_values(by='ediff')
    print(df[['Element','ediff']].iloc[0:10])
find_peak(132.)

plt.show()
