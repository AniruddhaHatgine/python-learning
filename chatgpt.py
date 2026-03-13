import time

def chatgpt(query):
    if query == "Hi":
        print("Hello, How can I help you today!")
    elif query == "Good Morning":
        print("Very Good Morning")
    elif query == "Jevan jal ka":
        thinking()
        print("Nahi jal")
    else:
        print("Good Night")
        
        
def thinking():
    print("Thinking...")
    time.sleep(20)
    
        
counter = 0  #initi

while counter<10:
    query_by_user = input("Chat: ")
    chatgpt(query_by_user)
    counter = counter + 1
