#snake and ladder
import random
a=random.randint(1,6)
count=0
while(count<=100):
 a=random.randint(1,6)
 if (count>=94):
  if (count+a==100):
      print ("you won the game")
      break
  if (a<=100-count):
    count=count+a
    print (count)
 else:  
     count=count+a
     print (count)
     if count==8:
         print ("you may climb the ladder")
         count=37
     elif count==38:
         print ("you may come down the snake")
         count=9
     elif count==11:
         print ("you may come down the snake")
         count=2
     elif count==25:
         print ("you may come down the snake")
         count=4
     elif count==13:
         print ("you may climb the ladder")
         count=34
     elif count==40:
         print ("you may climb the ladder")
         count=68
     elif count==93:
         print ("you may come down the snake")
         count=64
     elif count==65:
         print ("you may come down the snake")
         count=46
     elif count==52:
         print ("you may climb up the ladder")
         count=81
     elif count==89:
         print ("you may come down the snake")
         count=70
     elif count==76:
         print ("you may climb the ladder")
         count=97
     
         
     
     
    


    

