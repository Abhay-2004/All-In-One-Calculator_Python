# Abhay Prasanna Rao
'''
This program is named as " ALl IN ONE CALCULATOR" 
You can calculate your Body Mass Index or
You can convert the temperatur from Faherenheit to Celcius or Kelvin, or
You can play around with lists for fun!

Enter the correct Input in order for the code to run properly and to get the desired output

Example - you can convert temperature from fahrenheit or you can figure out if you have a low or high BMI and if you are fit or not 
or you can do some simple calculations using the lists
'''

def BMIcalc(): #This function calculates the Body Mass Index
    try :
        height=float(input("Enter your height(in cm ): "))
    except:
        print("\nError....Enter float/integer! ")
        print("\nReturning to the MAIN MENU ")
        return
    try:
        Weight=float(input("Enter your weight (in Kg): "))
    except:
        print("\nError...Enter integer value!")
        print("\nReturning to the MAIN MENU ")
        return
    height = height/100
    b=Weight/(height*height)
    print("\nYour Body Mass Index is: ",b)
    if(b>0):
        if(b<=16):
            print("\nYou are extremely underweight !")
        elif(b<=18.5):
            print("\nYou are underweight...On the border line")
        elif(b<=25):
            print("\nYou are fit and healthy! ")
        elif(b<=30):
            print("\nYou are Overweight! ")
        else: print("\nYou are extremely Overweight! ")
    else:("\nEnter the details properly")

def TempConv(): #This function calculates the temperature in celcuis and kelvin
    try:
        temperature = float(input("\nEnter the temperature in Fahrenheit: "))
    except:
        print("\nError....Enter float/integer! ")
        print("\nReturning to the MAIN MENU ")
        return
    inp = input("Do you want to convert it into Celcius[c] or kelvin [k]: ")
    if inp == 'c':
        g = (temperature - 32)*(5/9)
        print(f"In Celcius, it's {g} degrees.")
    elif inp == 'k':
        k = 5 * (temperature-32)/9 + 273.15
        print("In kelvin, it's ",round(k,2))
    else:
        print("Please enter [c] or [k]")

def playwithlists(): # This function is used to manuplate the lists and perform some specific operations
    strlist1 = []
    strlist2 = []
    numlist1 = []
    numlist2 = []
    resultnumlist=[]
    resultstrlist=[]

    z = input("\nDo you want to play with list containing numbers [n] or string [s]: ")

    if z == 'n':
        try:
            xy = int(input("\nHow many numbers do you want to input in the list? "))
        except:
            print("\nError! You had to enter integer value.....")
            print("Returning to the Main Menu.....")
            return
        print("\nEnter {0} digist for the 1st list".format(xy))
        xyz = True
        while xyz == True:
            for i in range (0,xy):
                numlist1.append(int(input()))
                #i+=1
            print("\nEnter {0} digist for the 2nd list".format(xy))
            for j in range (0,xy):
                numlist2.append(int(input()))
                #j+=1
            break
        ask1 = input("\nDo you want to add[a] subtract[s] or multiply[m] ?")
        if ask1 == 'a':
            for i in range (0,xy):
                resultnumlist.append(numlist1[i]+numlist2[i])
            print()
            print(f"The resultant list is : {resultnumlist}")
        elif ask1 == 's':
            for ij in range (0,xy):
                resultnumlist.append(numlist1[ij]-numlist2[ij])
            print()
            print(f"The resultant list is : {resultnumlist}")
        elif ask1 =='m':
            for iji in range (0,xy):
                resultnumlist.append(numlist1[iji]*numlist2[iji])
            print()
            print(f"The resultant list is : {resultnumlist}")
        else:
            print("\nError! Please enter [a], [s] or [m] !")

    elif z =='s':
        print("\nYou selected to play with string lists! ")
        print("\nCurrently, you can only concatnate the lists....")
        try:
            xz = int(input("\nEnter the number of words you want to register in the lists: "))
        except:
            print("\nError...Enter integer value!")
            print("\nReturning to the MAIN MENU ")
            return
        print("\nEnter {0} words for the 1st list".format(xz))
        for i in range(0,xz):
            ele = input()
            strlist1.append(ele)
            i+=1
        print("\nEnter {0} words for the 2nd list".format(xz))
        for j in range(0,xz):
            ele1 = input()
            strlist2.append(ele1)
            j+=1
        resultstrlist = strlist1+strlist2
        print("\nNew list after merigin the two lists is {0}".format(resultstrlist))
    else:
        print("\nError...Enter [n] or [s] ")

def main():
    end = False

    print("\nAll in one Calculator! ")
    print()
    
    print("Name: Abhay Prasanna Rao")
    print()

    while end == False:

        choice = input("\nMAIN MENU: [b]BMI Calculator, [t]Temperature conversion, [l] play with lists or [q]uit?: ")
        print()
        # Calling the Body Mass Index function
        if choice == "b": 
            BMIcalc()

        elif choice == "t":
        # Calling the Temperature conversion function
            TempConv()
        
        elif choice == "l":
        # Calling the list function
            playwithlists()

        elif choice == "q":
            end = True
            print("Have a good Day....Bye! ")
            print()

        else:
            print("Please enter [b], [t], or [q]...")
            print()

if __name__ == "__main__":
    main()