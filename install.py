import os
import shutil
import matplotlib as mpl

stylelib = os.path.join(mpl.get_configdir(), 'stylelib')
[shutil.copy(f, stylelib) for f in os.listdir('.') if f.endswith('.mplstyle')]
