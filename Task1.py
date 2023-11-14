import random
import numpy as np
import matplotlib.pyplot as plt


selling_price = 249
administrative_cost = 400000
advertising_cost  = 600000
fixed_cost = advertising_cost + administrative_cost

mean = 15000
standard_div=4500

max_profit=0
min_profit=0
avg_profit=0
loss_count=0
n=500

def get_c1(r1):
    if(r1>=0 and r1<0.1):
        c1=43
    elif(r1>=0.1 and r1<0.3):
        c1=44                               
    elif(r1>=0.3 and r1<0.7):
        c1=45
    elif(r1>=0.7 and r1<0.9):
        c1=46
    else :
        c1=47
    return c1

def get_c2():
    c2=random.uniform(80,100)
    return c2

def get_x():
    x=np.random.normal(mean,standard_div)
    return x

c1List=list()

c2List=list()

profitList=list()

demandList=list()

for i in range(0,n):
    r1=random.uniform(0,1)
    c1=get_c1(r1)
    c1List.append(c1)
    c2=get_c2()
    c2List.append(c2)
    x=get_x()
    demandList.append(x)
    profit=((selling_price-c1-c2)*x)-fixed_cost
    if(profit<0):
        loss_count+=1
    else:
        profitList.append(profit)
    max_profit=max(profit,max_profit)
    min_profit=min(profit,min_profit)

avg_profit=sum(profitList)/len(profitList)

print("Maximum Profit = ",max_profit,"\n")
print("Minimum Profit = ",min_profit,"\n")
print("Average Profit = ",avg_profit,"\n")
print("Probability of Loss = ",loss_count/n,"\n")


plt.hist(profitList, density=True, bins=15)
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.title('Histogram of Profit')
plt.show()

plt.hist(c1List, density=True, bins=15)
plt.xlabel('c1')
plt.ylabel('Frequency')
plt.title('Histogram of c1')
plt.show()

plt.hist(c2List, density=True, bins=15)
plt.xlabel('c2')
plt.ylabel('Frequency')
plt.title('Histogram of c2')
plt.show()

plt.hist(demandList, density=True, bins=15)
plt.xlabel('Demand')
plt.ylabel('Frequency')
plt.title('Histogram of Demand')
plt.show()


