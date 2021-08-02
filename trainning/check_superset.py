set_A = set(input())
n = int(input())
sets_n = []
counting = 0

for i in range(n):
    set_n = set(input())
    sets_n.append(set_n)
    
for setsofn in sets_n:   
    if set_A.issuperset(setsofn):
        counting = 0 + counting
    else:
        pass

if counting == n:
    print(True)
else:
    print(False)
        