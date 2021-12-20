import matplotlib.pyplot as plt
import random
from Linear_Regression_Analyzer import regression_analysis, Point

totalPoints = 30
min_point = 0
max_point = 100
loopcheck = True
while loopcheck:
    ###############################################################################################
    #random points to form a line for random points to follow
    rp = []
    rp.append(Point(random.randint(min_point, max_point),random.randint(min_point, max_point)))
    rp.append(Point(random.randint(min_point, max_point),random.randint(min_point, max_point)))

    #slope of random point line
    m = (rp[1].y-rp[0].y)/(rp[1].x-rp[0].x)
    #y-intercept of random point line
    b = rp[0].y
    variance = 3

    points = []
    #random points but following the random line

    for i in range(totalPoints):
        x = random.randint(min_point, max_point)
        novariance = b + (x * m)
        y = novariance + random.randint(-variance, variance)
        if y > min_point and y < max_point:
            points.append(Point(x,y))
    ###############################################################################################
    #completely random points
    # for i in range(totalPoints):
    #     points.append(Point(random.randint(0, 20),random.randint(0, 20)))


    plt.figure(figsize=(8, 8))

    # plotting the points
    for point in points:
        plt.scatter(point.x, point.y, color = 'blue')

    ra = regression_analysis(points,totalPoints)

    #plot the line 
    plt.axline((0,ra.intercept), slope=ra.slope, color="red")

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.xlim([min_point, max_point])
    plt.ylim([min_point, max_point])
    plt.show()
    check = input("run again y or n:")
    if check == 'n': loopcheck = False