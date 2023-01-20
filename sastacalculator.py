#sasta calcultor
a=int(input("ENTER THE NUMBER:"))
b=int(input("ENTER THE NUMBER:"))
print("ENTER THE OPERATION YOU WANT TO PERFORM\n1.ADD\n2.SUBSTRACT\n3.MULTIPLY\n4.DIVIDE\n5.EXIT")
c=int(input("ENTER YOUR CHOICE:"))

if c==1:
    result=a+b
    print(result)
elif c==2:
    result=a-b
    print(result)
elif c==3:
    result=a*b
    print(result)
elif c==4:
    result=a/b
    print(result)
elif c>4 :
    print("EXIT")

