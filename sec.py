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
