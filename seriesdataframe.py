import pandas as pd
import numpy as np
s1=pd.Series(np.random.random(5))
print(s1)
s2=pd.Series(np.random.random(5))
print(s2)
a= pd.DataFrame([s1,s2])
print(a)