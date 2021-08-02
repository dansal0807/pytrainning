def descending_order(num):
    list_nums = [int(i) for i in str(num)]
    list_nums.sort(reverse = True)
    fnum = ""
    for c in list_nums:
        i = str(c)
        fnum += i
    
    print(fnum)


descending_order(51)
