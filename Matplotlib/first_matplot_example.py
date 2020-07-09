import matplotlib.pyplot as matplot

matplot.figure("Demo Graph")
matplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], label="Data 1", color="green")
matplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 2, 4, 2, 4, 2, 4, 2, 4], label="Data 2", color="blue")

matplot.xlabel("X Axis")
matplot.ylabel("Y Axis")
matplot.legend()
matplot.show()
