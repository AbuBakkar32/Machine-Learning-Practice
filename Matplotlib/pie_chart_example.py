import matplotlib.pyplot as matplot

matplot.pie([10, 25, 25, 20, 20], labels=["PHP", "Java", "Python", "JavaScript", "C Sharp"],
            colors=["red", "blue", "green", "yellow", "orange"], shadow=True, autopct="%1.1f%%", startangle=90,
            explode=(0.1, 0.1, 0.1, 0.1, 0.1))
matplot.axis("equal")
matplot.show()
