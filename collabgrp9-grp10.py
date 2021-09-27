# Laboratory Activity No. 3 Assignment
# Author: Duran, Klibill & Delos Reyes, Nikki (Group 1)
# Author: Adame, Anamarie C. & Espiritu, Allysa Mae B. (Group 2)

print("----------------------------------------------")
print("           University Enrollment Form")
print("----------------------------------------------")

fname = str(input("Full Name\t\t\t:\t"))
email = str(input("Email Address\t\t\t:\t"))
usn = int(input("USN\t\t\t\t:\t"))
course = str(input("Course\t\t\t\t:\t"))
yrlvl = int(input("Year Level\t\t\t:\t"))
sem = str(input("Semester\t\t\t:\t"))

units = int(input("Enter No. of Total Units\t:\t"))
print("")
misc = 2300
ofee = 1250
tfee = 821 * units
gamount = misc + ofee + tfee
print("----------------------------------------------")
print("                Assessment Form")
print("----------------------------------------------")
print("Miscellaneous Fee\t\t:\t{}" .format(misc))
print("Other Fees\t\t\t:\t{}" .format(ofee))
print("Tuition Fee\t\t\t:\t{}" .format(tfee))
print("Gross Amount\t\t\t:\t{}" .format(gamount))
print("----------------------------------------------")

isko = str(input("Do you have a Scholarship?(Y/N)\t:\t"))

if isko == "Y" or isko == "y":
    disc = float(input ("Discount (%)\t\t\t:\t"))
    tda = gamount * (disc/100)
    print ("Total Discount Amount\t\t:\t{}" .format(tda))
    
    downp = int(input("Downpayment\t\t\t:\t"))

    tbal = gamount - downp - tda
    print("==============================================")
    print("Total Balance\t\t\t:\t{}" .format(tbal))
    print("==============================================")
elif isko == "N" or isko == "n":
    downp = int(input("Downpayment\t\t\t:\t"))

    tbal = gamount - downp
    print("==============================================")
    print("Total Balance\t\t\t:\t{}" .format(tbal))
    print("==============================================")
else:
    print("")
    print("----------------Invalid Input!----------------")
    
    
    
    