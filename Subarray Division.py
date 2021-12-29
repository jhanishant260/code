class quee:
    def __init__(self,month,date):
        self.items=[]
        self.month=month
        self.count=0
        self.date=date
    def sum(self):
        sum=0
        for i in self.items:
            sum=sum+i
        return sum
    def add(self,i):
        if len(self.items)<self.month:
            print("inside if")
            self.items.append(i)
        else:
            print("inside else")
            print(self.items)
            p=self.sum()
            if p==self.date:
                self.count = self.count+1
            self.items.pop(0)
            self.items.append(i)



m=7
d=18
c=[2,5, 1 ,3 ,4 ,4, 3, 5, 1, 1 ,2 ,1 ,4 ,1 ,3 ,3 ,4 ,2 ,1]
p= quee(m,d)
for i in c:
    p.add(i)
print(p.count)
