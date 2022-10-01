#If statement= is a block of code that will execute if its condition is true

#age = int(input("HOW OLD ARE YOU ?:"))

#if age ==100:
 #   print("YOU ARE AN ANCENT OF DAYS BOSS")
#elif age >= 18:
 #   print("You are an adult.")
#elif age < 18:
  #  print("YOU ARE A MINOR ")
#elif age < 0:
  #  print("YOU ARE NOT BORN YET ABEG REST")

#else:
  # print("You are a minor ")


print("WELCOME TO THE ROLLRCOASTER!!!\n")

height = int(input("What is your height in cm ?\n"))
bill = 0

if height >= 120 and height <= 139:
    print("You can enter the ride ")
    age = int(input("What is your age ?\n"))
    if age <=10:
        bill = 7
        print("Kids  fee is $7")
    elif age >=18:
        bill = 15
        print("Adult fee is  15$")
    else:
        bill = 12
        print("teens fee is $12")

    wants_photo = input("DO YOU WANT A PICTURE TAKEN ? Y OR N ?:")
    if wants_photo == "Y":
        bill += 3
        print(f"YOUR TOTAL BILL IS ${bill}")
    else:
        print(f"YOUR TOTAL BILL IS ${bill}")

    print("ENJOY THE RIDE!!")


elif height >=140:
    print("You are too tall for this ride,Pls try another section. ")
else:
    print("Sorry you are below 120cm , kindly try another ride. ")















