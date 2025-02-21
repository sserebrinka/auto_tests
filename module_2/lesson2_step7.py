import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

print(os.path.abspath(__file__)) # c:\Users\serebrinkaa\selenium_course\module_2\lesson2_step7.py
print(os.path.abspath(os.path.dirname(__file__))) # c:\Users\serebrinkaa\selenium_course\module_2
print(file_path) # c:\Users\serebrinkaa\selenium_course\module_2\file.txt