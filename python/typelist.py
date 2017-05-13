def type_list(list):
    string = []
    sum = 0
    status = False
    for i in list:
        if type(i) == str:
            string.append(i)
            status = True
        else:
            sum = sum + i
            status = True


    if string ==[]:
        print " the array you entered is integer type"
        print "Sum: ", sum
    elif sum == 0:
        print " the array you entered is string type"
        print "String: ", string
    else:
        print " the array you entered is mixed type"
        print "String: ", string
        print "Sum: ", sum





type_list(['magical unicorns',19,'hello',98.98,'world'])
type_list([2,3,1,7,4,12])
type_list(['magical','unicorns'])
