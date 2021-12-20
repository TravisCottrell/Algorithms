class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class regression_analysis:
    
    def __init__(self, points,totalPoints):
        self.totalPoints = totalPoints
        self.points = points
        self.slope = 0
        self.intercept = 0  
        print(self.points)
        x_Sum = 0
        y_Sum = 0
 
        for point in self.points:
            x_Sum += point.x
            y_Sum += point.y

        x_Avg = x_Sum / self.totalPoints
        y_Avg = y_Sum / self.totalPoints

        x_Var = self.x_Variance(x_Avg)
        
        
        cov_XY = self.covarianceXY(x_Avg, y_Avg)
       

        self.slope = cov_XY / x_Var
        print("slope: ", self.slope)
        
        self.intercept = y_Avg - (self.slope * x_Avg)
        print("Y intercept: ", self.intercept)

    def x_Variance(self, x_Avg):
        vSum = 0
        for point in self.points:
            vSum += (point.x - x_Avg) ** 2

        variance = (1 / (self.totalPoints - 1)) * vSum
        return variance

    def covarianceXY(self, x_Avg, y_Avg):
        cvSum = 0
        for point in self.points:
            cvSum += (point.x - x_Avg) * (point.y - y_Avg)

        covariance = (1 / (self.totalPoints - 1) ) * cvSum
        return covariance