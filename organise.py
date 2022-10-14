import os
import shutil

from_dir = "C:/Users/HP/Downloads/pic"
to_dir = "D:/images"
list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    # print(name)
   # print(extension)
    if extension == '':
       continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfiif']:
       path1 = from_dir + '/' + file_name
       path2 = to_dir + '/' + "Rohan"
       path3 = to_dir + '/' + "Rohan" + '/' + file_name
     #  print("path1",path1)
    print("path2",path1)
     print("path3",path1)
    
       if os.path.exists(path2):
          print("moving" + file_name + "...")
          shutil.move(path1, path3) 
       else:
           os.makedirs(path2)
           print("moving" + file_name + "...")
           shutil.move(path1, path3)