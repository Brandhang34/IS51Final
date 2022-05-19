

"""
STRUCTURED ENGLISH

The program will display the number of grades, the average grade, and the percentage of grades
that are above the average grade. Final.txt will supply the inputs, "grades" in order to do the
following operations. To count the number of grades, the program will append all of the data into a list
and print out the amount of items in the list. In order to find the average grade, the programm will 
add all of the numbers in "Final.txt" and divide by the amount of numbers in the text. The program will 
print that number and display the average. Finally, to print the percentage of grades above average,
the program will go through the list and append those numbers into a new list which are the values above 
average calculated before. Divide the length of the grades above average list by the overall list and 
multiply that value by 100 to get the percentage.
"""

"""
PSEUDO CODE

Create a main function
    open Final.txt file in read mode and set it to a variable called "file"
    create a list named "grades"
    loop through the file
        append the values into the grades list as an integer
    close the Final.txt file
    
    print the number of grades by obtaining the length of the list
    print the average grade by obtaining add all values in the list and divide it by the number of items

    call the calculate_percent_above_average() function, passing the grades list, the average, and the length

Create a Calculate_percent_above_average function
    Create a "grades_abv_avg" list

    loop through the original list
        if the value in the list is above the average
            append the value into the "grades_abv_avg" list
    
    create a variable called "percent_abv_avg" and set it to ((grades_abv_avg length / original list length) * 100)
    
    print "the percentage of grades above average: "  round(((grades_abv_avg length / original list length) * 100), 2), "%"

Call the main function
"""

#CODE

def main():
    file = open("Final.txt", "r")
    grades = []

    for i in file:
        grades.append(int(i))
    
    file.close()

    print("Number of grades: ", len(grades))
    print("Average grade: ", (sum(grades)/len(grades)))

    calculate_percent_above_average(grades, (sum(grades)/len(grades)), len(grades))

def calculate_percent_above_average(list, avg, leng):
    grades_abv_avg = []

    for i in list:
        if(i > avg): grades_abv_avg.append(i)
    
    percent_abv_avg = round(((len(grades_abv_avg) / leng) * 100), 2)

    print("Percentage of grades above average: ", percent_abv_avg, "%")
    
main()
    