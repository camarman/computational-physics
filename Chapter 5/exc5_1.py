from pylab import loadtxt, plot, show, xlabel, title, legend

data = loadtxt("velocities.txt")

time = data[:, 0]
velocity = data[:, 1]

func = dict(zip(time, velocity))

a = func[0]
b = func[100]
N = 100
h = 1  # the difference between each time step

S1 = sum([func[i] for i in range(1, N)])
I = h * (0.5 * (func[0] + func[100]) + S1)

distance = [0]
for i in range(0, 100):
    x = h * (func[i] + func[i+1] / 2)
    distance.append(distance[-1] + x)

plot(time, distance, "g--", label="position")
plot(time, velocity, "b-", label="velocity")
legend(loc='upper left')
xlabel("Time(s)")
title("Velocity vs Time and Distance vs Time")
show()
