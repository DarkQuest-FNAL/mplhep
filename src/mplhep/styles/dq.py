from __future__ import annotations

import matplotlib as mpl

# PRL figsize / Elsevier figsize, Nature is somewhere in between
# single column width -  86 mm (3.386in) /  90 mm (3.543in)
# double column width - 172 mm (6.772in) / 180 mm (7.087in)
# For now size to 10

DQ = {
    "font.sans-serif": ["TeX Gyre Heros", "Helvetica", "Arial"],
    "font.family": "sans-serif",
    "mathtext.fontset": "custom",
    "mathtext.rm": "TeX Gyre Heros",
    "mathtext.bf": "TeX Gyre Heros:bold",
    "mathtext.sf": "TeX Gyre Heros",
    "mathtext.it": "TeX Gyre Heros:italic",
    "mathtext.tt": "TeX Gyre Heros",
    "mathtext.cal": "TeX Gyre Heros",
    "mathtext.default": "regular",
    "figure.figsize": (10.0, 10.0),
    "font.size": 23,
    "axes.labelsize": "large",
    "axes.unicode_minus": False,
    "xtick.labelsize": "medium",
    "ytick.labelsize": "medium",
    "legend.fontsize": "small",
    "legend.handlelength": 1.5,
    "legend.borderpad": 0.5,
    "legend.frameon": False,
    "xtick.direction": "in",
    "xtick.major.size": 12,
    "xtick.minor.size": 6,
    "xtick.major.pad": 6,
    "xtick.top": True,
    "xtick.major.top": True,
    "xtick.major.bottom": True,
    "xtick.minor.top": True,
    "xtick.minor.bottom": True,
    "xtick.minor.visible": True,
    "ytick.direction": "in",
    "ytick.major.size": 12,
    "ytick.minor.size": 6.0,
    "ytick.right": True,
    "ytick.major.left": True,
    "ytick.major.right": True,
    "ytick.minor.left": True,
    "ytick.minor.right": True,
    "ytick.minor.visible": True,
    "grid.alpha": 0.8,
    "grid.linestyle": ":",
    "axes.linewidth": 2,
    "savefig.transparent": False,
    "xaxis.labellocation": "right",
    "yaxis.labellocation": "top",
}

# Filter extra (labellocation) items if needed
DQ = {k: v for k, v in DQ.items() if k in mpl.rcParams}

DQTex = {
    **DQ,
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{siunitx},\sisetup{detect-all}, \
                              \usepackage{helvet},\usepackage{sansmath}, \
                              \sansmath",
}

ROOT = DQ  # Leave as default
# ROOT = DeprecDict(
#     CMS, message="'ROOT' style dict is deprecated, please use 'CMS' or other"
#     "experiment specific stytle instead"
# )
ROOTTex = DQTex
# ROOTTex = DeprecDict(
#     CMSTex, message="'ROOTTex' style dict is deprecated, please use 'CMSTex' or other"
#     "experiment specific stytle instead"
# )

