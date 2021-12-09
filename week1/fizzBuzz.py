def fizzBuzz(self, n: int) -> List[str]:
  a = [0]*n
  for i in range(1,n+1):
      if i%3 == 0 and i%5 == 0:
          a[i-1] = "FizzBuzz"
      elif i%3 == 0 :
          a[i-1] = "Fizz"
      elif i%5 == 0:
          a[i-1] = "Buzz"
      else: 
          a[i-1] = str(i)
  return a
