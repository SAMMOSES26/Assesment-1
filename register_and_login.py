import re

#<-----------choices for register and login ------------->

def choices():
    while True:
        choice = int(input("For Register press 1 \n\nFor Login press 2\n\nEnter: "))
        if choice == 1:
            return register()
        elif choice == 2:
            return login()
        else:
            print("--------------------------------------Please Enter Valid Number--------------------------------------")

#<-----------choices for register and forget_password ------------->            

def reg_forget():
    while True:
        choice = int(input("For Register press 1 \n\nForget password press 2\n\nEnter: "))
        if choice == 1:
            return register()
        elif choice == 2:
            return forget_password()
        else:
            print("--------------------------------------Please Enter Valid Number--------------------------------------")

#<--------------------stage 1 Regsiter----------------->

def register():
    while True:
        special_characters = '!@#$%^&*()_+{}:"<>?-=[];\',./'
        email = input("Enter your email : ")
        flag = 0


        for each in special_characters:
            if each == email[0]:
                print("Email should not starts with symbol")
                print("Please enter in correct formate")
                register()
                flag = 1
        if re.search("@", email) is None:
            print("@ not found")

        d = re.findall("^\d", email)
        if d != []:
            print("Email should not starts with numbers")
            flag = 1
        a = re.findall('.+@\.[a-z]', email)
        if a != []:
            print("there should not '.' after @")
            flag = 1
        # z = re.findall('.+@.+[a-z]', email)
        # if z != []:
        #     print("there should not '.' after @")
        #     flag = 1
        if flag == 0:
            l = re.findall(".+@.+\.[a-z].+", email)
            if l != []:
                # print(*l)
                # print("Email Valid")

# <------------------------------------------pass validation -------------------------------------->

                while True:
                    password = input("Enter your password: ")

                    if len(password) < 5:
                        print("Make sure your password is at greater than 5 letters")
                    elif len(password) > 16:
                        print("Make sure your password is at greater than 5 letters")
                    elif re.search('[0-9]', password) is None:
                        print("Make sure your password has a numbers in it")
                    elif re.search('[A-Z]', password) is None:
                        print("Make sure your password has atleast one capital letter in it")
                    elif re.search('[a-z]', password) is None:
                        print("Make sure your password has atleast one small letter in it")
                    else:
                        print()
                        print("--------------------------------------Succefully Registered--------------------------------------")
                        print()
                        file = open('sam.txt', 'a')
                        file.write(email + "," + password + "\n")
                        # file.write("Password - " )
                        file.close()
                        choices()
        else:
                    print("Please enter in correct formate")

                
#<---------------------------------stage-2 Login-------------------------------------->

def login():
    while True:
        flag = 0
        file = open('sam.txt', 'r')
        name = input("Enter Email: ")
        password = input("Enter password: ")
        for line in file:
            file_name, file_password = line.split(',')
            file_password = file_password.strip()
            if (name!=file_name and password!=file_password):
                flag=1
            elif (name == file_name and password == file_password):
                flag=2
                break
        file.close()
        if (flag==1):
            print("--------------------invalid username | password----------")
            reg_forget()
        if (flag==2):
            print("--------------------Login success----------------")
            choices()
        else:
            print("--------------------please register---------------")
            choices()

#<----------------------------------------stage-3 forget_password--------------------------------------------------->

def forget_password():
    while True:
        flag = 0
        file = open('sam.txt', 'r')
        email = input("Enter Your Email: ")
        # password = input("Enter password: ")
        for line in file:
            file_email, file_password = line.split(',')

            if email != file_email:
                flag = 1
            elif (email == file_email):
                flag = 2
                break
        file.close()
        if (flag == 1):
            print("-----------------User does not exits-----------------")
        if flag == 2:
            while True:
                reset_password = input("Enter The New Password: ")
                if len(reset_password) < 5:
                    print("Make sure your password is at greater than 5 letters")
                elif len(reset_password) > 16:
                    print("Make sure your password is at greater than 5 letters")
                elif re.search('[0-9]', reset_password) is None:
                    print("Make sure your password has a numbers in it")
                elif re.search('[A-Z]', reset_password) is None:
                    print("Make sure your password has atleast one capital letter in it")
                elif re.search('[a-z]', reset_password) is None:
                    print("Make sure your password has atleast one small letter in it")
                else:
                    file = open("sam.txt", 'a')
                    file.write(email + "," + reset_password + "\n")
                    # file.write(email + "," + password + "\n")
                    file.close()
                    print("--------------Password Successfully Updated--------------------")
                    choices()



        else:
            print("---------------please register----------------")


choices()
