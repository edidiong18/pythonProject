import matplotlib.pyplot as plt

def coordinate():
    print("please enter an x value")
    value_x = input()
    print("please enter a y value")
    value_y = input()
    return value_x, value_y

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for values in range(4):
        data=coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]

def run():
    values = path()
    plt.plot(values[0], values[1], 'r--o')

    plt.xlabel = 'x_values'
    plt.ylabel = 'y_values'
    plt.show()

run()
