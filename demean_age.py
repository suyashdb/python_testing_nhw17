import numpy as np
age = np.loadtxt("participants.tsv", skiprows=1, usecols=3)
mean_age = sum(age)/len(age)
assert mean_age < 120
assert mean_age > 10;
np.savetxt("demeaned_age.txt", age-mean_age)
print("done!!")
