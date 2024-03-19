import numpy as np
import random
import time
import matplotlib.pyplot as plt
# from tqdm.notebook import tqdm
from matplotlib import style
random.seed(0.5)
# print(plt.style.available)
data = []

omega1 = 1

T = 5 / omega1
dT = 1 / (1000 * omega1)
t = np.arange(0, T, dT)

# c = np.zeros((2, int(T / dT)), dtype=np.complex128)    # | C(2,:) | ^ 2 is the excited state population
# c[0, 1] = 1
# print(c.shape)

leng = 1
c_mean = np.zeros((leng, int(T / dT)))

omega = 1
gamma = 1
delta = 0
fig, ax = plt.subplots(1, 4, figsize=(20, 3))
t0 = time.time()

set = [10,3,2,5]

leng = 10

for jj in range(leng):
    c = np.zeros((2, int(T / dT)), dtype=np.complex128)  # | C(2,:) | ^ 2 is the excited state population
    c[0, 0] = 1

for a, om in enumerate(set):
    index = a
    omega = om
    for n in range(int(T / dT)-1):

        rand = random.uniform(0,1)

        if rand < (2 * gamma * dT * (abs(c[1, n])) * (abs(c[1, n]))):
            c[0, n + 1] = 1
            c[1, n + 1] = 0
        else:
            c[0, n + 1] = 1j * dT * (omega * c[1, n]) + c[0, n]
            c[1, n + 1] = 1j * dT * (omega * c[0, n]) + c[1, n] -c[1, n] * gamma * dT + 1j * dT * (delta * c[1, n]) + 1j * delta * dT * c[1, n]

            c[0, n + 1] = c[0, n+1] / np.sqrt((abs(c[0, n + 1]))*(abs(c[0, n + 1])) + (abs(c[1, n + 1]))*(abs(c[1, n + 1])))
            c[1, n + 1] = c[1, n + 1] / np.sqrt((abs(c[0, n + 1]))*(abs(c[0, n + 1])) + (abs(c[1, n + 1]))*(abs(c[1, n + 1])))

    c_mean[jj] = (abs(c[1])) * (abs(c[1]))

    print(a)
    ax[index].plot(np.mean(c_mean,axis = 0), color = "C0",ls = "-")
    ax[index].title.set_text(f"Omega={omega} gamma={gamma}")
plt.show()
    # np.savetxt(r'C:\Users\ariel\Dropbox (Weizmann Institute)\Deep Learning\project\data1\repetition={} omega={}  gamma={} delta={}.dat'.format(r+1, w, gamma, delta), c_mean[jj], delimiter=",")
    #np.save(r'C:\Users\ariel\Dropbox (Weizmann Institute)\Deep Learning\project\Dataset\validation\repetition={} omega={}  gamma={} delta={}'.format(r + 1, w, gamma, delta), c_mean[jj])
    # plt.plot(t, np.mean(c_mean,axis = 0), color = "C0",ls = "-")
    # plt.show()
# data.append(c_mean[jj])

# t1 = time.time()
# print(t1-t0)
# np.save(r'C:\Users\ariel\Desktop\master1.dat', data)  #, delimiter=",")

# np.savetxt(r'C:\Users\ariel\Desktop\master1.dat', data, delimiter=",")

# z = 1 / 3 - 1 / 15 * np.exp(-3 / 2 * t) * (np.sqrt(15) * np.sin(np.sqrt(15) / 2 * t) + 5 * np.cos(np.sqrt(15) / 2 * t))

# numpy.savetxt(r'C:\Users\ariel\Desktop\master1.dat', np.mean(c_mean, axis = 0))





plt.figure(1)
plt.style.use('bmh')
plt.plot(t, np.mean(c_mean,axis = 0), color = "C0",ls = "-")
# plt.plot(t, z, color = (1,0.5,0), ls="solid")

plt.xlabel('$t~\left[\\frac{1}{\Omega}\\right]$')
plt.ylabel('$|C_e(t)|^2$')
# plt.xlim([0,5])
plt.ylim([0,1.2])
plt.title('$Excited~State~Population~vs.~Time$', fontsize=15, color="black", fontname="Calibri", fontweight="bold")
plt.show()

