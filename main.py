# Python program to explain os.path.exists() method   
      
# importing os module   
import os  
    
# Specify path  
path = '/usr/local/bin/'
    
# Check whether the specified  
# path exists or not  
isExist = os.path.exists(path)  
print(isExist)  
    
    
# Specify path  
path = '/home/User/Desktop/file.txt'
    
# Check whether the specified  
# path exists or not  
isExist = os.path.exists(path)  
print(isExist)  

# credit to geeksforgeeks.com at
# https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/