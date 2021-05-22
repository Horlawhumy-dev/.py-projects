
                                                                                        #  ... Programmed  By Ibiyemi Opeyemi...

#greetings
name = input ("Please enter your name (e.g Seun) :  ")
   
print (" Hello, " +  name + " you are welcome.")            #print used to give output to user 

#getting information about institution
Name_of_inst = input (" Enter the name of institution:  ")
if (Name_of_inst == "OAU" or Name_of_inst == "Oau" or Name_of_inst == "oau" or
    Name_of_inst == "Obafemi Awolowo University" or Name_of_inst == " obafemi awolowo university" or
    Name_of_inst == "OBAFEMI AWOLOWO UNIVERSITY"):
    
    print ("Great! you are good to go")
    print ("Now answer the following questions")

    #getting student's information
    full_name = input ("enter your full name: ")
    Faculty = input ("enter your faculty: ")
    Dpt = input ("Your Department: ")
    mat_number = input ("Enter your matric Number: ")
    print ("Now Enter Your Date of birth")
    year = input ("Enter your year of birth. (e.g 1990):  ")
    month = input ("Enter your month of Birth:  ")
    Day = input ("Enter your birthday. (e.g 27th): ")
    current_year = input ("enter current year: ")

    # Guessing the users department and Faculty
    

                                                                                                        # ... Programmed By STEIN


    #reply if user entered an incorrect Current year...
    if int(current_year)  !=  2019 :
        print ("You have entered an invalid current year, Try again...")
        current_year = input ("enter current year: ")
    
    #calculating age
    age = int(current_year) - int(year)     # strings converted to itntegers before calculation with the prefix "int".

    print( full_name + " do you know you are " + str(age) + " years old now ?")  # integer is converted to string with the prefix "str"

    # age in the next 100 years
    age_in_100 = (int(age) + 100)    # string converted to integer before calculation.

    quest = input ("Do you also know in the next One Hundred years you will be " + str(age_in_100) + " years old ?: [Y/N] :    ")           # asked if user knows his/her age.

    if quest == "Y" or quest == "yes" or quest == "y" or quest == "Yes" or quest == "YES":                        #reply if user knows his/ her age.
       print ("since you know you better work harder")
       print (full_name + " You are a student of " + Name_of_inst + " under the faculty of " + Faculty + " in the department of " + Dpt + " with matric number " + mat_number + " thanks for your time. And remember " + Name_of_inst + " is not a playing ground.")
    else:                       #reply if user replies N or any other reply apart from ( y, yes, Yes, YES)
        print ("time waits for no man continue wasting it... you better sit down and calculate your age.")
        print (full_name + " You are a student of " + Name_of_inst + " under the faculty of " + Faculty + " in the department of " + Dpt + " with matric number " + mat_number + " thanks for your time. And remember " + Name_of_inst + " is not a playing ground.")


                                                                          



#reply if not an oau student
else:
    namesofoau = [ "OAU", "Oba Awon University", "Great Ife", "Obafemi Awolowo University"]  # a list of other names for OAU. (bounded by "[ ] "as string is bounded by " " )

    insults_list = [ "Glorified secondary school", "advanced secondary school", "play ground"]

    import random           #importing a builtin module (random)
    random.choice(namesofoau)
    random.choice(insults_list)

    print ("This app is built for " + random.choice(namesofoau) + " students only 'NOT' for any " + random.choice(insults_list) +" student." + " THANK YOU...")





    
    




