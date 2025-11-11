no_of_total_students=int(input("Enter number of students? "))
no_of_stu_per_group=int(input("Required group size? "))
no_of_group=no_of_total_students//no_of_stu_per_group
no_of_left_out=no_of_total_students-(no_of_group*no_of_stu_per_group)
print("No of Groups with %d Students each: %d"%(no_of_stu_per_group, no_of_group))
if (no_of_left_out<=1):
    print("No of Left Out Student: ", no_of_left_out)
else:
    print("No of Left Out Students: ", no_of_left_out)

