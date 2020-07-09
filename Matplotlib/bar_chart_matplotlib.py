import matplotlib.pyplot as matplot

matplot.figure("Bar Chart")

x_data = [0, 2, 4, 6, 8, 10]
y_data = [4, 6, 8, 9, 10, 12]

x1_data = [1, 3, 5, 7, 9, 11]
y1_data = [5, 3, 6, 19, 2, 7]

x2_data = [12, 13, 14, 15, 16, 17]
y2_data = [2, 4, 7, 9, 3, 6]

matplot.bar(x_data, y_data, label="Data 1", color="red")
matplot.bar(x1_data, y1_data, label="Data 2", color="blue")
matplot.bar(x2_data, y2_data, label="Data 3", color="green")

matplot.xlabel("X Axis")
matplot.ylabel("Y Axis")
matplot.legend()
matplot.show()
