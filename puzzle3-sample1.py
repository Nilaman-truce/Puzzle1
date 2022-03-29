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
    if checknr(cnumber, '147', 1,0) and \
       checknr(cnumber, '189', 1,1) and \
       checknr(cnumber, '964', 2,0) and \
       checknr(cnumber, '532', 0,0) and \
       checknr(cnumber, '286', 1,0) :

       print("Code found: " + str(cnumber).zfill(3))