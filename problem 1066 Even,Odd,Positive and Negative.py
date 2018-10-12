even=0
odd=0
positive=0
negative=0
for i in range(5):
    n = float(input())
    if(n % 2 == 0):
         even = even+1
    else:
        odd =odd+1
    if (n > 0):
        positive =positive+1
    elif (n < 0):
        negative =negative+1
print("{} valor(es) par(es)".format(even))
print("{} valor(es) impar(es)".format(odd))
print("{} valor(es) positivo(s)".format(positive))
print("{} valor(es) negativo(s)".format(negative))