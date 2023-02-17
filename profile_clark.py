#!/usr/bin/env python

import os
os.environ["NUMBA_NUM_THREADS"] = str(1)
os.environ["OMP_NUM_THREADS"] = str(1)
os.environ["OPENBLAS_NUM_THREADS"] = str(1)
os.environ["MKL_NUM_THREADS"] = str(1)
os.environ["VECLIB_MAXIMUM_THREADS"] = str(1)

import sys
import numpy as np
from daskms.experimental.zarr import xds_from_zarr
from pfb.deconv import clark
from pfb.utils.misc import dds2cubes
from pfb.deconv.clark import clark
from ducc0.misc import make_noncritical
# import pyscilog
# pyscilog.init('pfb')
# log = pyscilog.get_logger('CLARK')

if __name__=='__main__':
    dds_name = sys.argv[1]
    dds = xds_from_zarr(dds_name,
                        columns=('DIRTY','PSF','PSFHAT','WSUM','BEAM'))
    nband = len(dds)
    dirty, model, residual, psf, psfhat, beam, wsums, _ = dds2cubes(
                                                            dds,
                                                            nband,
                                                            apparent=True)

    dirty_mfs = np.sum(dirty, axis=0)
    rmax = dirty_mfs.max()

    # import pdb; pdb.set_trace()
    dirty = make_noncritical(dirty)
    psf = make_noncritical(psf)
    psfhat = make_noncritical(psfhat)

    x, status = clark(dirty, psf, psfhat,
                    threshold=0.0,
                    gamma=0.1,
                    pf=0.025,
                    maxit=50,
                    subpf=0.75,
                    submaxit=1000,
                    verbosity=1,
                    report_freq=10,
                    sigmathreshold=1,
                    nthreads=1)




