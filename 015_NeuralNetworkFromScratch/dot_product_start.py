#%% packages
import numpy as np
# %%
X = [0, 1]
w1 = [2, 3]
w2 = [0.4, 1.8]

# %% Question: which weight is more similar to input data X
d1 = np.dot(X, w1)
print(d1)
d2 = np.dot(X, w2)
print(d2)
# %%
