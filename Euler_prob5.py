import time
start_time = time.time()
def divisible(x,n):
    for i in range (1,n):
        if(x%i != 0):
            return False
    return True

if __name__ == "__main__":
    num = 2000
    while 1:

        if divisible (num,20):
            print ("found", num)
            print("--- %s seconds ---" % (time.time() - start_time))
            exit (0)
        num+=20
        #print("still searching", num)

