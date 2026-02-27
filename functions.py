# basic fx definations


mood = input("How are you?: ")
def greet():
    print("good morning sir,")
    if mood in {"fine", "good", "happy", "ok"}:
        print("glad to hear that")
    else:
        print("tell me how can i help to fix that, gentleman")
        
        
# calling fx multiple times

def say_goodbye():
    print("good bye, sir!")
say_goodbye()
say_goodbye()
say_goodbye()


# if else statements 

def check_weather():
    temp = 13
    if temp > 14:
        print("its pretty cold tbh")
    else:
        print("its pretty hot tbh")
        
check_weather()        

        
# multiple parameters in fx to make them dynamics and not harc coded
name = input("what is you name nigger: ")
def greet(name):
    print(f"hello, {name}")       
greet(name)

def age(lastname, firstname):
    print(f"firstname={firstname}, lastname={lastname}")
    #here the variable has to come at first in paramter else it would make error 
age(lastname="john")


#local and global varibales as in var. in fx and in global code
price = int(input("inter your amount: "))
def smp_int(price):
    interest = 10
    time = 1 # year
    simple_int = (interest * time * price)/100
    print(smp_int)
smp_int(price)
#interest time are unknow as they are not global var and instead in a fx making them local to the fx means local var and can be repeated in other fx 
#but doesnt work with global var making it uni directional fact

#return statement
def add_print(a,b):
    print(a+b)
add_print(a=5, b = 13)
print_result = add_print(a=5, b= 13) #this wont give anything in compiler as result
# with print you cannot do anything with the information and keep it static but with return fx

def add_return(a,b):
    return a+b
result = add_return(a=5, b=13)
#making result as useable var. in the code 

#example of return statement 
def clac_area(l,b):
    area = l*b
    area = area * 1.05
    return area
room_area = clac_area(l =3, b=12)
print= (f"room size: {room_area} m^2")   

total_area_house = clac_area(2,5) + clac_area(5,2) + clac_area(4,3)

def fx():
    num= [1,2,3,4]
    first_num = num[0]
    last_num= num[-1]
    return first_num , last_num
f,l = fx() # we can call first_num, last_num as f,l or anything and use them respective
print=(f)
print=(l)






 
    
    
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        