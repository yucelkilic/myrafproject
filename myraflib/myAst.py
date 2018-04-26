# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 19:48:32 2018

@author: mshem
"""
#Importing needed functions
from astropy import units as U
from astropy import coordinates


from astropy.time import Time

from astropy.wcs import WCS

from astropy.io import fits as fts

from astropy.table import Table as TBL

from scipy.ndimage.interpolation import shift

from numpy import min as nmin
from numpy import max as nmax
from numpy import mean as nmean
from numpy import median as nmead
from numpy import std as nstd
from numpy import log10 as nlog10
from numpy import asarray
from numpy import float64 as nf64
from numpy import sort as nsort

from math import pow as mpow
from math import sqrt as msqrt

from sep import Background
from sep import sum_circle
from sep import extract

from astroquery.vizier import Vizier

from datetime import datetime


#Importing myraf's needed modules
from . import myEnv

class fits():
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = myEnv.etc(verb=self.verb)
        
    def pure_header(self, src):
        try:
            hdu = fts.open(src, mode='readonly')
            return(hdu[0].header)
        except Exception as e:
            self.etc.log(e)
        
    def get_header(self, src):
        try:
            return(fts.getheader(src))
        except Exception as e:
            self.etc.log(e)
        
    def header(self, src, field="*"):
        self.etc.log("Getting Header from {}".format(src))
        ret = []
        try:
            hdu = fts.open(src, mode='readonly')
            for i in hdu[0].header:
                if not i == "":
                    ret.append([i, hdu[0].header[i]])
                
            if field == "*":
                return(ret)
            else:
                return([field, hdu[0].header[field]])
        except Exception as e:
            self.etc.log(e)
            
    def data(self, src, table=True):
        self.etc.log("Getting Data from {}".format(src))
        try:
            hdu = fts.open(src, mode='readonly')
            data = hdu[0].data
            data = data.byteswap().newbyteorder()
            if table:                
                return(TBL(data))
            else:
                data = data.byteswap().newbyteorder()
                data = data.astype(nf64)
                return(data)
        except Exception as e:
            self.etc.log(e)
    
    def delete_header(self, src, key):
        self.etc.log("Updating {}'s Header".format(src))
        try:
            hdu = fts.open(src, mode='update')
            del hdu[0].header[key]
            return(hdu.close())
        except Exception as e:
            self.etc.log(e)
    
    def update_header(self, src, key, value):
        self.etc.log("Updating {}'s Header".format(src))
        try:
            hdu = fts.open(src, mode='update')
            hdu[0].header[key] = value
            return(hdu.close())
        except Exception as e:
            self.etc.log(e)

    def fits_stat(self, src):
        self.etc.log("Getting Stats from {}".format(src))
        try:
            hdu = fits.open(src)
            image_data = hdu[0].data
            return({'Min': nmin(image_data),
                    'Max': nmax(image_data),
                    'Mean': nmean(image_data),
                    'Stdev': nstd(image_data)})
        except Exception as e:
            self.etc.log(e)
            
    def shift(self, dest, src, x, y):
        self.etc.log("Shifting Image {}".format(src))
        try:
            data = self.data(src, table=False)
            header = self.pure_header(src)
            new_data = self.shift_ar(data, x, y)
            self.write_h(dest, new_data, header)
        except Exception as e:
            self.etc.log(e)
            
    def shift_ar(self, data, x, y):
        self.etc.log("Shifting array x={}, y={}".format(x, y))
        try:
            return(shift(data, [x, y]))
        except Exception as e:
            self.etc.log(e)
        
            
    def write(self, dest, data):
        self.etc.log("Writeing data to file({})".format(dest))
        try:
            fts.writeto(dest, data)
        except Exception as e:
            self.etc.log(e)
            
    def write_h(self, dest, data, header):
        self.etc.log("WriteingH data to file({})".format(dest))
        try:
            fts.writeto(dest, data, header)
        except Exception as e:
            self.etc.log(e)
        

class calc():
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = myEnv.etc(verb=self.verb)
        self.fit = fits(verb=self.verb)
        
    def flux2magmerr(self, flux, fluxerr):
        self.etc.log("Calculating Mag and Merr")
        try:
            mag = -2.5 * nlog10(flux)
            magerr = 2.5 / nlog10(10.0) * fluxerr / flux
            return(mag, magerr)
        except Exception as e:
            self.etc.log(e)
            
    def radec2wcs(self, ra, dec):
        self.etc.log("Converting coordinates to WCS")
        try:
            c = coordinates.SkyCoord('{0} {1}'.format(ra, dec),
                                     unit=(U.hourangle, U.deg), frame='icrs')
            return(c)
        except Exception as e:
            self.etc.log(e)
            
    def xy2sky(self, file_name, x, y, sep=" "):
        self.etc.log("Converting physical coordinates to WCS")
        try:
            header = fts.getheader(file_name)
            w = WCS(header)
            astcoords_deg = w.wcs_pix2world([[x, y]], 0)
            c = coordinates.SkyCoord(astcoords_deg * U.deg, frame='icrs')
            #the_coo = c.to_string(style='hmsdms', sep=sep, precision=4)[0]
            return(c.ra.deg[0], c.dec.deg[0])
        except Exception as e:
            self.etc.log(e)
            
    def is_close_arc(self, coor1, coor2, max_dist=10):
        self.etc.log("Calculating proximity(WCS)")
        try:
            c1 = self.radec2wcs(coor1[0], coor1[1])
            c2 = self.radec2wcs(coor2[0], coor2[1])
            
            ret = c1.separation(c2)
            return(ret.arcsecond < max_dist)
        except Exception as e:
            self.etc.log(e)

    def is_close_phy(self, coor1, coor2, max_dist=15):
        self.etc.log("Calculating proximity(PHY)")
        try:
            dX = coor1[0] - coor2[0]
            dY = coor1[1] - coor2[1]
            dist = msqrt(mpow(dX, 2) + mpow(dY, 2))
            return(dist < max_dist)
        except Exception as e:
            self.etc.log(e)
        
    def jd(self, timestamp):
        self.etc.log("Calculating JD from timestamp({})".format(timestamp))
        try:
            if "T" not in timestamp:
                timestamp = str(timestamp).replace(" ", "T")
            
            t_jd = Time(timestamp, format='isot', scale='utc')
    
            return(t_jd.jd)
        except Exception as e:
            self.etc.log(e)
        
    def mjd(self, timestamp):
        self.etc.log("Calculating MJD from timestamp({})".format(timestamp))
        try:
            if "T" not in timestamp:
                timestamp = str(timestamp).replace(" ", "T")
            
            t_jd = Time(timestamp, format='isot', scale='utc')
    
            return(t_jd.mjd)
        except Exception as e:
            self.etc.log(e)
            
    def imexamine(self, src):
        try:
            data = self.fit.data(src, table=False)
            the_min = nmin(data)
            the_max = nmax(data)
            the_mea = nmean(data)
            the_std = nstd(data)
            the_med = nmead(data)
            return([the_mea, the_med, the_std, the_min, the_max])
        except Exception as e:
            self.etc.log(e)
            
        
class phot():
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = myEnv.etc(verb=self.verb)
        self.fop = myEnv.file_op(verb=self.verb)
        self.calc = calc(verb=self.verb)
        
    def do(self, data, x_coor, y_coor, aper_radius=10.0, gain=1.21):
        self.etc.log("Starting Photometry")
        try:
            bkg = Background(data)
            data_sub = data - bkg
            flux, fluxerr, flag = sum_circle(data_sub, x_coor, y_coor,
                                             aper_radius, err=bkg.globalrms,
                                             gain=gain)
            return(flux, fluxerr, flag)
        except Exception as e:
            self.eetc.log(e)
        
    def do_mag(self, data, x_coor, y_coor, aper_radius=10.0, gain=1.21):
        self.etc.log("Starting (MAG) Photometry")
        try:
            flux, fluxerr, flag = self.do(data, x_coor,
                                          y_coor, aper_radius=10.0, gain=1.21)
            return(calc.flux2magmerr(self, flux, fluxerr))
        except Exception as e:
            self.etc.log(e)
            
class time():
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = myEnv.etc(verb=self.verb)
        self.fop = myEnv.file_op(verb=self.verb)
        self.calc = calc(verb=self.verb)
        
    def time_stamp(self, utc=False):
        try:
            if utc:
                return(str(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")))
            else:
                return(str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S")))
        except Exception as e:
            self.eetc.log(e)
    
    def jd(self, utc=False):
        try:
            return(self.calc.jd(self.time_stamp(utc=utc)))
        except Exception as e:
            self.eetc.log(e)
        
    def mjd(self, utc=False):
        try:
            return(self.calc.mjd(self.time_stamp(utc=utc)))
        except Exception as e:
            self.eetc.log(e)
        
class sextractor():
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = myEnv.etc(verb=self.verb)
        
    def find(self, data, threshold=1.5, table=True, only_best=True):
        try:
            bkg = Background(data)
            data_sub = data - bkg
            all_objects = asarray(extract(data_sub, threshold,
                                          err=bkg.globalrms))
            if only_best:
                all_objects = all_objects[all_objects['flag'] == 0]
                
            if table:            
                return(TBL(all_objects))
            else:
                return(all_objects)
        except Exception as e:
            self.etc.log(e)
            
    def find_limited(self, data, threshold=1.5, table=True,
                     only_best=True, max_sources=200):
        try:
            bkg = Background(data)
            data_sub = data - bkg
            all_objects = asarray(extract(data_sub, threshold,
                                          err=bkg.globalrms))
            if only_best:
                all_objects = all_objects[all_objects['flag'] == 0]
            
            ord_objects = nsort(all_objects, order=['flux'])
            
            if len(ord_objects) <= max_sources:
                max_sources = len(ord_objects)
                objects = ord_objects[::-1][:max_sources]
            if len(ord_objects) > max_sources:
                objects = ord_objects[::-1][:max_sources]
            elif not max_sources:
                objects = ord_objects[::-1]
                
            if table:            
                return(TBL(objects))
            else:
                return(objects)
        except Exception as e:
            self.etc.log(e)
            
    def extract_xy(self, src):
        try:
            return(TBL([src['x'], src['y']]))
        except Exception as e:
            self.etc.log(e)
              
class cat():
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = myEnv.etc(verb=self.verb)
        
    def gaia(self, ra, dec, radius=0.0027, max_mag=20,
                   max_coo_err=1, max_sources=1):
        self.etc.log("Getting data from Gaia for ra({}), dec({}) and radius({})".format(ra, dec, radius))
        try:
            field = coordinates.SkyCoord(ra=ra,dec=dec,
                                               unit=(U.deg, U.deg),
                                               frame='icrs')
            
            vquery = Vizier(columns=['Source', 'RA_ICRS', 'DE_ICRS',
                                     'e_RA_ICRS','e_DE_ICRS',
                                     'phot_g_mean_mag', 'pmRA', 'pmDE',
                                     'e_pmRA', 'e_pmDE', 'Epoch', 'Plx'],
                row_limit=max_sources)
            
            return(vquery.query_region(field, width="{:f}d".format(radius),
                                       catalog="I/337/gaia")[0])
        except Exception as e:
            self.etc.log(e)
            
    def nomad(self, ra, dec, radius=0.0027, min_mag=10,
              max_mag=20, max_sources=1):
        self.etc.log("Getting data from Nomad for ra({}), dec({}) and radius({})".format(ra, dec, radius))
        try:
            c = coordinates.SkyCoord(ra, dec,
                                           unit=(U.deg, U.deg),
                                           frame='icrs')
            r = radius * U.deg

            vquery = Vizier(columns=['NOMAD1', 'RAJ2000', 'DEJ2000', 'Bmag',
                                     'Vmag', 'Rmag'], row_limit=max_sources)

            result = vquery.query_region(c, radius=r, catalog="NOMAD")[0]

            return(result)
        except Exception as e:
            self.etc.log(e)
            
    def usno(self, ra, dec, radius=0.0027, min_mag=10,
              max_mag=20, max_sources=1):
        self.etc.log("Getting data from Usno for ra({}), dec({}) and radius({})".format(ra, dec, radius))
        try:
            c = coordinates.SkyCoord(ra, dec,
                                           unit=(U.deg, U.deg),
                                           frame='icrs')
            r = radius * U.deg

            vquery = Vizier(columns=['USNO', 'RAJ2000', 'DEJ2000', 'Bmag',
                                     'Rmag'], row_limit=max_sources)

            result = vquery.query_region(c, radius=r, catalog="USNO-A2.0")[0]

            return(result)
        except Exception as e:
            self.etc.log(e)

