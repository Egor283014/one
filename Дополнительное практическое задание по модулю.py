# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
the_students_arithmetic_average = {'Johnny':[5, 3, 3, 5, 4],'Bilbo':[2, 2, 2, 3],'Steve':[4, 5, 5, 2],'Khendrik': [4, 4, 3],'Aaron':[5, 5, 5, 4, 5]}
Johnny= (sum([5, 3, 3, 5, 4])/len([5, 3, 3, 5, 4]))
print(Johnny)
the_students_arithmetic_average['Johnny']=Johnny
#print(the_students_arithmetic_average)
Bilbo=sum([2, 2, 2, 3])/len([2, 2, 2, 3])
the_students_arithmetic_average['Bilbo']=Bilbo
Steve=sum([4, 5, 5, 2])/len([4, 5, 5, 2])
the_students_arithmetic_average['Steve']=Steve
Khendrik=sum([4, 4, 3])/len([4, 4, 3])
the_students_arithmetic_average['Khendrik']=Khendrik
Aaron=sum([5, 5, 5, 4, 5])/len([5, 5, 5, 4, 5])
the_students_arithmetic_average['Aaron']=Aaron
print(the_students_arithmetic_average)
