import time




level =input(" ")
if level.lower() == "m":

  time.sleep(1)
  print("""
   RULES !!!
     
    > TYPE A , B , C , D FOR YOUR ANSWER AND PRESS ENTER 
    
    """)

  print("""WELCOME TO THE MEDIUM LEVEL
    
    """)
    
     
  print("""Q1.WHAT IS THE FULL FORM OF CPU ??
      
     
      
      """)   
    
  for i in range (10 , 0 , -1):
    print("time left:- ",i,end="\r")
    time.sleep(1)
    question = input(" ")
    
     
    
    if question.lower() == "b":
        print(""" YES!! , YOUR ANSWER IS CORRECT 
        THE FULL FORM OF CPU IS CENTRAL PROCESSING UNIT
        
        """)
        break
        
    
  else:
        print("""SORRY, YOUR ANSWER IS WRONG.
        THE FULL FORM OF CPU IS CENTRAL PROCESSING UNIT 
        
        """)
  
  
print("worked")
    

  
  
  
    
 