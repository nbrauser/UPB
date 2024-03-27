#  Question 1
tuple1 = ("Car", [34, 23, 8], False, [15, 20, 11])
print(tuple1[3][1])  # Goes the third position and then goes inside the set and goes to the 1 position where 20 is

# Question 2
List1 = [44, 12, 578, 21, 134, 67]
print(List1[3:6]) # Slices the list from the third position to the 5 position because the six is not included

# Question 3
list1 = [5, 10, 15, 20, 74, 100, 50]
list1[3] = 200  # goes to position 3 where the 20 is and then change the value to 200
print(list1)

# Question 4
tuple2 = (11, [64, 33], 243, 123)
tuple2[1][1] = 66  # Gets the 1 position where the list is then goes to the 1 position in the list to change 33 to 66
print(tuple2)

# Question 5
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))
# Merges the two sets but does not add two 30's, 40's, and 50's because sets dont have duplicates

# Question 6
list3 = [3, 6, 9, 12, 15, 18, 21]
list4 = [4, 8, 12, 16, 20, 24, 28]

list3.remove(3)
list3.remove(9)
list3.remove(15)
list3.remove(21) # removes the odd values
list3.extend(list4)  # combines the two lists
print(list3)

# Question 7
list4 = [34, 54, 67, 89, 11, 43, 94]
list4.remove(11)
list4.insert(2,11)
list4.append(11)
print(list4)

# Question 8
list5 = [10, 20,[300, 400, [5000, 6000], 500], 30, 40]
list5[2][2].insert(2,7000)
print(list5)

# Question 9
list6 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list7 = ["h", "i", "j"]
list6[2][1][2].extend(list7)  # goes into the position of the list where f and g is and extend it with the list7
print(list6)

# Question 10
tuple10 = (40, 19, 234, 12, 10, 123)
print(tuple10[-1], tuple10[-2], tuple10[-3], tuple10[-4], tuple10[-5], tuple10[-6])
# Prints the values in the reverse order by indexing them using negative values

# Question 11
dict1 = {
    "course": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(dict1["course"]["student"]["marks"]["history"])
# goes into the dictionary goes into the course then the student then marks and history and prints the value
