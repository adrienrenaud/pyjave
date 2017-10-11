import numpy as np
import plotly.graph_objs as go
import scipy.stats


def histo_w_error(data, 
                  bins=None, range=None):
    histvalues, binedges = np.histogram(data, bins=bins, range=(-5, 5))
    bincenters = (binedges[1:]+binedges[:-1])/2
    error_y = scipy.stats.poisson.interval(0.682, histvalues)
    
    histo = go.Bar(
        x=bincenters,
        y=histvalues,
        error_y=dict(
            type='data',
            symmetric=False,
            array=error_y[1]-histvalues,
            arrayminus=histvalues - error_y[0]
        )
    )

    layout = go.Layout(
        bargap=0.
    )

    fig = go.Figure(data=[histo], layout=layout)
    
    return fig
