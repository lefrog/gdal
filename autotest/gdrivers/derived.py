#!/usr/bin/env python
###############################################################################
# $Id$
#
# Project:  GDAL/OGR Test Suite
# Purpose:  Test derived driver
# Author:   Julien Michel <julien dot michel at cnes dot fr>
#
###############################################################################
# Copyright (c) 2016, Julien Michel, <julien dot michel at cnes dot fr>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################

import sys
from osgeo import gdal


import gdaltest
import pytest


def test_derived_test1():
    filename = "../gcore/data/cfloat64.tif"
    gdal.ErrorReset()
    ds = gdal.Open(filename)
    assert ds is not None and gdal.GetLastErrorMsg() == ''
    got_dsds = ds.GetMetadata('DERIVED_SUBDATASETS')
    expected_gt = ds.GetGeoTransform()
    expected_prj = ds.GetProjection()
    expected_dsds = {'DERIVED_SUBDATASET_1_NAME': 'DERIVED_SUBDATASET:AMPLITUDE:../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_1_DESC': 'Amplitude of input bands from ../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_2_NAME': 'DERIVED_SUBDATASET:PHASE:../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_2_DESC': 'Phase of input bands from ../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_3_NAME': 'DERIVED_SUBDATASET:REAL:../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_3_DESC': 'Real part of input bands from ../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_4_NAME': 'DERIVED_SUBDATASET:IMAG:../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_4_DESC': 'Imaginary part of input bands from ../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_5_NAME': 'DERIVED_SUBDATASET:CONJ:../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_5_DESC': 'Conjugate of input bands from ../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_6_NAME': 'DERIVED_SUBDATASET:INTENSITY:../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_6_DESC': 'Intensity (squared amplitude) of input bands from ../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_7_NAME': 'DERIVED_SUBDATASET:LOGAMPLITUDE:../gcore/data/cfloat64.tif',
                     'DERIVED_SUBDATASET_7_DESC': 'log10 of amplitude of input bands from ../gcore/data/cfloat64.tif'}

    if got_dsds != expected_dsds:
        import pprint
        pprint.pprint(got_dsds)
        pytest.fail()

    for key in expected_dsds:
        val = expected_dsds[key]
        if key.endswith('_NAME'):
            ds = gdal.Open(val)
            assert ds is not None and gdal.GetLastErrorMsg() == ''
            gt = ds.GetGeoTransform()
            if gt != expected_gt:
                import pprint
                pprint.pprint("Expected geotransform: " + str(expected_gt) + ", got " + str(gt))
                pytest.fail()
            prj = ds.GetProjection()
            if prj != expected_prj:
                import pprint
                pprint.pprint("Expected projection: " + str(expected_prj) + ", got: " + str(gt))
                pytest.fail()
    

def test_derived_test2():
    filename = "../gcore/data/cint_sar.tif"
    gdal.ErrorReset()
    ds = gdal.Open(filename)
    assert ds is not None and gdal.GetLastErrorMsg() == ''
    got_dsds = ds.GetMetadata('DERIVED_SUBDATASETS')
    expected_dsds = {'DERIVED_SUBDATASET_1_NAME': 'DERIVED_SUBDATASET:AMPLITUDE:../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_1_DESC': 'Amplitude of input bands from ../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_2_NAME': 'DERIVED_SUBDATASET:PHASE:../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_2_DESC': 'Phase of input bands from ../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_3_NAME': 'DERIVED_SUBDATASET:REAL:../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_3_DESC': 'Real part of input bands from ../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_4_NAME': 'DERIVED_SUBDATASET:IMAG:../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_4_DESC': 'Imaginary part of input bands from ../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_5_NAME': 'DERIVED_SUBDATASET:CONJ:../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_5_DESC': 'Conjugate of input bands from ../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_6_NAME': 'DERIVED_SUBDATASET:INTENSITY:../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_6_DESC': 'Intensity (squared amplitude) of input bands from ../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_7_NAME': 'DERIVED_SUBDATASET:LOGAMPLITUDE:../gcore/data/cint_sar.tif',
                     'DERIVED_SUBDATASET_7_DESC': 'log10 of amplitude of input bands from ../gcore/data/cint_sar.tif'}

    expected_cs = {'DERIVED_SUBDATASET_1_NAME': 345,
                   'DERIVED_SUBDATASET_2_NAME': 10,
                   'DERIVED_SUBDATASET_3_NAME': 159,
                   'DERIVED_SUBDATASET_4_NAME': 142,
                   'DERIVED_SUBDATASET_5_NAME': 110,
                   'DERIVED_SUBDATASET_6_NAME': 314,
                   'DERIVED_SUBDATASET_7_NAME': 55}

    if got_dsds != expected_dsds:
        import pprint
        pprint.pprint(got_dsds)
        pytest.fail()

    for key in expected_dsds:
        val = expected_dsds[key]
        if key.endswith('_NAME'):
            ds = gdal.Open(val)
            assert ds is not None and gdal.GetLastErrorMsg() == ''
            cs = ds.GetRasterBand(1).Checksum()
            if expected_cs[key] != cs:
                import pprint
                pprint.pprint("Expected checksum " + str(expected_cs[key]) + ", got " + str(cs))
                pytest.fail()

    
# Error cases


def test_derived_test3():

    with gdaltest.error_handler():
        # Missing filename
        ds = gdal.Open('DERIVED_SUBDATASET:LOGAMPLITUDE')
    assert ds is None

    with gdaltest.error_handler():
        ds = gdal.Open('DERIVED_SUBDATASET:invalid_alg:../gcore/data/byte.tif')
    assert ds is None

    with gdaltest.error_handler():
        ds = gdal.Open('DERIVED_SUBDATASET:LOGAMPLITUDE:dataset_does_not_exist')
    assert ds is None

    with gdaltest.error_handler():
        # Raster with zero band
        ds = gdal.Open('DERIVED_SUBDATASET:LOGAMPLITUDE:data/CSK_DGM.h5')
    assert ds is None

    for function in ['real', 'imag', 'complex', 'mod', 'phase', 'conj',
                     'sum', 'diff', 'mul', 'cmul', 'inv', 'intensity',
                     'sqrt', 'log10', 'dB', 'dB2amp', 'dB2pow']:
        ds = gdal.Open('<VRTDataset rasterXSize="1" rasterYSize="1"><VRTRasterBand subClass="VRTDerivedRasterBand"><PixelFunctionType>%s</PixelFunctionType></VRTRasterBand></VRTDataset>' % function)
        with gdaltest.error_handler():
            ds.GetRasterBand(1).Checksum()

    


if __name__ == '__main__':

    gdaltest.setup_run('derived')

    gdaltest.run_tests(gdaltest_list)

    sys.exit(gdaltest.summarize())
