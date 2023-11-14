import random

price=450
stroage_cost=50
customer_cost=100
loss =0
profit_list=list()

def get_random_number():
    return random.uniform(0,1)

def get_x():
    prob= get_random_number()
    if prob>=0 and prob<0.2:
        x=0
    elif prob>=0.2 and prob<0.6:
        x=1
    elif prob>=0.6 and prob<0.8:
        x=2
    elif prob>=0.8 and prob<0.9:
        x=3
    else:
        x=4
    return x


for order in range(1,3):
    avil_pc=0
    for week in range(500):
        x=get_x()
        avil_pc += order
        
        if x>avil_pc:
            unstatisfied_customer= x - avil_pc
            sold = avil_pc
            avil_pc = 0
            loss = unstatisfied_customer * customer_cost
        
        elif x<avil_pc:
            avil_pc -= x
            sold = x
            stored = avil_pc - x
            loss = stored * stroage_cost
        
        else:
            loss = 0
            avil_pc = 0
            sold = x

        profit = sold * price-loss
        
        if profit >=0:
            profit_list.append(profit)
    
    if order==1:
        average_profit_1=sum(profit_list)/500
        profit_list.clear()
    
    else:
        average_profit_2=sum(profit_list)/500
        profit_list.clear()


print("average profit for order 1 is",average_profit_1,"\n")

print("average profit for order 2 is",average_profit_2,"\n")

if average_profit_1>average_profit_2:
    print("order 1 is better")
else:
    print("order 2 is better")

