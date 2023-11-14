# import random

# price=450
# stroage_cost=50
# customer_cost=100
# loss =0
# profit_list=list()

# def get_random_number():
#     return random.uniform(0,1)

# def get_x():
#     prob= get_random_number()
#     if prob>=0 and prob<0.2:
#         x=0
#     elif prob>=0.2 and prob<0.6:
#         x=1
#     elif prob>=0.6 and prob<0.8:
#         x=2
#     elif prob>=0.8 and prob<0.9:
#         x=3
#     else:
#         x=4
#     return x


# for order in range(1,3):
#     avil_pc=0
#     for week in range(500):
#         x=get_x()
#         avil_pc += order
        
#         if x>avil_pc:
#             unstatisfied_customer= x - avil_pc
#             sold = avil_pc
#             avil_pc = 0
#             loss = unstatisfied_customer * customer_cost
        
#         elif x<avil_pc:
#             avil_pc -= x
#             sold = x
#             stored = avil_pc - x
#             loss = stored * stroage_cost
        
#         else:
#             loss = 0
#             avil_pc = 0
#             sold = x

#         profit = sold * price-loss
        
#         if profit >=0:
#             profit_list.append(profit)
    
#     if order==1:
#         average_profit_1=sum(profit_list)/500
#         profit_list.clear()
    
#     else:
#         average_profit_2=sum(profit_list)/500
#         profit_list.clear()


# print("average profit for order 1 is",average_profit_1,"\n")

# print("average profit for order 2 is",average_profit_2,"\n")

# if average_profit_1>average_profit_2:
#     print("order 1 is better")
# else:
#     print("order 2 is better")
import numpy as np

# Define the input vectors for class 1 and class 2
x1 = np.array([[0.8, 0.5, 0], [0.9, 0.7, 0.3], [1, 0.8, 0.5]])
x2 = np.array([[0, 0.2, 0.3], [0.2, 0.1, 1.3], [0.2, 0.7, 0.8]])

# Define the target outputs for class 1 and class 2
y1 = np.ones((x1.shape[0], 1))
y2 = -np.ones((x2.shape[0], 1))

# Combine the input vectors and target outputs
x = np.concatenate((x1, x2), axis=0)
y = np.concatenate((y1, y2), axis=0)

# Initialize the weight vector and bias
w = np.zeros((x.shape[1], 1))
b = 0

# Set the learning rate
c = 1

# Perform the training
for _ in range(100):  # Maximum of 100 iterations
    for i in range(x.shape[0]):
        if y[i] * (np.dot(w.T, x[i]) + b) <= 0:
            w += c * y[i] * x[i].reshape(w.shape)
            b += c * y[i]

print("Solution weight vector: ", w.flatten())
print("Bias: ", b)
