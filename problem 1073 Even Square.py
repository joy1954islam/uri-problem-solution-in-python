n= int(input())
for i in range(1,n+1):
    if(i%2==0):
        print("{}^{} = {}".format(i,2,pow(i,2)))