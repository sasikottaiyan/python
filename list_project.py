import os
folders = input("enter the folder:").split()

for data in folders:

   try:
       files= os.listdir(data)
   except FileNotFoundError:
       print("enter a valid folder name")
       continue

   print("=== listing the files in " , data)
   
for dot in files:
   print(dot)