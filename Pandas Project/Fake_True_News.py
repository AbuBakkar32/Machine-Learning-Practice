import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

profile = ProfileReport(pd.read_csv('True_False_data.gz'), title='Fake And True Profiling Report', explorative=True)

# Saving results to a HTML file
profile.to_file("output.html")