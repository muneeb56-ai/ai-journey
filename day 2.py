# Cities = ["Okara", "Sahiwal", "Pakpattan", "Patoki"]
# print(Cities)
# print(Cities[2])
# print(Cities[-1])
# print(Cities[1])
# print(Cities[0])
# print(Cities[3])
# print(len(Cities))
grocery_items = ["soap", "shampoo", "tea", "sugar", "oil"]
for items in grocery_items:
    print(items)
# print(grocery_items[0])
# print(grocery_items[1])
# print(grocery_items[2])
# print(grocery_items[3])
# print(grocery_items[4])
# print(len(grocery_items))
# grocery_items.append("salt")
# grocery_items[0]="butter"  ##this is used to replace the value using position index
# print(grocery_items)
# print(len(grocery_items))
marks = [25,31,47,79,60,58]
# print(marks)
# print(marks[5])
# print(len(marks))
# # print(len(marks[3]))
# print(max(marks))
# print(min(marks))
# print(sum(marks))  
# print(sum(marks)/len(marks))    ##this is used to calculate the average of the marks
# print(if (marks>= 50)"Pass", else "Fail")  ##this is used to check the pass or fail of the student
# for i in marks:
#     if i>=50:
#         print("Pass")
#     else:
#         print("Fail")

# print("Pass" if marks>=50 else"Fail")
for m in marks:
    # print("Pass" if m>=50 else"Fail" )
    print(m,"Pass" if m>=50 else "Fail")
print("Done")


members = ["Ali", "Hamza", "Amir", "Raza", "Fahad"]
for persons in members:
    print("Welcome ,", persons)



    scores = [5 , 52,63,15,18,79,67,91]
    total = 0
    count = 0
    maximum = 0
    minimum = 100
    average = 0
    passed = 0
    for score in scores:
        total= total+score
        count=count+1
        if score>maximum:
            maximum=score
        if score<minimum:
                minimum=score
        if score>=50:
             passed=passed +1

    print("Total:", total)
    print("Count:", count)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Average:", total/count)
    print("Passed:", passed)