import time
start_time = time.time()
#a,b,s=1,1,0
a,b,s=2,8,2
while b < 4000000:
    a,b,s=b,a+4*b,s+b
print(s)
print("--- %s seconds ---" % (time.time() - start_time))