# -*- coding: utf-8 -*-

from . import myFit
from . import myEnv

from pyraf.iraf import noao
from pyraf.iraf import astutil
from pyraf.iraf import asthedit

from astropy.time import Time
from time import strftime

from pyraf.iraf import setairmass as sam


class etc():

    def __init__(self, verb=True):
        self.verb = verb

    def is_close(self, in_val, comparison_val, tolerance=0.01):
        return (in_val + tolerance) >= comparison_val >= (in_val - tolerance)


class time_calculation():

    def __init__(self, verb=True):
        self.verb = verb
        self.mfho = myFit.header_operation(verb=self.verb)
        self.meetc = myEnv.etc(verb=self.verb)
        self.mefo = myEnv.file_operation(verb=self.verb)

    def get_epoch(self, in_file, time, date, timestamp=False):
        ret = [False, None]

        obs_time = self.mfho.get_header(in_file, time)
        if timestamp:
            if obs_time[0]:
                use_time, use_date = obs_time[1].split(date)
        else:
            obs_date = self.mfho.get_header(in_file, date)
            if obs_time[0] and obs_date[0]:
                use_time = obs_time[1]
                use_date = obs_date[1]

        if 'use_time' in locals():
            if 'use_date' in locals():
                try:
                    t = Time(strftime(
                        '%s %s' % (
                            use_time, use_date)), format='iso', scale='utc')
                    ret = [True, t.byear]
                except Exception as e:
                    self.meetc.print_if(e)
            else:
                self.meetc.print_if("Can not resolve date.")
        else:
            self.meetc.print_if("Can not resolve time.")

        return ret

    def get_sidereal(self, in_file, observat, time, date, timestamp=False):
        ret = [False, None]

        obs_time = self.mfho.get_header(in_file, time)
        if timestamp:
            if obs_time[0]:
                use_time, use_date = obs_time[1].split(date)
        else:
            obs_date = self.mfho.get_header(in_file, date)
            if obs_time[0] and obs_date[0]:
                use_time = obs_time[1]
                use_date = obs_date[1]

        if 'use_time' in locals():
            if 'use_date' in locals():
                try:
                    obs = self.mefo.get_values_from_obs_file(observat.lower())
                    if obs[0]:
                        lo, la = obs[1]['longitude'], obs[1]['latitude']
                        t = Time(strftime('%s %s' % (use_time, use_date)),
                            format='iso', scale='utc', location=(
                                '%sd' % (lo), '%sd' % (la)))
                        ret = [True, t.sidereal_time('mean').value]
                except Exception as e:
                    self.meetc.print_if(e)
            else:
                self.meetc.print_if("Can not resolve date.")
        else:
            self.meetc.print_if("Can not resolve time.")

        return ret

    def set_airmass(self, in_file, observat="observat", rightascension="ra",
            declination="dec", equinox="epoch", sidereal_time="st",
            u_time="ut", dat="date", exposure="exptime"):
        ret = False
        do_it = True
        try:
            if do_it and self.mfho.does_header_exist(in_file, observat):
                do_it = True
            else:
                do_it = False
                self.meetc.print_if("No Header(%s) found in file(%s)" % (
                    in_file, observat))

            if do_it and self.mfho.does_header_exist(in_file, rightascension):
                do_it = True
            else:
                do_it = False
                self.meetc.print_if("No Header(%s) found in file(%s)" % (
                    in_file, rightascension))

            if do_it and self.mfho.does_header_exist(in_file, declination):
                do_it = True
            else:
                do_it = False
                self.meetc.print_if("No Header(%s) found in file(%s)" % (
                    in_file, declination))

            if do_it and self.mfho.does_header_exist(in_file, equinox):
                do_it = True
            else:
                do_it = False
                self.meetc.print_if("No Header(%s) found in file(%s)" % (
                    in_file, equinox))

            if do_it and self.mfho.does_header_exist(in_file, sidereal_time):
                do_it = True
            else:
                do_it = False
                self.meetc.print_if("No Header(%s) found in file(%s)" % (
                    in_file, sidereal_time))

            if do_it and self.mfho.does_header_exist(in_file, u_time):
                do_it = True
            else:
                do_it = False
                self.meetc.print_if("No Header(%s) found in file(%s)" % (
                    in_file, u_time))

            if do_it and self.mfho.does_header_exist(in_file, dat):
                do_it = True
            else:
                do_it = False
                self.meetc.print_if("No Header(%s) found in file(%s)" % (
                    in_file, dat))

            if do_it and self.mfho.does_header_exist(in_file, exposure):
                do_it = True
            else:
                do_it = False
                self.meetc.print_if("No Header(%s) found in file(%s)" % (
                    in_file, exposure))

            if do_it:
                sam(in_file, observatory=observat, intype ="middle",
                    outtype="effective", ra=rightascension, dec=declination,
                    equinox=equinox, st=sidereal_time, ut=u_time, date=dat, exposur=exp)



            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret
