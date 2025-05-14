''' 
Python Assignment
Functions 
'''
#--------- EASY --------
#Q1
def calculate_average (nums=0) :
    sum = 0
    count = 0
    for n in nums :
        sum += n
        count += 1
    if count == 0 :
        return 0
    else :
        return sum/count 
#Q2   
def greet_user(name, greeting = "Hello") :
    return greeting +", "+ name + " !"


#--------- MEDIUM --------
#Q1
def calculate_total (*prices, discounts=0) :
    sum = 0
    price_list = list(prices)
    for p in price_list:
        sum += p
    final = sum - ((sum * discounts)/100)
    return final
#Q2
def create_multiplier(number): # ye factory-function hai
    def multiply(value): # ye working function hai
        return value * number
    return multiply


#--------- HARD --------
#Q1
def power (x,n):
    if n==0:
        return 1
    half = power(x,n//2)
    if half/2 ==0:
        return half*half
    else:
        return x*half*half
    
#Q2
def compose(f1,f2,f3):
    def combine(x):
        return f1(f2(f3(x)))
    return combine
    
#---------------------------
#   Test Cases - outputs
#---------------------------
if __name__ == "__main__" :
    #easy
    print("Easy")
    print(calculate_average([10,20,30,40,50,60,70,80]))
    print(calculate_average([]))

    greet_user("Priyesh")
    greet_user("Pravin","Namaste")


    #medium
    print("Medium")
    print(calculate_total(213,42,547,897,85,73))
    print(calculate_total(21,100,34,10,50))

    quadruple = create_multiplier(4)
    print(quadruple(6))  # Output: 24


    #hard
#Q1
    print("Hard")
    print(power(10,0))
    print(power(1,100))
    print(power(2,5))
    print(power(7,10))
#Q2
    def add_one(x): return x + 1
    def double(x): return x * 2
    def square(x): return x ** 2
    
    f = compose(square, double, add_one)
    print(f(3))