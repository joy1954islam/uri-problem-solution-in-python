X,Y=list(map(int,input().split()))
if(X == 1):
    price  = (float) (4.00 * Y)
elif(X == 2):
    price  = (float) (4.50 * Y)
elif(X == 3):
    price  = (float) (5.00 * Y)
elif (X == 4):
    price  = (float) (2.00 * Y);
elif (X == 5):
    price  = (float) (1.50 * Y)
print("Total: R$ %.2f"%price)