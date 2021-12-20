import numpy as np

class FeedForward_Neural_Network:
    def __init__(self,inputs,hiddenAmount, outputAmount, biasValue,Threshold):
        self.threshold = Threshold
        self.hiddenweights = np.random.uniform(-.5,.5, size=(len(inputs[0]) * hiddenAmount,1)).reshape(hiddenAmount,len(inputs[0]))
        self.outputweights = np.random.uniform(-.5,.5, size=(hiddenAmount * outputAmount,1)).reshape(outputAmount,hiddenAmount)
        self.learningRate = 0
        
    def cycle(self, inputs, targetOutputs, cycleAmount):
        for i in range(cycleAmount):
            temp = self.process(inputs, self.hiddenweights)
            error1 = targetOutputs - temp
            adjustweight1 = np.dot( error1 * self.sigmoidDerivative(temp), inputs.T)
            self.hiddenweights += adjustweight1
            
            temp2 = self.process(temp, self.outputweights)
            error2 = targetOutputs - temp2
            adjustweight2 = np.dot(error2 * self.sigmoidDerivative(temp2), inputs.T)
            
            self.outputweights += adjustweight2
            
            
            
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x)) 
    
    def sigmoidDerivative(self, x):
        return np.exp(-x)/((1 + np.exp(-x))**2) 
    
    def process(self, inputs, weight):
        return self.sigmoid(np.dot(weight, inputs))

       
    
    
inputs = np.array([[0, 1, 1], [1, 0, 0], [1, 0, 1]])
outputs = np.array([[1, 0, 1]])
hiddenAmout = 3 
outputAmount = 3 
biasValue = 1 
cycleAmount = 1000 
Threshold = 1 - np.finfo(float).eps
     
test = FeedForward_Neural_Network(inputs,hiddenAmout, outputAmount,biasValue,Threshold)
test.cycle(inputs, outputs, cycleAmount)
print(test.process(outputs, test.outputweights))
