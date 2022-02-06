class Diff():
    def __init__(self, ratio):
        self.ratio=ratio

    def compute(self, lista):
        res=[]
        for i in range(0, len(lista)-1):
            res.append((lista[i+1]-lista[i])/self.ratio)
        return res
    
diff = Diff(1)
result = diff.compute([2,4,8,16])
print(result)