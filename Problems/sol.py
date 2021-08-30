def expanding(l):
    a=0
    for i in range(1,len(l)):
        if a >= abs(l[i]-l[i-1]):
            return False
        a=abs(l[i]-l[i-1])
    else:
        return True
      
def sumsquare(l):
    res=[]
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even=even+i**2
        else:
            odd=odd+i**2
    res.append(odd)
    res.append(even)
    return res
  
def transpose(m):
  n=m.copy()
  res=[]
  result = [[n[j][i] for j in range(len(n))] for i in range(len(n[0]))]
  return result