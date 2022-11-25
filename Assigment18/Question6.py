# Write a python program to create a dictionary that contains three dictionaries.(nested)
course1 = {
  "name" : "BCA",
  "year" : 2004  }
course2 = {
  "name" : "BBA",
  "year" : 2007  }
course3 = {
  "name" : "MCA",
  "year" : 2010  }

Qualification = {
  "course1" : course1,
  "course2" : course2,
  "course3" : course3
}
print(Qualification)
