def find_char(list, val):
    temp = []
    for i in list:
        for j in i:
            if val == j:
                temp.append(i)
    print temp


find_char(['hello','world','my','name','is','Anna'], 'o')
