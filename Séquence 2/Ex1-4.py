T = [1,2,3,4,5,6,7,8,9,10] 



for i in range(0, 5, 1):
   v = T[i]
   T[i]= T[10-i-1]
   T[10-i-1]= v 

print ("Après inversion :")
print (T)