import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

profile = ProfileReport(pd.read_csv('train.csv'), explorative=True)

# Saving results to a HTML file
profile.to_file("output.html")
