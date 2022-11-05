a = '100+200+1000'
count_symbols = 0
for i in range(0, len(a)):
    
    if a[i] == "+":
        tmp = a[i-count_symbols:i+1]
        print(tmp)
        count_symbols = 0
    elif i == len(a) -1:
        tmp = a[i-count_symbols:i+1]
        print(tmp)
        count_symbols = 0
    else:
        count_symbols += 1 
        