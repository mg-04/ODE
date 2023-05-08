import numpy as np
import matplotlib.pyplot as plt
dt = 0.01                   # time step
Ti, Tf, Yi = 0, 10, 0       # initial conditions
Kp, Ki, Kd = 1, 0.2, 0.5      # gains
k = 0.1                     # cooling rate
def system(y, t, u):
    return -k*y + u
def r(t):
    return 10
    #return 1 + 0.2*np.sin(t)
    if (t > 5 and t < 15):
        return 1
    else: 
        return 0

#for Kp in [0.5, 1, 1.5]:
#for Ki in [0.02, 0.1, 0.5]:
for Kd in [0,0.5]:
    yVals = []
    tVals = []
    rVals = []
    uVals = []

    # initialization
    y = Yi  
    t = Ti
    integral = 0
    derivative = 0
    prevError = r(Ti) - y
    #for t in np.arange()
    for i in range(Ti, int(Tf / dt)):
        """
        try:
            error = r(t) - yVals[i-100]
        except:
            error = r(t)
"""
        error = r(t) - y
        u = Kp*error + Ki*integral + Kd*derivative
        #u = max(min(u, 10), -10)   # for rate limit

        integral += dt * error
        derivative = (error - prevError)/dt
        prevError = error

        dy = system(y, t, u)
        y += dy*dt
        t += dt

        rVals.append(r(t))
        tVals.append(i*dt)
        yVals.append(y)
        uVals.append(u)
  
    plt.plot(tVals, yVals)
    #plt.yscale('log')
#plt.plot(tVals, uVals)
plt.plot(tVals, rVals)

#plt.title("Kp=0.7, Kd=0.5")
#plt.title("Ki=0.1, Kd=0.5")
plt.title("Kp=1, Ki=0.2")
#plt.title("1-second Delay")

#plt.legend(["Ki=0.02", "Ki=0.1", "Ki=0.5"])
#plt.legend(["Kp=0.5", "Kp=1", "Kp=1.5"])
plt.legend(["Kd=0", "Kd=0.5", "r(t)"])
#plt.legend(["y(t)", "r(t)"])

#plt.ylim([0, 1.5])
#plt.xlim([0, 2000*dt])

plt.show()