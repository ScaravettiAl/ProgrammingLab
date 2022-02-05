class MovingAverage():
    def __init__(self, n):
        self.n= n
    
    def compute(self, lista):
        l= len(lista)
        res=[]
        r=0
        s=0
        e=self.n
        while e <= l:
            for i in range(s, e):
                print(i)
                r+=lista[i]
        
        res.append(r/self.n)
        print(i)
        print(res)
        s+=1
        e+=1
        c+=1
        return res

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result)