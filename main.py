import os

if __name__ == '__main__':
    
    while True:
        text = input("Enter whatever you want to say!")
        if text == "bye":
            os.system("say 'Bye Bye friend'")
            break
        
        command = f"say {text}"
        os.system(command)
        