def compare_list(list_one, list_two):
    for element in list_one:
        if element not in list_two:
            print "not the same"
        else:
            print "same list"






list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compare_list(list_one,list_two)
