Dict = {'CS101': [3004, "Haynes", "8:00 a.m."],
        'CS102': [4501, "Alvarado", "9:00 a.m."],
        'CS103': [6755, "Rich", "10:00 a.m."],
        'NT110': [1244, "Burke", "11:00 a.m."],
        'CM241': [1411, "Lee", "1:00 p.m."]}


print("Once you put in the course number, the program will display that")
print("course's room number, instructor, and meeting time respectively.")

course_num = input("WHat is the couruse number? ")
print("Room Number: ", Dict[course_num][0])
print("Instructor: ", Dict[course_num][1])
print("Meeting Time: ", Dict[course_num][2])
