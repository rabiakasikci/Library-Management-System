# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:00:32 2024

@author: Rabia KAŞIKCI
"""
import time

class Library:
    
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")
        
    def __del__(self):
        self.file.close()
    """      
    In this function, the books in the file are listed.
    If there is no book in the file, it notifies you.
    """

    def Lists_Books(self):
        self.file.seek(0)
        all_lines=self.file.read().splitlines()
        
        if not all_lines:
            print("There is no book")
        else:
            for i in all_lines:
                print(i)
                
    """      
    With this function, you can add any book you want to the file.
    However, if the book you want to add is already in the file, you cannot add it.
    """ 
            
  
    def Add_Books(self):
        
        
        name = input('Enter name of Book:')
        writer = input('Enter name of writer:')
        
        
        add_lines=str(name+","+writer)
        
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        
        for lines in book_lines:
            a=str(lines.split(",")[0])+","+str(lines.split(",")[1])
            
            if add_lines in  a:
                print("This book already exists.Please try another books")
                self.Add_Books()
                return 
            
        date = input('Enter date of release:')
        if not date.isdigit():
            date = input("Please enter a valid date")
        
        page = input('Enter number of pages:')
        if not page.isdigit():
            page = input("Please enter a valid page number")
        add_lines=str(name+","+writer+","+date+","+page)
        self.file.seek(0, 2)
        self.file.write(str(add_lines+"\n"))
    
    """      
    You can also delete any book you want in the file with the Remove Book Function.
    If there is a book name you want to remove, you must also enter the author name.
    In addition, the book you want to delete from the file must be in the file. 
    Otherwise you will receive a warning.
    """  
         
        
    def Remove_Books(self):
        remove = input("Enter the title of the book that you want to remove: ")

        self.file.seek(0)
        book_lines=self.file.read().splitlines()

        
        count = 0
        for line in book_lines:
            if remove == line.split(",")[0]:
                count += 1
        
        

        new_lines = []
        if count == 0:
            
            print("This book does not exist.")
            for line in book_lines:
                new_lines.append(line)
            
            
        elif count > 1:
            print("There is more than one book with this name")
            remove_writer = input("Please enter the writer of the book that you want to remove: ")
            
            for line in book_lines:
                if remove_writer != line.split(",")[1] :
                    new_lines.append(line)
            print(f"{remove} from  {remove_writer} removed successfully.")
            
        else:
            
            for line in book_lines:
                if remove !=  line.split(",")[0]  :
                    new_lines.append(line)
            print(f"{remove} removed successfully.")
            

        self.file.seek(0)
        self.file.truncate(0)  # Clear the file contents
        
        for i in new_lines:
            self.file.write(str(i) + '\n')
    


        
        
        
        

        
    
    

    

        
lib=Library()


while True:
    print("*** MENU*** " + "\n"
          + "1) List Books" + "\n"
          + "2) Add Book" + "\n"
          + "3) Remove Book" + "\n"
          + "Q=QUIT")
    print('Enter your choice:')
    x = input()

    if x == '1':
        
        lib.Lists_Books()
    elif x == '2':
        
        lib.Add_Books()
    elif x == '3':
        
        lib.Remove_Books()
    elif x.upper() == 'Q' or x == 'Q':
        
        break
    else:
        print("Please choise a valid option.")
    time.sleep(1)
