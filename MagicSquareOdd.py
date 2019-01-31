def generateOdd(n): 

    mS = []
    for i in range(n):
      s = []
      for j in range(n):
        s.append(0)
      mS.append(s)

    i = 0
    j = int(n / 2)

    place = 1
    while place <= (n * n): 
        if i == -1 and j == n: 
            j = 0
            i = n - 1
        else:
            if j == n:
                j = 0
            if i == -1:
                i = n - 1
                  
        if mS[i][j]!=0: 
            i += 1
            continue
        else: 
            mS[i][j] = place
            place += 1
                  
        i -= 1
        j += 1
   
    for i in range(0, n): 
        for j in range(0, n): 
            print(mS[i][j] ,end='\t')
        print('\n') 
  

n = int(input())
generateOdd(n)      
  
