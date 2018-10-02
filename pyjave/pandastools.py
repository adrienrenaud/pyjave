from . import plotlytools
import pandas as pd
from IPython.display import display
import plotly.offline as py

try:
    py.init_notebook_mode(connected=True)
except:
    pass

def _jhist(self, bins=None, range=None):
    data = self.values
    fig = plotlytools.histo_w_error(data, bins, range)
    return py.iplot(fig)

def _printnb(self, name='DataFrame', n=2):
    print(f'\n::: {name}')
    display(self.head(n))
    print(f'Shape: {self.shape}')


pd.DataFrame.printnb = _printnb
pd.Series.jhist = _jhist
