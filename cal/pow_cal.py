import csv
import scipy.stats
tl=[]
cl=[]
vl=[]
rl=[]
pl=[]

with open('pow_dat.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        t,c,v,r,p=line
        tl.append(float(t))
        cl.append(float(c))
        vl.append(float(v))
        rl.append(float(r))
        pl.append(float(p))
print(pl,tl)
slope,intercept,rval,pval,std_dev=scipy.stats.linregress(pl,tl)
#intercept should be at room temperature, which is 30 deg C
print(slope,intercept)
