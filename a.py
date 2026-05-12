#CHATBOT
import datetime
def chatbot():
    name=input("Enter the name:")
    print(f"Welcome {name}")
    memory={}
    while True:
        user=input("You:").lower()
        if "hi" in user or "hello" in user:
            print(f"Bot : Welcome {name}")
        elif "calculator" in user:
            exp=input("Enter the expression:")
            print(f"Bot:The value for expression is :",eval(exp))
        elif "age" in user:
            if "my age" in user:
                if "age" in memory:
                    print(f"You are {memory['age']} years old:")
                else:
                    print("You have not entered age")
            else:
                age=input("Enter the age:")
                memory['age']=age
                print("age saved")

        elif "sad" in user:
            print("Don't be sad")
        elif "datetime" in user:
            print("Datetime:",datetime.datetime.now())

        elif "bye" in user:
            print("Goodye")
            break
        else:
            print("I dont understand")
chatbot()            
