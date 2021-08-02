def nb_year(p0, percent, aug, p):
    years =[]
    if p >= int(p0):
        while p >=  int(p0):            
            p0 += p0*(percent/100) + aug
            print(int(p0))
            years.append(int(p0))
    n = len(years)
    if percent == 0:
        n = n - 1
    print(n)


nb_year(2010000, 0.0, 10000, 2000000)
nb_year(1000, 2, 50, 1214)