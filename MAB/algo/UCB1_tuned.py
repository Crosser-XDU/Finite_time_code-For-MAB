import math
import numpy

class UCB1_tuned():
    def __init__(self,K) -> None:
        self.K=K
        self.t=0

    def initialize(self):
        self.count=[0 for i in range(self.K)]
        self.value=[0.0 for i in range(self.K)]
        self.squ_value=[0.0 for i in range(self.K)]
        self.t=0

    def v_j(self,j):
        return self.squ_value[j]/self.count[j]-self.value[j]**2+math.sqrt(2*math.log(self.t)/self.count[j])
        
    def choose(self):
        for arm in range(self.K):
            if self.count[arm]==0:
                return arm
        ucb1=[0.0 for i in range(self.K)]
        for arm in range(self.K):
            ucb1[arm]=self.value[arm]+math.sqrt((math.log(self.t)/self.count[arm])*min(1/4,self.v_j(arm)))
        return ucb1.index(max(ucb1))

    def update(self,chosen_arm,reward):
        self.count[chosen_arm]+=1
        n=self.count[chosen_arm]
        self.value[chosen_arm]=(self.value[chosen_arm]*float(n-1)+reward)/float(n)
        self.squ_value[chosen_arm]+=reward**2
        self.t+=1