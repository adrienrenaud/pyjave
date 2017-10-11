from . import plotlytools
import pandas as pd
import plotly.offline as py

py.init_notebook_mode(connected=True)

def _jhist(self, bins=None, range=None):
    data = self.values
    fig = plotlytools.histo_w_error(data, bins, range)
    return py.iplot(fig)

pd.Series.jhist = _jhist
