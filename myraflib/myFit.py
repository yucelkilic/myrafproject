# -*- coding: utf-8 -*-

from pyraf.iraf import noao
from pyraf.iraf import imred
from pyraf.iraf import ccdred
from pyraf.iraf import digiphot
from pyraf.iraf import apphot

from pyraf.iraf import hedit
from pyraf.iraf import imaccess
from pyraf.iraf import rfits
from pyraf.iraf import imstatistics
from pyraf.iraf import zerocombine as zc
from pyraf.iraf import darkcombine as dc
from pyraf.iraf import flatcombine as fc
from pyraf.iraf import imshift as imsh
from pyraf.iraf import ccdproc as cp

from pyraf.iraf import datapars
from pyraf.iraf import centerpars
from pyraf.iraf import fitskypars
from pyraf.iraf import photpars
from pyraf.iraf import phot as pt
from pyraf.iraf import txdump

from shutil import rmtree

import alipy
import glob

from . import myEnv
from . import cosmics


class etc():

    def __init__(self, verb=True):
        self.verb = verb
        self.meetc = myEnv.etc(verb=self.verb)
        self.mefop = myEnv.file_operation(verb=self.verb)

    def is_fits(self, file_name):
        ret = False
        if self.mefop.is_file(file_name):
            if imaccess(file_name) == 1:
                ret = True
            else:
                self.meetc.print_if("%s:Not a valid FIT(S) file" % (file_name))

        return ret


class statistics_operation():

    def __init__(self, verb=True):
        self.verb = verb
        self.meetc = myEnv.etc(verb=self.verb)
        self.mefo = myEnv.file_operation(verb=self.verb)
        self.etc = etc(verb=self.verb)
        self.fo = fits_operation(verb=self.verb)

    def get_stats_object(self, in_file, coords):
        self.meetc.print_if("Getting statistics for source(%s-%s) in file(%s)"
            % (coords[0], coords[1], in_file))
        ret = [False, None]
        try:
            tmp_dir = self.mefo.get_tmp_dir()
            if tmp_dir[0]:
                coos = open("%s/coors" % (tmp_dir[1]), "w")
                coos.write("%s %s 1" % (coords[0], coords[1]))
                coos.close()
                stat = self.fo.assoc_photometry(in_file,
                    "%s/coors" % (tmp_dir[1]), 15)
                if stat[0]:
                    ret = [True, [coords[0], coords[1], stat[1][4]]]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_stats(self, in_files):
        self.meetc.print_if("Getting statistics for files")
        ret = [False, None]
        vals = []
        try:
            for i in in_files:
                self.meetc.print_if("Getting stats forfile(%s)" % (i))
                stat = imstatistics(i, Stdout=1)[1].split()
                vals.append(stat)

            ret = [True, vals]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_sources(self, in_file, count=25):
        self.meetc.print_if("Finding source(s)(%s) for file(%s)" % (
            count, in_file))
        ret = [False, None]
        source_list = []
        try:
            images_to_align = sorted(glob.glob(in_file))
            ref_image = in_file
            ids = alipy.ident.run(ref_image, images_to_align,
                n=int(count), visu=False, verbose=False)
            for i in ids:
                if i.ok:
                    for u in i.ukn.starlist:
                        tmp_coor = str(u).split("|")[0].split(":")[1].replace(
                            "(", "").replace(")", "")
                        coors = [float(tmp_coor.split(",")[0].strip()),
                            float(tmp_coor.split(",")[1].strip())]
                        tmp_flux = str(u).split("|")[2].split()
                        flux = float(tmp_flux[0])
                        source_list.append([coors[0], coors[1], flux])

            ret = [True, source_list]
        except Exception as e:
            self.meetc.print_if(e)

        return ret


class header_operation():

    def __init__(self, verb=True):
        self.verb = verb
        self.meetc = myEnv.etc(verb=self.verb)
        self.mefop = myEnv.file_operation(verb=self.verb)
        self.etc = etc(verb=self.verb)

    def get_header(self, file_name, header):
        ret = [False, None]
        self.meetc.print_if("Getting header(%s) for file(%s)" % (
            header, file_name))
        try:
            if self.does_header_exist(file_name, header):
                h = self.get_list_header(file_name)
                if h[0]:
                    for i in h[1]:
                        if i[0] == header:
                            ret = [True, i[1]]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def get_list_header(self, file_name):
        ret = [False, None]
        self.meetc.print_if("Getting list of headers for file(%s)" % (
            file_name))
        if self.etc.is_fits(file_name):
            try:
                lst = []
                im_header = hedit(file_name, "*", ".", Stdout=1)
                for i in im_header:
                    try:
                        head = i.split(",")
                        key, value = head[1].split(" = ")
                        lst.append([key.strip(), value.strip()])
                    except:
                        self.meetc.print_if(
                            "Can not get value from header(%s). Skipping" % (i))
                ret = [True, lst]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def does_header_exist(self, file_name, key):
        ret = False
        self.meetc.print_if("Checking for header(%s) in file(%s)" % (
            key, file_name))
        all_headers = self.get_list_header(file_name)
        if all_headers[0]:
            for i in all_headers[1]:
                if key.upper() == i[0].upper():
                    ret = True

        if ret:
            self.meetc.print_if("Header '%s' DOES exist in file('%s')" %
                (key, file_name))
        else:
            self.meetc.print_if("Header '%s' DOES NOT exist in file('%s')" %
                (key, file_name))
        return ret

    def add_update_header(self, file_name, key, value):
        ret = False
        self.meetc.print_if("Adding header(%s) with value(%s) to file(%s)" % (
            value, key, file_name))
        try:
            if self.etc.is_fits(file_name):
                if self.does_header_exist(file_name, key):
                    self.meetc.print_if("Going for an update")
                else:
                    self.meetc.print_if("Going to add it")

                hedit(file_name, key, value, add="yes", verify="no",
                    show="no", update="yes")
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def delete_header(self, file_name, key):
        ret = False
        self.meetc.print_if("Deleting header(%s) from file(%s)" % (
            file_name, key))
        try:
            if self.etc.is_fits(file_name):
                if self.does_header_exist(file_name, key):
                    hedit(file_name, key, delete="yes", verify="no",
                        show="no", update="yes")
                    ret = True
                else:
                    self.meetc.print_if(
                        "No header key '%s' fount in file '%s'" % (
                            key, file_name))
                    ret = False
        except Exception as e:
            self.meetc.print_if(e)

        return ret


class fits_operation():

    def __init__(self, verb=True):
        self.verb = verb
        self.meetc = myEnv.etc(verb=self.verb)
        self.mefo = myEnv.file_operation(verb=self.verb)
        self.ho = header_operation(verb=self.verb)

    def convert_to_fits(self, in_file, out_file):
        ret = False
        self.meetc.print_if("Converting file(%s) to IRAF file" % (in_file))
        try:
            if self.mefo.is_file(in_file):
                rt = rfits(in_file, "", out_file, Stdout=1)
                if not len(rt) == 1:
                    ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def cosmic_clean(self, file_name, out_file_name, mask=True, gain=2.2,
        readnoise=10.0, sigclip=5.0, sigfrac=0.3, objlim=5.0):
        ret = False
        self.meetc.print_if("%s%s%s" % (
            "Cosmic Cleaning rays from file(%s) with " % (file_name),
        "settings(mask:%s, gain:%s, read_noise:%s, sigma_" % (mask, gain,
        readnoise),
            "clip:%s, sigma_fraction:%s, object_limit:%s)" % (sigclip, sigfrac,
            objlim)))

        try:
            array, header = cosmics.fromfits(file_name)
            cleaned = cosmics.cosmicsimage(array, gain=gain,
                readnoise=readnoise, sigclip=sigclip, sigfrac=sigfrac,
                objlim=objlim)
            cleaned.run(maxiter=4)
            cosmics.tofits(out_file_name, cleaned.cleanarray, header)
            if mask:
                fne = out_file_name.split(".")
                cosmics.tofits("%s._mask.fit" % (fne[0]),
                    cleaned.mask, header)
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def zerocombine(self, file_list, out_file, combine="median",
        reject="minmax", ccdtype=""):
        file_list_str = self.meetc.join_list_items_to_string(file_list)
        self.meetc.print_if("%s%s" % (
            "Zercombining files:(%s) with " % (file_list_str[1]),
            "settings(combine:%s, reject:%s, ccdtype:%s)" % (combine,
                reject, ccdtype)))
        ret = False
        tmp_dir = self.mefo.get_tmp_dir()
        if tmp_dir[0]:
            if self.mefo.write_list_to_file(file_list, "%s/%s" % (
                tmp_dir[1], "bias_list")):
                zc.input = "@%s/%s" % (tmp_dir[1], "bias_list")
                zc.output = out_file
                zc.combine = combine
                zc.reject = reject
                zc.ccdtype = ccdtype
                zc.process = "no"
                try:
                    zc._runCode()
                    ret = True
                except Exception as e:
                    self.meetc.print_if(e)

        return ret

    def darkcombine(self, file_list, out_file, combine="median",
                    reject="minmax", scale="exposure", ccdtype=""):
        file_list_str = self.meetc.join_list_items_to_string(file_list)
        self.meetc.print_if("%s%s" % (
            "Darkcombining files:(%s) with " % (file_list_str[1]),
            "settings(combine:%s, reject:%s, scale:%s, ccdtype:%s)" % (
                combine, reject, scale, ccdtype)))
        ret = False
        tmp_dir = self.mefo.get_tmp_dir()
        if tmp_dir[0]:
            if self.mefo.write_list_to_file(file_list, "%s/%s" % (
                tmp_dir[1], "dark_list")):
                dc.input = "@%s/%s" % (tmp_dir[1], "dark_list")
                dc.output = out_file
                dc.combine = combine
                dc.reject = reject
                dc.ccdtype = ccdtype
                dc.scale = scale
                dc.process = "no"
                try:
                    dc._runCode()
                    ret = True
                except Exception as e:
                    self.meetc.print_if(e)

        return ret

    def flatcombine(self, file_list, out_dir, combine="median",
        reject="minmax", subset="no", ccdtype=""):
        file_list_str = self.meetc.join_list_items_to_string(file_list)
        self.meetc.print_if("%s%s" % (
            "Flatcombining files:(%s) with " % (file_list_str[1]),
            "settings(combine:%s, reject:%s, subset:%s, ccdtype:%s)" % (
                combine, reject, subset, ccdtype)))
        ret = False
        tmp_dir = self.mefo.get_tmp_dir()
        if tmp_dir[0]:
            if self.mefo.write_list_to_file(file_list, "%s/%s" % (
                tmp_dir[1], "flat_list")):
                fc.input = "@%s/%s" % (tmp_dir[1], "flat_list")
                if subset == "yes":
                    fc.output = "%s/flat_" % (out_dir)
                else:
                    fc.output = out_dir
                fc.combine = combine
                fc.reject = reject
                fc.subset = subset
                fc.ccdtype = ccdtype
                fc.process = "no"
                try:
                    fc._runCode()
                    ret = True
                except Exception as e:
                    self.meetc.print_if(e)

        return ret

    def calibration(self, in_file, out_file, bias_file, dark_file, flat_file,
        ccdty="", subs="no"):
        ret = False
        bia = "yes"
        dar = "yes"
        fla = "yes"
        if bias_file == "":
            bia = "no"
        if dark_file == "":
            dar = "no"
        if flat_file == "":
            fla = "no"

        self.meetc.print_if("%s%s" % ("Calibrating file:(%s) with " % (in_file),
        "settings bias:%s(%s), dark:%s(%s), flat:%s(%s), ccdtype:%s, subset:%s"
        % (bia, bias_file, dar, dark_file, fla, flat_file, ccdty, subs)))

        cp.images = in_file
        cp.output = out_file
        cp.ccdtype = ccdty
        cp.fixpix = "no"
        cp.overscan = "no"
        cp.trim = "no"
        cp.zerocor = bia
        cp.darkcor = dar
        cp.flatcor = fla
        cp.zero = bias_file
        cp.dark = dark_file
        cp.flat = flat_file
        try:
            cp(images=str(in_file))
            self.ho.add_update_header(out_file, "MyCal",
                "Calibrated Via MYRaf V3.0 Beta @ %s" % (
                    self.meetc.time_stamp()))
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def manual_align(self, in_file, diff_x, diff_y, out_file):
        self.meetc.print_if("Aligning file(%s) with (%s,%s) coordinates" % (
            in_file, diff_x, diff_y))
        ret = False
        try:
            imsh(in_file, out_file, int(diff_x), int(diff_y))
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def auto_align(self, in_file, ref_image, out_dir):
        self.meetc.print_if("Aligning file(%s) with reference(%s)" % (
            in_file, ref_image))
        ret = False
        out_file = None
        try:
            pfn = self.mefo.get_base_name(in_file)
            if pfn[0]:
                out_file = "%s/%s" % (out_dir, pfn[1][1])
            images_to_align = sorted(glob.glob(in_file))
            identifications = alipy.ident.run(ref_image, images_to_align,
                visu=False)
            outputshape = alipy.align.shape(ref_image)
            for id in identifications:
                if id.ok is True:
                    alipy.align.affineremap(id.ukn.filepath, id.trans,
                        shape=outputshape, alifilepath=out_file, outdir=out_dir,
                        makepng=False, verbose=False)
            ret = True
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def assoc_photometry(self, in_file, param_file, aper):
        ret = [False, None]
        self.meetc.print_if(
            "Assoc will work for image(%s) using settings(%s)" % (
                in_file, param_file))
        try:
            ana_dir = self.mefo.get_analyzed_dir()
            if ana_dir[0]:
                alipy.pysex.run(in_file, keepcat=True,
                    rerun=True, catdir=ana_dir[1],
                    params=['VECTOR_ASSOC(1)', 'MAG_BEST', 'FLUX_BEST',
                        'MAGERR_BEST', 'FLAGS', 'FWHM_IMAGE'],
                    conf_args={'VERBOSE_TYPE': 'QUIET', 'DETECT_THRESH': 3.0,
                        'ANALYSIS_THRESH': 3.0, 'BACKPHOTO_TYPE': 'LOCAL',
                        'BACKPHOTO_THICK': 24, 'ASSOC_RADIUS': aper,
                        'ASSOC_PARAMS': '1,2', 'ASSOC_DATA': '3',
                        'ASSOC_NAME': param_file})

                pfn = self.mefo.get_base_name(in_file)
                if pfn[0]:
                    ext = self.mefo.get_extension(in_file)
                    if ext[0]:
                        fl_name = pfn[1][1].replace(ext[1], ".pysexcat")
                        fil_path = "%s/%s" % (ana_dir[1], fl_name)
                        vals = open(fil_path, "r")
                        for val in vals:
                            line = val.replace("\n", "")
                            if not line.startswith("#"):
                                ret_vals = line.split()
                                ret = [True, ret_vals]

        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def photometry(self, in_file, out_file, coords, ape, ann, dan, cbox,
            time, exptime, zmag, gain, filtr):
        ret = [False, None]
        md = self.mefo.get_myraf_dir()
        if md[0]:
            datapars.setParam("exposur", exptime)
            #datapars.setParam("filter", filtr)
            #datapars.setParam("airmass", "airmass")
            datapars.setParam("obstime", time)
            datapars.setParam("gain", gain)
            datapars.saveParList(
                filename="%s/uparm/aptdataps.par" % (md[1]))

            centerpars.setParam("cbox", cbox)
            centerpars.saveParList(
                filename="%s/uparm/aptcentes.par" % (md[1]))

            fitskypars.setParam("annulus", ann)
            fitskypars.setParam("dannulus", dan)
            fitskypars.saveParList(
                filename="%s/uparm/aptfitsks.par" % (md[1]))

            photpars.setParam("apertur", ape)
            photpars.setParam("zmag", zmag)
            photpars.saveParList(
                filename="%s/uparm/aptphot.par" % (md[1]))

            ana_dir = self.mefo.get_analyzed_dir()
            tmp_dir = self.mefo.get_tmp_dir()
            if ana_dir[0] and tmp_dir[0]:
                try:
                    if self.mefo.write_list_to_file(coords, "%s/%s" % (
                        tmp_dir[1], "coors")):
                        pfn = self.mefo.get_base_name(in_file)
                        if pfn[0]:
                            tx_file = "%s/%s.mag.1" % (ana_dir[1], pfn[1][1])
                            if self.mefo.is_file(tx_file):
                                self.mefo.delete_file(tx_file)
                            pt(in_file, coords="%s/%s" % (tmp_dir[1], "coors"),
                                output="%s/" % (ana_dir[1]), interac="no",
                                verify="no", Stdout=1)
                            td = self.tx_dump(tx_file, out_file)
                            if td[0]:
                                ret = [True, td[1]]
                except Exception as e:
                    self.meetc.print_if(e)

        return ret

    def tx_dump(self, in_file, out_file, fields="id, otime, mag, merr"):
        ret = [False, None]
        try:
            vals = txdump(in_file, fields, "yes", Stdout=1)
            ret = [True, vals]
        except Exception as e:
            self.meetc.print_if(e)

        return ret
