def longest(a1, a2):
    # your code
    a3 = a1 + a2
    while True:
        try:
            filter(str.isalpha, a3)
            break
        except ValueError:
            print("This can't be done.")
    
    s3=[]
    for i in a3:
        s3.append(i)
    s3 = list(dict.fromkeys(s3))
    fstr = "".join(s3)
    print(fstr)
        



longest("aretheyhere", "yestheyarehere")