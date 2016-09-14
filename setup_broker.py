import matplotlib
matplotlib.use('qt5agg')

import os
from portable_mds.sqlite.mds import MDS
from portable_fs.sqlite.fs import FileStore
from databroker import Broker


def make_broker(directory='storage'):

    os.makedirs(directory, exist_ok=True)
    mds = MDS({'directory': directory, 'timezone': 'US/Eastern'})
    fs = FileStore({'dbpath': os.path.join(directory, 'filestore.db')})
    return Broker(mds, fs)


db = make_broker()
