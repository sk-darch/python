list1 = [11, 5, 36, 27, 49]
list2 = [303, 101, 202, 505, 404]
list3 = [3000, 5000, 4000, 1000, 2000]

list1.sort()
list2.sort()
list3.sort()

maxlist = [list1[-2], list1[-1], list2[-2], list2[-1], list3[-2], list3[-1]]
minlist = [list1[0], list1[1], list2[0], list2[1], list3[0], list3[1]]
mxavg = sum(maxlist) / len(maxlist)
miavg = sum(minlist) / len(minlist)

print "The maxlist elements are : ", maxlist 
print "The average of maxlist is : ", mxavg
print "The minlists elements are : ", minlist
print "The average of minlist is : ", miavg