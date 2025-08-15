
l=[]
for i in range(1,100):
    n=input("Enter your word:")
    if(n==""):
        break
    l.append(n)
print(l)

l.reverse()
print(l)

h= " ".join(map(str,l))

print(h)

r=str(h)[::-1]
print(r)

