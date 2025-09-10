day_of_week = input("enter the day of week").lower() #convert lower case
print(day_of_week)
if day_of_week == "saturday" or day_of_week =="sunday": #==is comparing values

 print ("i will learn devops")
else :
    print ("i wil practice devops")

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    Choice = input ("Enter the operation (options: + , - , * , / , %): ")

    if Choice =="+":
        sum_of_num = num1 + num2
        print("addition: ",sum_of_num)

    elif Choice == "-":
        diff_of_num = num1 - num2
        print ("subtraction:", diff_of_num)

    elif Choice == "*":
        prod_of_num = num1 * num2
        print ("multiplicaion:", prod_of_num)

    elif Choice == "/":
            div_of_num = num1 / num2
            print ("division:", div_of_num)

    elif Choice == "%":
                rem_of_num = num1 % num2
                print("remainder:", rem_of_num)

    else :
                print ("invalid choice")   