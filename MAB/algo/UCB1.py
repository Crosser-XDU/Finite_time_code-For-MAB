import math

class UCB1():
    def __init__(self,K) -> None:
        self.K=K
        self.t=0

    def initialize(self):
        self.count=[0 for i in range(self.K)]
        self.value=[0.0 for i in range(self.K)]

    def choose(self):

        for arm in range(self.K):
            if self.count[arm]==0:
                return arm
        ucb1=[0.0 for i in range(self.K)]
        for arm in range(self.K):
            r=math.sqrt((2 * math.log(self.t)) / float(self.count[arm]))
            ucb1[arm]=self.value[arm]+r

        return ucb1.index(max(ucb1))

    def update(self,chosen_arm,reward):
        self.count[chosen_arm]+=1
        n=self.count[chosen_arm]
        self.value[chosen_arm]=(self.value[chosen_arm]*float(n-1)+reward)/float(n)
        self.t+=1

