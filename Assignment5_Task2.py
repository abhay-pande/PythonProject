n=list(range(1,11))
print("original list: "+ str(n))

a=n[0:5]
print("Extracted first five elements: " +str(a))

a.reverse()
print("Reverse Extracted Elements: "+ str(a))