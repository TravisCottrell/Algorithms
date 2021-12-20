import numpy as np

class FeedForward_Neural_Network:
    def __init__(self,inputs,hiddenAmount, outputAmount, biasValue,Threshold):
        self.threshold = Threshold
        self.hiddenweights = np.random.uniform(-1,1, size=(len(inputs[0]) * hiddenAmount,1)).reshape(hiddenAmount,len(inputs[0]))
        self.outputweights = np.random.uniform(-1,1, size=(hiddenAmount * outputAmount,1)).reshape(outputAmount,hiddenAmount)
        self.learningRate = 2
        
    def cycle(self, inputs, targetOutputs, cycleAmount):
        negthres = -1 * self.threshold
        for i in range(cycleAmount):
        
            # Pass the input set through the network.
            output1 = self.process(inputs, self.hiddenweights)

            # get the error
            error1 = targetOutputs - output1

            adjustweight = self.adjust_weight(output1, error1)
            temp1 = self.hiddenweights - self.learningRate * adjustweight
            
            # if np.all(temp1 < self.threshold) and np.all(temp1 > negthres):
            self.hiddenweights = temp1
            # else:
            #     for hrow,frow in zip(self.hiddenweights,adjustweight):
            #         for h,f in zip(hrow,frow):
            #             hf = h + f
            #             if((hf < self.threshold) and (hf > negthres)):
                            # h = hf
           
        ###########################################################################
            
            # Pass the input set through the network.
            output2 = self.process(self.hiddenweights, self.outputweights)

            # get the error
            error2 = targetOutputs - output2

            adjustweight2 = self.adjust_weight(output2, error2)
            temp2 = self.outputweights - self.learningRate * adjustweight2
            
            #if np.all(temp2 < self.threshold) and np.all(temp2 > negthres):
            self.outputweights = temp2
            # else:
            #      for orow,frow in zip(self.outputweights,adjustweight2):
            #         for o,f in zip(orow,frow):
            #             of = o + f
            #             if((of < self.threshold) and (of > negthres)):
            #                 o = of

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x)) 
    
    def process(self, inputs, weight):
        return self.sigmoid(np.dot(inputs, weight))
    
    def adjust_weight(self, output, error):
        return np.dot(output.T, error * (output * (1 - output)))
    
    
inputs = np.array([[0, 1, 1], [1, 1, 0], [1, 0, 1]])
outputs = np.array([[1, 0, 1]])
hiddenAmout = 3 
outputAmount = 3  
biasValue = 1 
cycleAmount = 2000 
Threshold = 1 - np.finfo(float).eps
     
test = FeedForward_Neural_Network(inputs,hiddenAmout, outputAmount,biasValue,Threshold)
test.cycle(inputs, outputs, cycleAmount)
print(test.process(outputs, test.outputweights))
