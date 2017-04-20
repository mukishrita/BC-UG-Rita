def find_missing(list1,list2):

      	if len(list1) == 0 and len(list2) == 0:
            return 0

    	list3 = list(set(list1).symmetric_difference(set(list2)))
        if len(list3) == 0:
            return 0
        else:
            return list3[0]