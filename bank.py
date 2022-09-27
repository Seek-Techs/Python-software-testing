"""
This assessment is to test your knowlegde of python dictionaries and functions and a lot more

- I used some advanced string formating in the code below, check them out on google to understand how the work and try to use them in your code some other time
- This code is a demo bank application
- The dictionary stores users and bank officials information like password and users account balance
- You need to understand how the dictionary is structured before attempting to debug this code
- The code below checks if the a user is logging in with the right information/details
- And shows the user balance
- A bank official can also login
 
 +++ Hint 
 Run the code first before attempting to debug 
Happy coding and debugging !!!

"""
print("""
                        ░░░░                      
                    ░░░░  ░░░░                    
                    ░░░░░░░░░░                    
                        ░░░░                      
                                                  
          ▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  
          ▒▒░░▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒              
          ▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒            
        ▒▒░░░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒            
        ▒▒░░██░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
    ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒        
    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒  ▒▒    
    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒      
      ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
        ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
          ▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒            
            ▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒              
            ▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒              
            ▒▒▒▒▒▒            ▒▒▒▒▒▒              
                                                  
                                                  
██████████████████████████████████████████████████
""")
bank_model = {
    "officials" : {
        # you can choose to change name afterwards
        0 : {
            "name" : "Danile Vanek",
            "password": "dv000"
        } ,
        1 : {
            "name" : "Donald Dorcas",
            "password": "dd001"
        }
    },
    "customers":{
        "0123456789" : {
            "account_type": "current",
            "account_name": "John Kennedy",
            "balance": 250,
            "password" : "jk002"
        },
        "0444456789" : {
            "account_type": "current",
            "account_name": "richard james",
            "balance": 1250,
            "password" : "rj003"
        },
    }
}

def login():
    print("Welcome to TEEKAY Bank")
    user = int(input("Log in as a bank 0fficial or a bank user? Enter 1. for official 2. for user "))

    if user == 1 :
        id = int(input("Enter your official id: "))
        password = input("Enter your official password: ")

        if password ==  bank_model["officials"][id]["password"]: 
            msg = "Welcome back %s " % (bank_model["officials"][id]["name"])
            print(msg)

        elif password !=  bank_model["offiials"][id]["password"]:

            print("password or id is invalid!!")
            login()
    else:
        id = input("Enter your account number: ")
        password = input("Enter your account password: ")
    
        if password ==  bank_model["customers"][id]["password"] :
            msg = "Welcome back %s\n Your current balance: $%s" % (bank_model["customers"][id]["account_name"], bank_model['customers'][id]["balance"])
            print(msg)

        elif password !=  bank_model["customers"][id]["password"]:
            print("password or id is invalid!!")
            login()

login()
