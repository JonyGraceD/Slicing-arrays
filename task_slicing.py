#Slicing over arrays
    #Task Assigned in Python ---> Slicing over 2-D and 3-D arrays
#Slicing over 1-D arrays
import numpy as np
a1=np.array([1,2,3,4,5,6,7,8])
print("a1: ",a1)
s1=a1[2:6]
print("\n s1: ",s1)

a=np.array(['Child','Teen','Young','Adult','Old'])
s=a[1:]
print("\n s: ",s)

b=np.array(['He','She','It','they','them'])
t=b[:5]
print("\n t: ",t)

c=np.array(['Cat','Goat','sheep','Cow','monkey'])
u=c[::]
print("\n u: ",u)

#Slicing over 2-D arrays
a2=np.array([[1,4,9,16],[25,36,49,64]])
print(a2)
s2=a2[0,1:3]
print("\n s2: ",s2)

a2=np.array([[1,4,9,16],[25,36,49,64]])
i=a2[1,0:]
print("\n i: ",i)

a2=np.array([[1,4,9,16],[25,36,49,64]])
j=a2[0,:]
print("\n j: ",j)

a2=np.array([[1,4,9,16],[25,36,49,64]])
k=a2[1,::2]
print("\n k: ",k)

a2=np.array([[1,4,9,16,25,36],[49,64,81,100,121,144]])
print("\n a2: ",a2)
l=a2[0,::3]
m=a2[1,::2]
print('\n l: ',l)
print('\n m: ',m)

#Slicing over 3-D arrays
a3=np.array([[['a','b','c','d'],['e','f','g','h'],['q','r','s','t']],[['i','j','k','l'],['m','n','o','p'],['u','v','w','x']]])
print("\n a3: ",a3)
s3=a3[0,2,1:3]
print("\n s3: ",s3)

a3=np.array([[['a','b','c','d'],['e','f','g','h'],['q','r','s','t']],[['i','j','k','l'],['m','n','o','p'],['u','v','w','x']]])
ab=a3[0,1,:]
print("\n ab: ",ab)

a3=np.array([[['a','b','c','d'],['e','f','g','h'],['q','r','s','t']],[['i','j','k','l'],['m','n','o','p'],['u','v','w','x']]])
ac=a3[1,2,::2]
print("\n ac: ",ac)

a3=np.array([[['a','b','c','d'],['e','f','g','h'],['q','r','s','t']],[['i','j','k','l'],['m','n','o','p'],['u','v','w','x']]])
ad=a3[1,0,::3]
print("\n ad: ",ad)

