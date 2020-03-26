grades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
print(grades[2])
print(sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]))
grades1 = [96, 90, 94]
grades.append(grades1)
print(grades[0], grades[1], grades[2], grades[3])
grades[0][1] = 20
print(grades[0])
gradesTuple = [(5, 17, 7), (23, 36, 28), (88, 80, 92)]
print(gradesTuple[2])
print(sum(gradesTuple[0])/len(gradesTuple[0]), sum(gradesTuple[1])/len(gradesTuple[1]),
      sum(gradesTuple[2])/len(gradesTuple[2]))
gradesdict = {
    "chinese": [5,14,7],
    "english": [23, 36, 28],
    "math": [88, 80, 92]}
print(gradesdict["math"])
print(gradesdict.get("math"))
print(sum(gradesdict["chinese"])/len(gradesdict["chinese"]))
print(sum(gradesdict["english"])/len(gradesdict["english"]))
print(sum(gradesdict["math"])/len(gradesdict["math"]))
gradesdict["science"] = [94, 90, 96]
gradesdict.update({"science": [94, 90, 96]})
print(gradesdict["science"])
fruits = {
    "apple",
    "banana",
    "guava",
    "guava"
}
fruits1 = {
    "strawberry",
    "banana",
    "papaya"
}
print(fruits | fruits1) #聯集
print(fruits & fruits1) #交集
print(fruits - fruits1) #差集
fruits.add("watermelon")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.remove("watermelon")
fruits.discard("watermelon")
print(fruits)
allstudents = {
    "John",
    "Eva",
    "Jill",
    "Eric",
    "Andy",
    "Albert",
    "Polina",
    "Kristin",
    "Angela"
}
danceclub = {
    "Andy",
    "Eric",
    "Albert",
    "Polina",
    "Kristin",
}
guitarclub = {
    "Jhon",
    "Eva",
    "Jill",
    "Eric",
    "Andy"
}
Set = {
    "Andy",
    "Eric",
    "Albert",
    "Polina",
    "Kristin",
    "John",
    "Eva",
    "Jill",
    "Eric",
    "Andy"
}
print(guitarclub & danceclub)
print(guitarclub - danceclub)
print(allstudents - Set)