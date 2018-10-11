import scipy
import matplotlib.pyplot as plt
import numpy as np

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
samples = scipy.fromfile(open("file8_0_0.00034800.dat"), dtype=scipy.uint32)

# print(samples[0:1000])

samples = (samples > 0) * 1

print(len(samples))
print(samples[:1000])

prev = 1
prev_cant = 0
for s in samples:
    if (s != prev):
        prev_cant = prev_cant + 1
        print(prev, prev_cant)
        prev_cant = 0
        prev = s
    else:
        prev_cant = prev_cant + 1


grouped_samples= list(chunks(samples[28:], 16))

downsampled = []
for i,s in enumerate(grouped_samples):
    downsampled.append(np.bincount(s).argmax()) 

print(''.join(map(str, downsampled)))

# # print(np.mean(samples.reshape(-1, 16), axis=1))

# #  downsampled.append(np.bincount(samples.slice(i, )).argmax())

# plt.plot(downsampled)
# plt.show()