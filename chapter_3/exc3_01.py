from pylab import loadtxt, plot, show, xlabel, ylabel, title


data = loadtxt("sunspots.txt")

time = data[:, 0]
sunspot_num = data[:, 1]
average_run = [(1/10 * sum(sunspot_num[i-5: i+5]))
               for i in range(len(sunspot_num) - 5)]
plot(time, sunspot_num, "g-")
plot(time[5:], average_run, "ro")
xlabel("Months")
ylabel("Sunspot Number")
title(" Sunspot Number vs Months")
show()
