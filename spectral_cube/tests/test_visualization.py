from __future__ import print_function, absolute_import, division

import pytest

from .test_spectral_cube import cube_and_raw


def test_to_pvextractor():
    pytest.importorskip('pvextractor')
    cube, data = cube_and_raw('vda_Jybeam_lower.fits')
    cube.to_pvextractor()


def test_projvis():
    pytest.importorskip('matplotlib')
    cube, data = cube_and_raw('vda_Jybeam_lower.fits')
    mom0 = cube.moment0()
    mom0.quicklook(use_aplpy=False)


def test_proj_imshow():
    plt = pytest.importorskip('matplotlib.pyplot')
    cube, data = cube_and_raw('vda_Jybeam_lower.fits')
    mom0 = cube.moment0()
    plt.imshow(mom0)


def test_projvis_aplpy():
    pytest.importorskip('aplpy')
    cube, data = cube_and_raw('vda_Jybeam_lower.fits')
    mom0 = cube.moment0()
    mom0.quicklook(use_aplpy=True)


def test_mask_quicklook():
    pytest.importorskip('aplpy')
    cube, data = cube_and_raw('vda_Jybeam_lower.fits')
    cube.mask.quicklook(view=(0, slice(None), slice(None)), use_aplpy=True)


def test_to_glue():
    pytest.importorskip('glue')
    cube, data = cube_and_raw('vda_Jybeam_lower.fits')
    cube.to_glue(start_gui=False)
