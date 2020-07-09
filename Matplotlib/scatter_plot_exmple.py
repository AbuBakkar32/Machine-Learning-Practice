import matplotlib.pyplot as matplot

matplot.figure("Ice Cream Sale According to Temperature")
ice_cream_sales = [10, 20, 15, 18, 25, 40, 35, 30, 19]
ice_cream_sales_1 = [11, 22, 17, 20, 27, 36, 32, 24, 16]
temperature = [14, 16, 11, 15, 18, 20, 10, 22, 17]

matplot.scatter(temperature, ice_cream_sales, marker="v", color="red")
matplot.scatter(temperature, ice_cream_sales_1, marker="o", color="green")
matplot.title("Ice Cream Sale According to Temperature")
matplot.xlabel("Temperature")
matplot.ylabel("Ice Cream Sales")
matplot.show()
