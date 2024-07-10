def main():
    Number = int(input("Enter the number of students: "))
    
    marks = []
    print(f"Enter marks for {Number} students:")
    for i in range(Number):
        marks.append(int(input()))
    

    max_mark = 0
    min_mark = 100
    
    for mark in marks:
        if mark > max_mark:
            max_mark = mark
        if mark > 0 and mark < min_mark:
            min_mark = mark
    
    print(f"The maximum marks scored by the students is: {max_mark}")
    print(f"The minimum marks scored by the students is: {min_mark}")
    
 
    Sum = 0
    for mark in marks:
        Sum += mark
    average = Sum / Number
    print(f"The Average marks scored by the students are: {average}")
    

    Absent = 0
    for mark in marks:
        if mark == -1:
            Absent += 1
    print(f"Number of students marked as Absent: {Absent}")
    

    passed_students = 0
    for mark in marks:
        if mark >= 33:
            passed_students += 1
    failed_students = Number - passed_students
    
    passed_percentage = (passed_students / Number) * 100
    failed_percentage = (failed_students / Number) * 100
    
    print(f"Percentage of students who have passed the examination: {passed_percentage}%")
    print(f"Percentage of students who have failed the examination: {failed_percentage}%")
    

    freq = {}
    for mark in marks:
        if mark in freq:
            freq[mark] += 1
        else:
            freq[mark] = 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    

    print("Marks with highest frequency: ")
    highest_freq = sorted_freq[0][1]
    for mark, count in sorted_freq:
        if count == highest_freq:
            print(f"Mark {mark}: {count} times")
        else:
            break
    
    print("Marks with lowest frequency: ")
    lowest_freq = sorted_freq[-1][1]
    for mark, count in reversed(sorted_freq):
        if count == lowest_freq:
            print(f"Mark {mark}: {count} times")
        else:
            break

if __name__ == "__main__":
    main()

#  Second assignment
n = int(input("Enter the total Number of students in the class: "))
cric_count = int(input("Enter the number of students that like to play cricket"))
badi_count = int(input("Enter the number of students who play football"))
foot_count = int(input("Enter the number of students that like to play cricket"))

cr_list = []
badi_list = []
foot_list = []

for i in range(0, cric_count)
    user_input = input("Enter the roll number of students who play cricket : ")
    cr_list.append(user_input)

for i in range(0, badi_count)
    user_input = input("Enter the roll number of students who play Badminton : ")
    badi_list.append(user_input)

for i in range(0, foot_count)
    user_input = input("Enter the roll number of students who play Football : ")
   foot_list.append(user_input)


x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []

for roll_number in range(1, n+1):
    if str(roll_number) in cr_list and str(roll_number) in badi_list:
        x1.append(str(roll_number))

    if str(roll_number) in cr_list and str(roll_number) in badi_list:
        if str(roll_number) not in foot_list:
            x2.append(str(roll_number))

    if str(roll_number) not in cr_list and str(roll_number) not in badi_list:
        x3.append(str(roll_number))

    if str(roll_number)  in cr_list and str(roll_number) in badi_list and str(roll_number) not in foot_list:
        x4.append(str(roll_number))

    if str(roll_number) not in cr_list and str(roll_number) not in badi_list and str(roll_number) not in foot_list:
        x5.append(str(roll_number))    

    if str(roll_number) in cr_list or str(roll_number) in badi_list or str(roll_number) in foot_list:
        x6.append(str(roll_number))        

    if str(roll_number) in cr_list and str(roll_number) in badi_list and str(roll_number) in foot_list:
        x7.append(str(roll_number))      



print("Students who play both cricket and badminton: ", x1)
print("Students who play either cricket or badminton but not football : ", x2)   
print("Students who play neither badminton nor cricket: ", x3)   
print("Students who play both cricket and football but not badminton : ", x4) 
print("Students who do not play any game: ", x5)
print("Students who play at least one game : ", x6)       
print("Students who play all the games : ", x7)   
