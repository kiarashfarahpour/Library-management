#lib
import os
import pickle

### path ###
PATH = "E:/kiarash/AI/libManegment/"

###  chek validation ###
def check_validation():
    if not os.path.exists(PATH + "user.dat"):
        f = open(PATH + "user.dat" , "wb")
        users_dict = {}
        pickle.dump(users_dict, f)
        f.close()
    
    if not os.path.exists(PATH + "books.dat"):
        f = open(PATH + "books.dat" , "wb")
        books_dict = {}
        pickle.dump(books_dict, f)
        f.close()    
    
    if not os.path.exists(PATH + "borrows.dat"):
        f = open(PATH + "borrows.dat" , "wb")
        borrows_dict = {}
        pickle.dump(borrows_dict, f)
        f.close()

#functions

### add users def ###
def add_users(name,family,father_name,natenality_code,birthday):
    check_validation()
    f = open(PATH + "user.dat" , "rb")
    users_dict = pickle.load(f)
    f.close()

    user_id = len(users_dict)
    users_dict[user_id] = [name, family, father_name, natenality_code, birthday]
    f = open(PATH + "user.dat" , "wb")
    pickle.dump(users_dict, f)
    f.close()

    print("welcom to our library..... your users ID:", user_id)

### add BOOKs def ###
def add_book(titel, auther, subject, year):
    check_validation()
    f = open(PATH + "books.dat" , "rb")
    books_dict = pickle.load(f) 
    f.close()

    books_dict = len(books_dict)
    books_dict[titel] = [auther, subject, year]
    f= open(PATH + "books.dat", "wb")
    pickle.dump(books_dict, f)
    f.close()

### search  Books def ### 
def search_book(titel):
    check_validation()
    f= open(PATH + "books.dat", "rb")
    books_dict = pickle.load(f)
    f.close()
    print(books_dict[titel])

### Barrow books def ###
def borrow(user_id, titel):
    check_validation()
    f = open(PATH + "borrows.dat" , "rb")
    borrows_dict = pickle.load(f)
    f.close()
   
    borrows_dict[user_id] = titel
    f = open(PATH + "borrows.dat" , "wb")
    pickle.dump(borrows_dict, f)
    f.close()

### show all info def ###
def show_all_info():
    check_validation()

    f = open(PATH + "books.dat" , "rb")
    users_dict = pickle.load(f)
    f.close()
    f = open(PATH + "books.dat" , "rb")
    books_dict = pickle.load(f) 
    f.close()
    f = open(PATH + "borrows.dat" , "rb")
    borrows_dict = pickle.load(f)
    f.close()

#start
ch = 1 
while ch != 0:
    print("1-Add User\n2-Add New Book\n3-Search\n4-Barrow\n5-Show\n0-Exit")
    ch = int(input("Enter Your Choice ! : "))
    if ch == 1:
        name = input("Enter Name :")
        family = input("Enter Family :")
        father_name = input("Enter Father Name :")
        natenality_code = input("Enter Natenality_code :")
        birthday = input("Enter Birthday :")
        add_users(name, family, father_name, natenality_code, birthday)

    elif ch == 2:
        titel = input("Enter Titel :")
        auther = input("Enter Auther :")
        subject = input("Enter Subject :")
        year = input("Enter Year :")
        add_book(titel, auther, subject, year)
    
    elif ch == 3:
        # check with title
        titel = input("Enter Titel :")
        search_book(titel)
    
    elif ch == 4:
        user_id = input("Enter User ID: ")
        titel = input ("Enter Titel :")
        borrow(user_id, titel)

    elif ch == 5:
        show_all_info()    