#  import find_index_module as fim
#  import only find index function
from find_index_module import find_index

#  pandas, numpy
#  import pandas as pd
#  import numpy as np

req_idx = find_index(['Apple', 'Orange', 'Kiwi'], 'Orange')
print(req_idx)
print('running find index module: ', __name__)