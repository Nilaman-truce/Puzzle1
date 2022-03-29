def checknr(number, checknumber, nr_correct,nr_correct_position):
    count_nr_correct = 0
    count_nr_correct_position = 0
    lnumber = str(number).zfill(len(checknumber))
    for i in range(len(checknumber)):
        if lnumber[i] in checknumber:
            count_nr_correct += 1
        if lnumber[i] == checknumber[i]:
            count_nr_correct_position += 1
    
    return nr_correct == count_nr_correct and \
        nr_correct_position == count_nr_correct_position

for cnumber in range (1000):
    if checknr(cnumber, '682', 1,1) and \
       checknr(cnumber, '614', 1,0) and \
       checknr(cnumber, '206', 2,0) and \
       checknr(cnumber, '738', 0,0) and \
       checknr(cnumber, '380', 1,0) :

       print("Code found: " + str(cnumber).zfill(3))