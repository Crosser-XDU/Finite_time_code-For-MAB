import random
class episilon_Greedy():
    def __init__(self,c,d,K) -> None:
        self.c=c
        self.d=d
        self.K=K

    def initialize(self):
        self.count=[0 for i in range(self.K)]
        self.value=[0.0 for i in range(self.K)]

    def choose(self):
        n=sum(self.count)+1
        epsilon=min(1,(self.c*self.K)/(self.d**2*n))
        if random.random() > epsilon:
            return self.value.index(max(self.value))
        else:
            return random.randrange(len(self.value))

    def update(self, chosen_arm, reward):
        self.count[chosen_arm]+=1
        n=self.count[chosen_arm]
        self.value[chosen_arm]=(self.value[chosen_arm]*float(n-1)+reward)/float(n)