## code forces

m,n,a = map(int,input().split())
k = m//a;
k2 = n//a;
if m%a != 0:
    k+=1
if n%a != 0:
    k2+=1
print(k*k2)
