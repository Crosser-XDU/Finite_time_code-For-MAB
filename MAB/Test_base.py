import random

class Arm():
    def __init__(self,p) -> None:
        self.p=p

    def pull(self):
        if random.random()>self.p:
            return 0.0
        else:
            return 1.0

def test_algo(algo,arms,num_sim,horizen):
    chosen_arms=[0.0 for i in range(0,num_sim*horizen)]
    rewards=[0.0 for i in range(0,num_sim*horizen)]
    cumulative_reward=[0.0 for i in range(num_sim*horizen)]
    sim_nums=[0.0 for i in range(num_sim*horizen)]
    times=[0.0 for i in range(num_sim*horizen)]

    for sim in range(num_sim):
        sim=sim+1
        algo.initialize()

        for t in range(horizen):
            t=t+1
            index=(sim-1)*horizen+t-1
            sim_nums[index]=sim
            times[index]=t

            chosen_arm=algo.choose()
            chosen_arms[index]=chosen_arm

            reward=arms[chosen_arm].pull()
            rewards[index]=reward

            if t==1:
                cumulative_reward[index]=reward
            else:
                cumulative_reward[index]=reward+cumulative_reward[index-1]

            algo.update(chosen_arm,reward)
    return [sim_nums, times, chosen_arms, rewards, cumulative_reward]  

def ave_up(result):
    n=len(result[0])
    all=result[0][n-1]
    result_sum=[]
    epoch_size=int(n/all)
    for i in range(epoch_size):
        s=0.0
        for j in range(all):
            s+=result[4][i+j*epoch_size]
        result_sum.append(s/all)
    return result_sum    

def handle_for_regret(result,means,best_arm):
    cul=0.0
    best_reward=means[best_arm]
    n=len(result[0])
    all=result[0][n-1]
    epoch_size=int(n/all)
    for i in range(len(result[0])):
        cul+=means[result[2][i]]    
        result[4][i]=result[1][i]*best_reward-cul
        if result[1][i]==epoch_size:
            cul=0.0
    return result    


def percentage(result,best_arm):
    cul=0.0
    n=len(result[0])
    all=result[0][n-1]
    epoch_size=int(n/all)
    for i in range(len(result[0])):
        if result[2][i]==best_arm:
            cul+=1.0
        result[4][i]=cul*100/result[1][i]
        if result[1][i]==epoch_size:
            cul=0.0
    return result        





        



              




