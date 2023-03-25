from algo.UCB1 import UCB1
from algo.UCB1_tuned import UCB1_tuned
from Test_base import *
import matplotlib.pyplot as plt
from algo.UCB2 import *
from algo.epsilon_Greedy import *


def test(algo,means,N=100,T=100000,alpha=None):

    K=len(means)
    arms = [Arm(means[i]) for i in range(K)]
    best_arm=means.index(max(means))
    print("Best arm is " + str(best_arm))
    if alpha==None:
        algori = algo(K,T)
        result = test_algo(algori, arms, N, T)
        result=handle_for_regret(result,means,best_arm)
        regret=ave_up(result)

        X=[i+1 for i in range(T)]
        plt.xscale('log')
        plt.plot(X,regret)  
        plt.show()
    else:
        alpha_num=len(alpha)
        X=[i+1 for i in range(T)]
        markers=["*","o","^","x","H"]
        legent=[]
        plt.xscale('log')
        for i in range(alpha_num):
            algori=algo(alpha[i],0.3,K)
            result = test_algo(algori, arms, N, T)
            percet=percentage(result,best_arm)
            percet=ave_up(percet)
            legent.append("epsi-Greedy alpha="+str(alpha[i]))
            plt.plot(X,percet,marker=markers[i],markevery=0.1)   
        algori=UCB1_tuned(K)
        result = test_algo(algori, arms, N, T)
        percet=percentage(result,best_arm)
        percet=ave_up(percet)
        legent.append("UCB_tuned")
        plt.plot(X,percet,marker=markers[3],markevery=0.1)
        algori=UCB2(0.001,K)
        result = test_algo(algori, arms, N, T)
        percet=percentage(result,best_arm)
        percet=ave_up(percet)
        legent.append("UCB2 alpha=0.001")
        plt.plot(X,percet,marker=markers[4],markevery=0.1)
        plt.legend(legent)    
        plt.show()        






