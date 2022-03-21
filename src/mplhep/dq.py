from __future__ import annotations

import inspect

from matplotlib import docstring
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

import mplhep

from . import label as label_base
from .label import lumitext

# Log styles
from .styles import dq as style

# import mplhep._deprecate as deprecate

__all__ = ("style", "lumitext")


@docstring.copy(label_base.exp_text)
def text(text="", **kwargs):
    for key, value in dict(mplhep.rcParams.text._get_kwargs()).items():
        if (
            value is not None
            and key not in kwargs.keys()
            and key in inspect.getfullargspec(label_base.exp_text).kwonlyargs
        ):
            kwargs.setdefault(key, value)
    kwargs.setdefault("italic", (False, True))
    kwargs.setdefault("exp", "DarkQuest")
    return label_base.exp_text(text=text, **kwargs)


@docstring.copy(label_base.exp_label)
def label(label=None, **kwargs):
    for key, value in dict(mplhep.rcParams.label._get_kwargs()).items():
        if (
            value is not None
            and key not in kwargs.keys()
            and key in inspect.getfullargspec(label_base.exp_label).kwonlyargs
        ):
            kwargs.setdefault(key, value)
    kwargs.setdefault("italic", (False, True))
    if label is not None:
        kwargs["label"] = label
    kwargs.setdefault("exp", "DarkQuest")
    return label_base.exp_label(**kwargs)

def logo(ax, loc = 'bottom right'):

    #Get the positions of the plot
    xmin, xmax, ymin, ymax = plt.axis()
    arr_img = plt.imread('DQ.png')

    imagebox = OffsetImage(arr_img, zoom=0.1, alpha=0.2)
    imagebox.image.axes = ax

    if loc == 'bottom right':
        xy = (xmax-0.6, ymin+0.1)
    elif loc == 'top left':
        xy = (xmin+0.6, ymax-0.1)
    elif isinstance(loc, list):
        xy = loc
    else:
        raise TypeError('The location needs to be "bottom right", "top left" or a list')
    
    ab = AnnotationBbox(imagebox, xy, frameon = False)
    ax.add_artist(ab)

    #return ax

# Deprecation example
# @deprecate.deprecate("Naming convention is changing. Use ``mplhep.cms.label``.")
# def cmslabel(*args, **kwargs):
#     return _cms_label(*args, **kwargs)

