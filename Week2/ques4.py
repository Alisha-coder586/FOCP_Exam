no_of_sweets=float(input("Enter number of sweets: "))
no_of_pupils=float(input("Enter number of pupils attending: "))
no_of_sweet_per_person=no_of_sweets//no_of_pupils
no_of_left_over=no_of_sweets%no_of_pupils
print("Sweet per person to be distributed %d left over sweets %d"%(no_of_sweet_per_person, no_of_left_over))