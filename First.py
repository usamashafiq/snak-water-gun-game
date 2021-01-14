def getdate():
    import datetime
    return datetime.datetime.now()


print("   HEALTH MANAGEMENT SYSTEM")

print("     NUMBER OF MEMBER")
print("        Rohan  for 1")
print("        Hammad for 2")

x = int(input())

if x == 1:
    print("Hi Rohan")
    print("Choose the file : READ OR WRITE MODE WRITE FOR W AND READ FOR R")
    c=input("Enter the character")
    if c=='w':

        print("FOR FOOD SELECT  1", "FOR Exercise SELECT 2")
        y = int(input())
        if y == 1:

            f = open("rohanf.txt", "w")
            F = input("Enter the FOOD : ")
            f.write(str(getdate()))
            f.write(F)
            f.close()
        else:
            f = open("rohane.txt", "w")
            F = input("Enter the Exercise : ")
            f.write(str(getdate()))
            f.write(F)
            f.close()
    else:
        print("FOR FOOD SELECT  1", "FOR Exercise SELECT 2")
        y = int(input())
        if y == 1:

            f = open("rohanf.txt", "r")
            print(f.read())
            f.close()
        else:
            f = open("rohane.txt", "r")
            print(f.read())
            f.close()
elif x==2:
    print("Choose the file : ")

    print("FOR FOOD SELECT  1", "FOR Exercise SELECT 2")
    y = int(input())
    if y == 1:

        f = open("Hammadf.txt", "w")
        F = input("Enter the FOOD : ")
        f.write(str(getdate()))
        f.write(F)
        f.close()
    else:
        f = open("Hammade.txt", "w")
        F = input("Enter the Exercise : ")
        f.write(str(getdate()))
        f.write(F)
        f.close()
else:
    print("FOR FOOD SELECT  1", "FOR Exercise SELECT 2")
    y = int(input())
    if y == 1:

        f = open("rohanf.txt", "r")
        print(f.read())
        f.close()
    else:
        f = open("rohane.txt", "r")
        print(f.read())
        f.close()


