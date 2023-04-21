# code to make a table containing info about the students in a class

name = ['Samantha', 'Charles', 'Jada', 'Jude', 'Jane', 'James', 'Claire', 'Kelvin', 'Elizabeth', 'Biodun', 'Mary',
        'Wale', 'Susan', 'Kunle',
        'Waje', 'Matthew', 'Taibat', 'Tom', 'Lilian', 'Kayode']
age = [17, 19, 16, 16, 17, 18, 18, 17, 16, 20, 18, 19, 17, 16, 20, 18, 19, 17, 17, 19]
height = [5.5, 5.7, 6.0, 5.9, 5.4, 5.8, 5.9, 6.1, 5.6, 5.9, 5.5, 5.5, 6.1, 6.1, 6.0, 5.4, 5.7, 5.8, 5.5, 5.7]
scores = [80, 74, 85, 87, 70, 75, 60, 68, 76, 66, 66, 78, 87, 87, 95, 98, 50, 54, 49, 60]

print('Name     | Age  | Height | Scores')
for i in range(len(name)):
    print(name[i], "|", age[i], "|", height[i], "|", scores[i])
