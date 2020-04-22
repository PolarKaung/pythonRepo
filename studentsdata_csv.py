import csv
studentsdata = [["Index", "Name", "Roll No", "Year"],
             [1, "Rebacca", "1", "1"],
             [2, "Liam", "2", "1"],
             [3, "Jenny", "3", "1"],
             [4, "Taylor", "4", "1"],
             [5, "Tim","5", "1" ]]
            
with open('students.csv', 'w', newline='') as a:
    writer = csv.writer(a)
    writer.writerows(studentsdata)
