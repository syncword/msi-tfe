import scipy
import matplotlib.pyplot as plt

samples = scipy.fromfile(open("packet.dat"), dtype=scipy.uint32)

print(samples[0:1000])

# samples = (samples > 0) * 1

# print(len(samples))
# print(samples[:20])
# plt.plot(samples)
# plt.show()