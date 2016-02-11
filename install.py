import os
import shutil
import matplotlib as mpl

stylelib = os.path.join(mpl.get_configdir(), 'stylelib')

# in case you don't have a stylelib directory yet
try:
    os.mkdir(stylelib)

except FileExistsError:
    pass

# copy the files into the stylelib directory
[shutil.copy(f, stylelib) for f in os.listdir('.') if f.endswith('.mplstyle')]
