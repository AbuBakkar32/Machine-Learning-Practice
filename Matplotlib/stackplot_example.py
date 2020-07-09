import matplotlib.pyplot as matplot

matplot.figure("Daily Schedule")

days = [1, 2, 3, 4, 5, 6, 7]
sleeping = [7, 8, 9, 10, 6, 12, 5]
eating = [2, 3, 4, 5, 1, 6, 7]
working = [9, 8, 7, 8, 9, 5, 11]
playing = [6, 5, 4, 1, 8, 1, 1]

matplot.plot([], [], color="red", label="Sleeping")
matplot.plot([], [], color="blue", label="Eating")
matplot.plot([], [], color="green", label="Working")
matplot.plot([], [], color="yellow", label="Playing")

matplot.stackplot(days, sleeping, eating, working, playing, colors=["red", "blue", "green", "yellow"])
matplot.title("Daily Schedule")
matplot.xlabel("Days")
matplot.ylabel("Daily Schedule")
matplot.legend()
matplot.show()
