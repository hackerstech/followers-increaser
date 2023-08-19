import sys 
import time
import os
user_name=str(sys.argv[1])
password=str(sys.argv[2])
s=[460563723,26669533,7719696,247944034,173560420,18428658,6380930,232192182,12281817,305701719,427553890,12331195,325734299,212742998,407964088,7555881,177402262,19596899,181306552,1506607755,184692323]                     
from instagram_private_api import *
  	     		   
api = Client(user_name, password)
print("\033[32m [•] login successful ")
  

 		  
  

while True:
                  
    for l in s:
        print("\n \033[1;33m following celegrams ....\033[0m")
        time.sleep(3)
        api.friendships_create(l)
       
         	 	    
        print("wait for 60 sec dont exit")
                	         		                                             
    time.sleep(70)
    api = Client(user_name, password)
    for i in s :
        api.friendships_destroy(i)
        time.sleep(3)


    
