# Coding Challenge 2, compound_interest.py
# Name: Adhiraj Lamichhane
# Student No: 2226691

# Compound Interest Calculator

"""
Requirements:
    You will develop a program to calculate compound interest.

    • Print a welcome message explaining the purpose of the program.
    • Prompt the user for the necessary inputs (see formulae and brief)
    • Convert input values to suitable data types.
    • Perform compound interest calculation using the forumlae provided.
    • Print the result to the terminal using appropriate formatting.
    
    • Your program should be as close as possible to the example shown in the assessment brief.

Constraints:
    • Ensure that the interest rate is entered as a percentage and not a decimal.
    • Ensure that all monetary values are formatted to two decimal places.

Hints:
    • Think about what data types are the most appropriate for each input value.
    • Order of operations will be important, make sure you use parenthesis.
    • Review lecture two for more information on string formatting.
    • Your programs output should be as close as possible to the example in the assessment brief.
"""

# TODO: Write your code here!

# ANSI Code for Color are listed below
red = "\033[31m"          
green="\033[32m"
Yellow = "\033[33m"
Cyan = "\033[36m"
Reset = "\033[0m"

U="\033[4;37m"  #Underlined text
u="\033[0;37m"
B="\033[1;37m"  #Bold text
b="\033[0;37m"

s=" "
j="-"
k="="

#Welcome Message
print()
print(f"{k*80}")
print(f"{Cyan}",f"{s*13}Welcome to the Wolving compound interest calculator.\n {s*4}This program calculates your potential returns when you invest with us")
print(f"{Reset}")
print(f"{Reset}",f"{k*80}")
#iteration to run program multiple times
while True:

#defiining function to calculate compound interest
    def ci(p,r,t,n):

# calculate compound interest
        CI=(p*Rate)/100
        return CI;

#Get Input From the User
    p=int(input(f"{green}What is the principal amount?:{s*14}{red} £"))
    r=float(input(f"{green}What is rate?:{s*30}{red} "))
    t=int(input(f"{green}What is the number of years?:{s*15}{red} "))
    n=int(input(f"{green}Times the interest is compounded per year?:{red}  "))
    period=n*t
    Rate=(r/n)
    ini=p
    i=0
    x=1
    year=1
    print(f"{Reset}",f"{k*80}")
    show=" Year   Period  Old Balance   Interest  New Balance"
    print(f"{B}",show,f"{b}")
    print(f"{j*53}")

#iterations for calculation of CI for each period
#prints CI for each period
    for i in range(0,period):
        
        #calling the function
        CI= ci(p,r,t,n)
        A=p+CI 

#Formatted output for tabular output
        print(f"{s*3}", year,f"{s*4}",x,f"{s*4}", "%.2f"%(p),f"{s*4}","%.2f"%(CI),f"{s*4}","%.2f"%(A))
        p=A
        if (x%n == 0):
            print()
            print(f"{s*16}", f"{U}","Year",year,"Total Amount:",f"{u}", f"{red}$","%.2f"%(A))
            int(year)
            year=year+1
            print(f"{Reset}",f"{j*53}")
        else:
            print(f"{Reset}")
            year=year+0
        x=x+1
    print(f"{s*26}",f"{green}Net Amount:","%.2f"%(A))
    print (f"{Reset}","...")


#Conclusion message(result)
    print(f"{B}","£",f"{b}",ini,f"{Yellow}invested over",f"{B}", t,f"{b}",f"{Yellow}years, compounding",f"{B}",n,f"{b}",f"{Yellow}times per year is:",f"{red}£%.2f"%(A))
    print(f"{Reset}")

#Ask user if they want to reuse the program
    Again=input("Do you want to redo?(Y/N")
    if (Again=="Y" or Again=="y"):
        print()
        continue
    else:
        print("\n")
        print(f"{red}Thank You For Using our Program.")
        print("\n")
        break

