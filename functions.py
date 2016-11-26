# -*- coding: utf-8 -*-

from myraflib import myEnv


from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import Comment

import multiprocessing


class multi_proc():

    def __init__(self, verb):
        self.verb = verb
        self.max_cpu = multiprocessing.cpu_count()


class settings():

    def __init__(self, verb=True):
        self.verb = verb
        self.mefop = myEnv.file_operation(verb=self.verb)
        self.meetc = myEnv.etc(verb=self.verb)

    def prettify(self, elem):
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def create_settings(self, set_name, gen_cpus="1",
        cal_zero_comb="1", cal_zero_rejc="1", cal_zero_ccdt=" ",
        cal_dark_comb="1", cal_dark_rejc="1", cal_dark_scale="0",
        cal_dark_ccdt=" ", cal_flat_comb="1", cal_flat_rejc="1",
        cal_flat_subs="0", cal_flat_ccdt=" ", cal_cali_subs="0",
        cal_cali_ccdt=" ", phot_fsp_anna="25", phot_fsp_dand="5",
        phot_fsp_cbox="10", phot_dpe_xpti="exptime", phot_dpt_filt="subset",
        phot_php_aper="10,15,20,25,30", phot_php_zmag="25",
        phot_php_gain="gain", phot_php_fxpx=" ", phot_wcs_raa="ra",
        phot_wcs_dec="dec", phot_lot_obse="observat", phot_lot_tmsp="f",
        phot_lot_time="time-obs", phot_lot_date="date-obs", phot_lot_epca="f",
        phot_lot_epch="Epoch", phot_stf_fxra="2", phot_stf_mnfh="4",
        phot_stf_mxfh="9", phot_stf_mstf="25", phot_hex="subset",
        phot_ccl_acmf="t", phot_ccl_gain="2.2", phot_ccl_rnoi="10",
        phot_ccl_scli="5", phot_ccl_sfra="0.3", phot_ccl_olim="5",
        phot_wct_serv="http://nova.astrometry.net/api/", phot_wct_apke="apiKey",
        phot_wct_befl="Compress",
        phot_wct_abap="t", phot_wct_scli="f"):

        ret = False

        top = Element("Settings")
        comment = Comment('%s settings for MYRaf' % (set_name))
        top.append(comment)
        name = SubElement(top, 'Name')
        name.text = set_name
        comment = Comment('Name of setting')
        name.append(comment)

        if True:
            general = SubElement(top, 'General')
            comment = Comment('General top settings for MYRaf')
            general.append(comment)
            if True:
                cpu = SubElement(general, 'CPU')
                comment = Comment('CPU settings for MYRaf')
                cpu.append(comment)

                cpus = SubElement(cpu, 'CPUs')
                cpus.text = gen_cpus

            if True:

                calibration = SubElement(top, 'Calibration')
                comment = Comment('Calibration top settings for MYRaf')
                calibration.append(comment)

                if True:
                    zerocombine = SubElement(calibration, 'Zerocombine')
                    comment = Comment('Zerocombine settings for MYRaf')
                    zerocombine.append(comment)
                    zero_zerocom = SubElement(zerocombine, 'zero_zerocom')
                    comment = Comment('Combine type: 0=median, 1=average')
                    zero_zerocom.append(comment)
                    zero_zerocom.text = cal_zero_comb
                    zero_reject = SubElement(zerocombine, 'zero_reject')
                    comment = Comment("Rejection: %s%s" % (
                        'Rejection type: 0=none, 1=minmax, 2=ccdclip,',
                        '3=crreject, 4=sigclip, 5=avsigclip, 6=pclip'))
                    zero_reject.append(comment)
                    zero_reject.text = cal_zero_rejc
                    zero_ccdtype = SubElement(zerocombine, 'zero_ccdtype')
                    comment = Comment('Header specifier')
                    zero_ccdtype.append(comment)
                    zero_ccdtype.text = cal_zero_ccdt

                if True:
                    darkcombine = SubElement(calibration, 'Darkcombine')
                    comment = Comment('Darkcombine settings for MYRaf')
                    darkcombine.append(comment)
                    dark_darkcom = SubElement(darkcombine, 'dark_darkcom')
                    comment = Comment('Combine type: 0=median, 1=average')
                    dark_darkcom.append(comment)
                    dark_darkcom.text = cal_dark_comb
                    dark_reject = SubElement(darkcombine, 'dark_reject')
                    comment = Comment("Rejection: %s%s" % (
                        'Rejection type: 0=none, 1=minmax, 2=ccdclip,',
                        '3=crreject, 4=sigclip, 5=avsigclip, 6=pclip'))
                    dark_reject.append(comment)
                    dark_reject.text = cal_dark_rejc
                    dark_scale = SubElement(darkcombine, 'dark_scale')
                    comment = Comment("Scale: %s%s" % (
                        'Scale type: 0=exposure, 1=none,',
                        '2=mode, 3=median, 4=mean'))
                    dark_scale.append(comment)
                    dark_scale.text = cal_dark_scale
                    dark_ccdtype = SubElement(darkcombine, 'dark_ccdtype')
                    comment = Comment('Header specifier')
                    dark_ccdtype.append(comment)
                    dark_ccdtype.text = cal_dark_ccdt

                if True:
                    flatcombine = SubElement(calibration, 'Flatcombine')
                    comment = Comment('Flatcombine settings for MYRaf')
                    flatcombine.append(comment)
                    flat_flatcom = SubElement(flatcombine, 'flat_flatcom')
                    comment = Comment('Combine type: 0=median, 1=average')
                    flat_flatcom.append(comment)
                    flat_flatcom.text = cal_flat_comb
                    flat_reject = SubElement(flatcombine, 'flat_reject')
                    comment = Comment("Recetion: %s%s" % (
                        'Rejection type: 0=none, 1=minmax, 2=ccdclip,',
                        '3=crreject, 4=sigclip, 5=avsigclip, 6=pclip'))
                    flat_reject.append(comment)
                    flat_reject.text = cal_flat_rejc
                    flat_subset = SubElement(flatcombine, 'flat_subset')
                    comment = Comment('Select by Filter: t=yes, f=no')
                    flat_subset.append(comment)
                    flat_subset.text = cal_flat_subs
                    flat_ccdtype = SubElement(flatcombine, 'flat_ccdtype')
                    comment = Comment('Header specifier')
                    flat_ccdtype.append(comment)
                    flat_ccdtype.text = cal_flat_ccdt

                if True:
                    Calib = SubElement(calibration, 'Calib')
                    comment = Comment('Calibration settings for MYRaf')
                    Calib.append(comment)
                    cal_subset = SubElement(Calib, 'cal_subset')
                    comment = Comment('Select by Filter: t=yes, f=no')
                    cal_subset.append(comment)
                    cal_subset.text = cal_cali_subs
                    cal_ccdtype = SubElement(Calib, 'cal_ccdtype')
                    comment = Comment('Header specifier')
                    cal_ccdtype.append(comment)
                    cal_ccdtype.text = cal_cali_ccdt

            if True:
                photometry = SubElement(top, 'Photometry')
                comment = Comment('Photometry top settings for MYRaf')
                photometry.append(comment)
                if True:
                    fitskypar = SubElement(photometry, 'FitSkyPar')
                    comment = Comment('Fit Sky Parameters settings for MYRaf')
                    fitskypar.append(comment)
                    annulus = SubElement(fitskypar, 'Annulus')
                    comment = Comment('An integer for annulus value')
                    annulus.append(comment)
                    annulus.text = phot_fsp_anna
                    dannulus = SubElement(fitskypar, 'Dannulus')
                    comment = Comment('An integer for Dannulus value')
                    dannulus.append(comment)
                    dannulus.text = phot_fsp_dand
                    cbox = SubElement(fitskypar, 'cbox')
                    comment = Comment('An integer for Centering Box value')
                    cbox.append(comment)
                    cbox.text = phot_fsp_cbox

                if True:
                    datapar = SubElement(photometry, 'Datapar')
                    comment = Comment('Data Parameters settings for MYRaf')
                    datapar.append(comment)
                    exposure = SubElement(datapar, 'Exposure')
                    comment = Comment('Where to find EXPOSURE value in header')
                    exposure.append(comment)
                    exposure.text = phot_dpe_xpti
                    filtr = SubElement(datapar, 'Filter')
                    comment = Comment('Where to find FILTER value in header')
                    filtr.append(comment)
                    filtr.text = phot_dpt_filt

                if True:
                    photpar = SubElement(photometry, 'PhotoPar')
                    comment = Comment(
                        'Photometry Parameters settings for MYRaf')
                    photpar.append(comment)
                    aperture = SubElement(photpar, 'Aperture')
                    comment = Comment('List of Aperture values. Like: 15,20,25')
                    aperture.append(comment)
                    aperture.text = phot_php_aper
                    zmag = SubElement(photpar, 'ZMag')
                    comment = Comment('An integer for Zero point of magnitude')
                    zmag.append(comment)
                    zmag.text = phot_php_zmag
                    gain = SubElement(photpar, 'Gain')
                    comment = Comment('Where to find GAIN value in header')
                    gain.append(comment)
                    gain.text = phot_php_gain
                    fixpix = SubElement(photpar, 'FixPix')
                    comment = Comment('DixPix area')
                    fixpix.append(comment)
                    fixpix.text = phot_php_fxpx

                if True:
                    wcs = SubElement(photometry, 'WCS')
                    comment = Comment('WCS Parameters settings for MYRaf')
                    wcs.append(comment)
                    rightascension = SubElement(wcs, 'RightAscension')
                    comment = Comment(
                        'Where to find RIGHTASCENSION value in header')
                    rightascension.append(comment)
                    rightascension.text = phot_wcs_raa
                    declination = SubElement(wcs, 'Declination')
                    comment = Comment(
                        'Where to find DECLINATION value in header')
                    rightascension.append(comment)
                    declination.text = phot_wcs_dec

                if True:
                    location_time = SubElement(photometry, 'LocationAndTime')
                    comment = Comment('Location and Time settings for MYRaf')
                    location_time.append(comment)
                    observatory = SubElement(location_time, 'Observatory')
                    comment = Comment(
                        'Where to find OBSERVATORY value in header')
                    observatory.append(comment)
                    observatory.text = phot_lot_obse
                    timestamp = SubElement(location_time, 'Timestamp')
                    comment = Comment('Using Timestamp? t=yes f=no.')
                    timestamp.append(comment)
                    timestamp.text = phot_lot_tmsp
                    timeobs = SubElement(location_time, 'TimeOBS')
                    comment = Comment("%s%s" % (
                        'Where to find OBSERVATION TIME value in header.',
                        'If Timestamp=yes than OBSERVATION TIMESTAMP'))
                    timeobs.append(comment)
                    timeobs.text = phot_lot_time
                    dateobs = SubElement(location_time, 'DateOBS')
                    comment = Comment("%s%s" % (
                        'Where to find OBSERVATION TIME value in header.',
                        'If Timestamp=yes than SEPERATOR'))
                    dateobs.append(comment)
                    dateobs.text = phot_lot_date
                    epoch_calc = SubElement(location_time, 'EpochCalculator')
                    comment = Comment('Calculate the Epoch. t=yes f=no')
                    epoch_calc.append(comment)
                    epoch_calc.text = phot_lot_epca
                    epoch = SubElement(location_time, 'Epoch')
                    comment = Comment('A float for epoch')
                    epoch.append(comment)
                    epoch.text = phot_lot_epch

                if True:
                    starfind = SubElement(photometry, 'StarFind')
                    comment = Comment('SExtractor settings for MYRaf')
                    starfind.append(comment)
                    fluxradi = SubElement(starfind, 'FluxRadius')
                    comment = Comment('An integer for FLUX RADIUS')
                    fluxradi.append(comment)
                    fluxradi.text = phot_stf_fxra
                    minfwhm = SubElement(starfind, 'MinFWHM')
                    comment = Comment('An integer for MINUMUM FWHM')
                    minfwhm.append(comment)
                    minfwhm.text = phot_stf_mnfh
                    maxfwhm = SubElement(starfind, 'MaxFWHM')
                    comment = Comment('An integer for MAXIMUM FWHM')
                    maxfwhm.append(comment)
                    maxfwhm.text = phot_stf_mxfh
                    mstf = SubElement(starfind, 'MaxStarsToFind')
                    comment = Comment('An integer for MAXIMUM STAR TO FIND')
                    mstf.append(comment)
                    mstf.text = phot_stf_mstf

                if True:
                    header_extractor = SubElement(photometry, 'HeaderExtractor')
                    comment = Comment('Header Extractor settings for MYRaf')
                    header_extractor.append(comment)
                    h_extract = SubElement(header_extractor, 'exract')
                    comment = Comment('List of headers to extract')
                    h_extract.append(comment)
                    h_extract.text = phot_hex

            if True:
                cosmic_cleaner = SubElement(top, 'CosmicCleaner')
                comment = Comment('Cosmic Cleaner top settings for MYRaf')
                cosmic_cleaner.append(comment)

                if True:
                    acmf = SubElement(cosmic_cleaner, 'AutoCreateMaskFile')
                    comment = Comment('Auto Create Mask File. t=yes f=no')
                    acmf.append(comment)
                    acmf.text = phot_ccl_acmf
                    gain = SubElement(cosmic_cleaner, 'Gain')
                    comment = Comment('A Float for Gain value')
                    gain.append(comment)
                    gain.text = phot_ccl_gain
                    read_noise = SubElement(cosmic_cleaner, 'ReadNoise')
                    comment = Comment('A Float for Read Noise value')
                    read_noise.append(comment)
                    read_noise.text = phot_ccl_rnoi
                    sigma_clip = SubElement(cosmic_cleaner, 'SigmaClip')
                    comment = Comment('A Float for Sigma Clip value')
                    sigma_clip.append(comment)
                    sigma_clip.text = phot_ccl_scli
                    sigma_frac = SubElement(cosmic_cleaner, 'SigmaFrac')
                    comment = Comment('A Float for Sigma Frac value')
                    sigma_frac.append(comment)
                    sigma_frac.text = phot_ccl_sfra
                    object_limit = SubElement(cosmic_cleaner, 'ObjectLimit')
                    comment = Comment('A Float for Object Limit value')
                    object_limit.append(comment)
                    object_limit.text = phot_ccl_olim

            if True:
                wcs_top = SubElement(top, 'WCS')
                comment = Comment('WCS top settings for MYRaf')
                wcs_top.append(comment)

                if True:
                    server = SubElement(wcs_top, 'Server')
                    comment = Comment('Server')
                    server.append(comment)
                    server.text = phot_wct_serv
                    apikey = SubElement(wcs_top, 'ApliKey')
                    comment = Comment('Api Key')
                    apikey.append(comment)
                    apikey.text = phot_wct_apke
                    beforeload = SubElement(wcs_top, 'BeforeLoad')
                    comment = Comment("%s%s" % (
                        'What to do before Upload.',
                        'Nothing, Compress and Binary'))
                    beforeload.append(comment)
                    beforeload.text = phot_wct_befl
                    aba = SubElement(wcs_top, 'AlignBeforeApplication')
                    comment = Comment('Align Before Application. t=yes f=no')
                    aba.append(comment)
                    aba.text = phot_wct_abap
                    sigma_clip = SubElement(wcs_top,
                        'CreateWCSHeadersSeparately')
                    comment = Comment("%s%s" % (
                        'Create WCS Headers Separately.', 't=yes f=no'))
                    sigma_clip.append(comment)
                    sigma_clip.text = phot_wct_scli

        ret = self.mefop.write_to_file("sessions/%s.set" % (set_name),
            self.prettify(top), "w", force=True)

        return ret

    def read_settings_name(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                name = root.find("Name")
                sett["name"] = name.text.strip()
                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_general_cpu(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                general = root.find("General")
                cpu = general.find("CPU")
                cpus = cpu.find("CPUs")
                sett["cpus"] = cpus.text.strip()
                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_calib_zerocombine(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Calibration")
                upset = up_upset.find("Zerocombine")

                cali_zero_comb = upset.find("zero_zerocom")
                sett["cali_zero_comb"] = cali_zero_comb.text.strip()

                cali_zero_reje = upset.find("zero_reject")
                sett["cali_zero_reje"] = cali_zero_reje.text.strip()

                cali_zero_ccty = upset.find("zero_ccdtype")
                sett["cali_zero_ccty"] = cali_zero_ccty.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_calib_darkcombine(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Calibration")
                upset = up_upset.find("Darkcombine")

                cali_dark_comb = upset.find("dark_darkcom")
                sett["cali_dark_comb"] = cali_dark_comb.text.strip()

                cali_dark_reje = upset.find("dark_reject")
                sett["cali_dark_reje"] = cali_dark_reje.text.strip()

                cali_dark_scal = upset.find("dark_scale")
                sett["cali_dark_scal"] = cali_dark_scal.text.strip()

                cali_dark_ccty = upset.find("dark_ccdtype")
                sett["cali_dark_ccty"] = cali_dark_ccty.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_calib_flatcombine(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Calibration")
                upset = up_upset.find("Flatcombine")

                cali_flat_comb = upset.find("flat_flatcom")
                sett["cali_flat_comb"] = cali_flat_comb.text.strip()

                cali_flat_reje = upset.find("flat_reject")
                sett["cali_flat_reje"] = cali_flat_reje.text.strip()

                cali_flat_subs = upset.find("flat_subset")
                sett["cali_flat_subs"] = cali_flat_subs.text.strip()

                cali_flat_ccty = upset.find("flat_ccdtype")
                sett["cali_flat_ccty"] = cali_flat_ccty.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_calib_calib(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Calibration")
                upset = up_upset.find("Calib")

                cali_cali_subs = upset.find("cal_subset")
                sett["cali_cali_subs"] = cali_cali_subs.text.strip()

                cali_cali_ccty = upset.find("cal_ccdtype")
                sett["cali_cali_ccty"] = cali_cali_ccty.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_phot_fitskypar(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Photometry")
                upset = up_upset.find("FitSkyPar")

                phot_fsp_annu = upset.find("Annulus")
                sett["phot_fsp_annu"] = phot_fsp_annu.text.strip()

                phot_fsp_dann = upset.find("Dannulus")
                sett["phot_fsp_dann"] = phot_fsp_dann.text.strip()

                phot_fsp_cbox = upset.find("cbox")
                sett["phot_fsp_cbox"] = phot_fsp_cbox.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_phot_datapar(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Photometry")
                upset = up_upset.find("Datapar")

                phot_dap_expo = upset.find("Exposure")
                sett["phot_dap_expo"] = phot_dap_expo.text.strip()

                phot_dap_fltr = upset.find("Filter")
                sett["phot_dap_fltr"] = phot_dap_fltr.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_phot_photpar(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Photometry")
                upset = up_upset.find("PhotoPar")

                phot_php_aper = upset.find("Aperture")
                sett["phot_php_aper"] = phot_php_aper.text.strip()

                phot_php_zmag = upset.find("ZMag")
                sett["phot_php_zmag"] = phot_php_zmag.text.strip()

                phot_php_gain = upset.find("Gain")
                sett["phot_php_gain"] = phot_php_gain.text.strip()

                phot_php_fxpx = upset.find("FixPix")
                sett["phot_php_fxpx"] = phot_php_fxpx.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_phot_wcs(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Photometry")
                upset = up_upset.find("WCS")

                phot_pwcs_rias = upset.find("RightAscension")
                sett["phot_pwcs_rias"] = phot_pwcs_rias.text.strip()

                phot_pwcs_decl = upset.find("Declination")
                sett["phot_pwcs_decl"] = phot_pwcs_decl.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_phot_locTime(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Photometry")
                upset = up_upset.find("LocationAndTime")

                phot_loti_obsv = upset.find("Observatory")
                sett["phot_loti_obsv"] = phot_loti_obsv.text.strip()

                phot_loti_tmsp = upset.find("Timestamp")
                sett["phot_loti_tmsp"] = phot_loti_tmsp.text.strip()

                phot_loti_tmob = upset.find("TimeOBS")
                sett["phot_loti_tmob"] = phot_loti_tmob.text.strip()

                phot_loti_dtob = upset.find("DateOBS")
                sett["phot_loti_dtob"] = phot_loti_dtob.text.strip()

                phot_loti_epca = upset.find("EpochCalculator")
                sett["phot_loti_epca"] = phot_loti_epca.text.strip()

                phot_loti_epoc = upset.find("Epoch")
                sett["phot_loti_epoc"] = phot_loti_epoc.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_phot_starfind(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Photometry")
                upset = up_upset.find("StarFind")

                phot_stfi_flra = upset.find("FluxRadius")
                sett["phot_stfi_flra"] = phot_stfi_flra.text.strip()

                phot_stfi_mifh = upset.find("MinFWHM")
                sett["phot_stfi_mifh"] = phot_stfi_mifh.text.strip()

                phot_stfi_mafh = upset.find("MaxFWHM")
                sett["phot_stfi_mafh"] = phot_stfi_mafh.text.strip()

                phot_stfi_mstf = upset.find("MaxStarsToFind")
                sett["phot_stfi_mstf"] = phot_stfi_mstf.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_phot_hextract(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                up_upset = root.find("Photometry")
                upset = up_upset.find("HeaderExtractor")

                phot_heex_extr = upset.find("exract")
                sett["phot_heex_extr"] = phot_heex_extr.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_ccleaner(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                upset = root.find("CosmicCleaner")

                coce_acmf = upset.find("AutoCreateMaskFile")
                sett["coce_acmf"] = coce_acmf.text.strip()

                coce_gain = upset.find("Gain")
                sett["coce_gain"] = coce_gain.text.strip()

                coce_reno = upset.find("ReadNoise")
                sett["coce_reno"] = coce_reno.text.strip()

                coce_sicl = upset.find("SigmaClip")
                sett["coce_sicl"] = coce_sicl.text.strip()

                coce_sifr = upset.find("SigmaFrac")
                sett["coce_sifr"] = coce_sifr.text.strip()

                coce_obli = upset.find("ObjectLimit")
                sett["coce_obli"] = coce_obli.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_wcs(self, file_name):
        ret = [False, None]
        sett = {}
        if self.mefop.is_file:
            try:
                tree = ElementTree.parse(file_name)
                root = tree.getroot()
                upset = root.find("WCS")

                wcs_serv = upset.find("Server")
                sett["wcs_serv"] = wcs_serv.text.strip()

                wcs_apke = upset.find("ApliKey")
                sett["wcs_apke"] = wcs_apke.text.strip()

                coce_belo = upset.find("BeforeLoad")
                sett["wcs_belo"] = coce_belo.text.strip()

                coce_abap = upset.find("AlignBeforeApplication")
                sett["wcs_abap"] = coce_abap.text.strip()

                coce_cwhs = upset.find("CreateWCSHeadersSeparately")
                sett["wcs_cwhs"] = coce_cwhs.text.strip()

                ret = [True, sett]
            except Exception as e:
                self.meetc.print_if(e)

        return ret

    def read_settings_calibration(self, file_name):
        ret = [False, None]
        ret_lst = {}
        try:
            bias = self.read_settings_calib_zerocombine(file_name)
            if bias[0]:
                for i in bias[1]:
                    ret_lst[i] = bias[1][i]

            dark = self.read_settings_calib_darkcombine(file_name)
            if dark[0]:
                for i in dark[1]:
                    ret_lst[i] = dark[1][i]

            flat = self.read_settings_calib_flatcombine(file_name)
            if flat[0]:
                for i in flat[1]:
                    ret_lst[i] = flat[1][i]

            cali = self.read_settings_calib_calib(file_name)
            if cali[0]:
                for i in cali[1]:
                    ret_lst[i] = cali[1][i]

            ret = [True, ret_lst]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def read_settings_photometry(self, file_name):
        ret = [False, None]
        ret_lst = {}
        try:
            datapar = self.read_settings_phot_datapar(file_name)
            if datapar[0]:
                for i in datapar[1]:
                    ret_lst[i] = datapar[1][i]

            fitskypar = self.read_settings_phot_fitskypar(file_name)
            if fitskypar[0]:
                for i in fitskypar[1]:
                    ret_lst[i] = fitskypar[1][i]

            hextractor = self.read_settings_phot_hextract(file_name)
            if hextractor[0]:
                for i in hextractor[1]:
                    ret_lst[i] = hextractor[1][i]

            locTime = self.read_settings_phot_locTime(file_name)
            if locTime[0]:
                for i in locTime[1]:
                    ret_lst[i] = locTime[1][i]

            photpar = self.read_settings_phot_photpar(file_name)
            if photpar[0]:
                for i in photpar[1]:
                    ret_lst[i] = photpar[1][i]

            starfind = self.read_settings_phot_starfind(file_name)
            if starfind[0]:
                for i in starfind[1]:
                    ret_lst[i] = starfind[1][i]

            wcs = self.read_settings_phot_wcs(file_name)
            if wcs[0]:
                for i in wcs[1]:
                    ret_lst[i] = wcs[1][i]

            ret = [True, ret_lst]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def read_settings_best_cpu(self):
        ret = [False, None]
        try:
            cores = multiprocessing.cpu_count()
            ret = [True, int(cores / 2)]
        except Exception as e:
            self.meetc.print_if(e)

        return ret

    def convert_blank_setting(self, setting):
        if setting == "":
            ret = " "
        else:
            ret = setting

        return ret