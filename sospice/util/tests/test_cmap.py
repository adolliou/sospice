from ..cmap import get_cmap
import matplotlib as mpl

def test_cmap():
    logt = 4.5
    cmap = get_cmap(logt=logt)
    assert isinstance(cmap, mpl.colors.LinearSegmentedColormap)