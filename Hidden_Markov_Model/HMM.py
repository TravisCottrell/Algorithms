import numpy as np

class HMM:
    def __init__(self,tm,em, sequence,initialState,graphSize):
        self.graphSize = graphSize
        self.states = np.arange(graphSize)
        
        self.tm = tm
        
        self.em = em
        
        self.sequence = sequence 
        
        self.initialState = initialState
        
        
    def cartesianProdcut(self):
        if self.graphSize == 2:
            
            cp = np.array(np.meshgrid(self.states,self.states)).T.reshape(-1, self.graphSize)
        elif self.graphSize == 3:
            cp = np.array(np.meshgrid(self.states,self.states,self.states)).T.reshape(-1, self.graphSize)
        elif self.graphSize == 4:
            cp = np.array(np.meshgrid(self.states,self.states,self.states,self.states)).T.reshape(-1, self.graphSize)
        elif self.graphSize == 5:
            cp = np.array(np.meshgrid(self.states,self.states,self.states,self.states,self.states)).T.reshape(-1, self.graphSize)
        elif self.graphSize == 6:
            cp = np.array(np.meshgrid(self.states,self.states,self.states,self.states,self.states,self.states)).T.reshape(-1, self.graphSize)
        elif self.graphSize == 7:
            cp = np.array(np.meshgrid(self.states,self.states,self.states,self.states,self.states,self.states,self.states)).T.reshape(-1, self.graphSize)
        elif self.graphSize == 8:
            cp = np.array(np.meshgrid(self.states,self.states,self.states,self.states,self.states,self.states,self.states,self.states)).T.reshape(-1, self.graphSize)
        return cp
        
                    
    def calcProb(self, cart):
        probabilities = list()
        for i,array in enumerate(cart):
            prob = self.initialState[array[0]]
            for j, a in enumerate(array):
                if j < len(array)-1:
                    emm = self.em[a][self.sequence[j]]
                    tmm = self.tm[a][array[j+1]]
                    prob *=  emm * tmm
                else:
                     prob *= self.em[a][self.sequence[j]]
            probabilities.append([prob, i])
            
        return probabilities



graphSize = input("graph size: ")
graphSize = int(graphSize)
tm = np.random.uniform(0,1, size=(graphSize,graphSize))
tm[0][2] = np.array(0)
em = np.random.uniform(0,1, size=(graphSize,graphSize))
initialState = np.random.uniform(0,1 , size=(graphSize))

loopcheck = True        

while loopcheck:
    seqList = list()
    sequence = input(f"enter a sequence of {graphSize} numbers: ") 
    for num in sequence:
        seqList.append(int(num)) 
    Hmm = HMM(tm, em, seqList, initialState, graphSize)
    cart = Hmm.cartesianProdcut()
    prob = Hmm.calcProb(cart)
    prob.sort(reverse=True)
    
    print("----------------------------------------------------------")
    print("emission matrix:")
    print(Hmm.em)
    print("----------------------------------------------------------")
    print("transition matrix:")
    print(Hmm.tm)
    print("----------------------------------------------------------")
    print("initial states:")
    print(Hmm.initialState)
    print("----------------------------------------------------------")
    for i in prob:
        print(f"{cart[i[1]]}->{i[0]}")
    print("------------------------------------------------------------")
    print(f"the most probable path is:{cart[prob[0][1]]}")
    print("probability:", prob[0][0])
    answer = input("loop again? y or n: ")
    if answer == 'n': loopcheck = False
