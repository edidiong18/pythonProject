import matplotlib.pyplot as plt

#display
def display(x,y):
    plt.xlabel("x_values")
    plt.ylabel("y_values")
    plt.plot(x, y)
    plt.show()
#run
def run():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    display(x,y)
run()
