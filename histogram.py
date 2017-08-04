import os
import numpy as np
# mpl.use('tkagg')
import matplotlib.pyplot as plt
os.system("rm test*.png *.pyc")

# plt.ion()
# from IPython.display import Latex, Markdown
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
# Plot a normalized histogram with 50 bins
fig1 = plt.figure()
plt.hist(v, bins=50, normed=1)  # matplotlib version (plot)
# plt.show()
# fig1.savefig('test2.png')
plt.savefig('test.png')

# Compute the histogram with numpy and then plot it
fig2 = plt.figure()
(n, bins) = np.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
ax = plt.plot(.5 * (bins[1:] + bins[:-1]), n)
# fig2.savefig('test5.png')
plt.savefig('test2.png')
plt.show(block=False)
