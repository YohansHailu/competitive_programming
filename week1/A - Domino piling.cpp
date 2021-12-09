##code forcess
## find number of dominos that fit in a board

in_list = list(map(int,input().split()));
 
m = in_list[0]
n = in_list[1]
 
if(m % 2 == 0):
    print( int(m/2 * n) )
elif(n%2 ==0):
    print(  int(m * n/2) )
else:
    print(  int( (m-1)/2*n+(n-1)/2 )  )
