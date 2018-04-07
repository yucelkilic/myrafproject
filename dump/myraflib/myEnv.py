# -*- coding: utf-8 -*-

import os
import getpass
import inspect
import platform
from datetime import datetime
import glob
from astropy.time import Time
from shutil import copy as cifir


class etc():

    def __init__(self, verb=True):
        self.verb = verb
        self.log_file = "%s/log.my" % (os.path.expanduser("~"))
        self.mini_log_file = "%s/mlog.my" % (os.path.expanduser("~"))

    def time_stamp(self):
        return str(datetime.utcnow().strftime("%Y-%m-%IT%H:%M:%S"))

    def user_name(self):
        return str(getpass.getuser())

    def system_info(self):
        si = platform.uname()
        return(("%s, %s, %s, %s"
        % (si[0], si[2], si[5], self.user_name())))

    def caller_function(self, pri=True):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        caller = calframe
        self.system_info()
        if pri:
            return "%s>%s>%s" % (caller[0][3], caller[1][3], caller[2][3])
        else:
            return caller

    def print_if(self, text):
        self.log_if(text)
        self.mini_log_if(text)
        if self.verb:
            print(("[%s|%s|%s]%s" % (self.time_stamp(), self.caller_function(),
                 self.system_info(), text)))

    def log_if(self, text):
        log_file = open(self.log_file, "a")
        log_file.write("Time: %s\n" % self.time_stamp())
        log_file.write("System Info: %s\n" % self.system_info())
        log_file.write("Log: %s\n" % text)
        log_file.write("Function: %s\n\n\n" % (self.caller_function(pri=False)))
        log_file.close()

    def mini_log_if(self, text):
        mini_log_file = open(self.mini_log_file, "a")
        mini_log_file.write("[%s|%s|%s]%s\n" % (
            self.time_stamp(), self.caller_function(),
            self.system_info(), text))
        mini_log_file.close()

    def get_mini_log_file(self):
        ret = [False, None]
        res = []
        try:
            mini_log_file = open(self.mini_log_file, "r")
            for i in mini_log_file:
                res.append(i.replace("\n", "").strip())
            mini_log_file.close()
            ret = [True, res]
        except Exception as e:
            self.print_if(e)

        return ret

    def join_list_items_to_string(self, lst):
        ret = [False, None]
        try:
            string_value = ""
            for i in lst:
                string_value = "%s,%s" % (string_value, i)
            ret = [True, string_value[1:]]
        except Exception as e:
            self.print_if(e)

        return ret


class file_operation():

    def __init__(self, verb=True):
        self.verb = verb
        self.fetc = etc(verb=verb)
        self.file_suffixes = ['bytes', 'KiB', 'MiB', 'GiB',
            'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

    def get_file_size(self, file_name):
        ret = [False, None]
        try:
            st = os.stat(file_name)
            ret = [True, [file_name, st.st_size]]
        except Exception as e:
            self.print_if(e)

        return ret

    def get_human_readable_file_size(self, num, suffix='B'):
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)

    def delete_log_files(self):
        f = open(self.fetc.log_file, "w")
        f.close()
        f = open(self.fetc.mini_log_file, "w")
        f.close()

    def get_total_log_file_size(self):
        ret = [False, None]
        try:
            lsize = 0
            mlsize = 0
            lf_size = self.get_file_size(self.fetc.log_file)
            mlf_size = self.get_file_size(self.fetc.mini_log_file)
            if lf_size[0]:
                lsize = lf_size[1][1]

            if mlf_size[0]:
                mlsize = mlf_size[1][1]

            total_size = lsize + mlsize

            ret = [True, self.get_human_readable_file_size(total_size)]
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def is_file(self, file_name):
        ret = False
        if os.path.isfile(str(file_name)):
            self.fetc.print_if("File(%s) DOES exist" % (file_name))
            ret = True
        else:
            self.fetc.print_if("File(%s) DOES NOT exist" % (file_name))

        return ret

    def is_dir(self, dir_name):
        ret = False
        if os.path.isdir(str(dir_name)):
            self.fetc.print_if("Directory(%s) DOES exist" % (dir_name))
            ret = True
        else:
            self.fetc.print_if("Directory(%s) DOES NOT exist" % (dir_name))

        return ret

    def write_file(self, file_to_write, text, op_type):
        ret = False
        try:
            fl = open(file_to_write, op_type)
            fl.write(text)
            fl.close()
            ret = True
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def write_to_file(self, file_to_write, text, op_type, force=False):
        ret = False
        if not self.is_file(file_to_write):
            ret = self.write_file(file_to_write, text, op_type)
        else:
            if force:
                ret = self.write_file(file_to_write, text, op_type)
            else:
                self.fetc.print_if("File(%s) already exist. Wont overwrite.")

        return ret

    def get_myraf_dir(self):
        ret = [False, None]
        hm = self.get_home_dir()
        if hm[0]:
            ret = [True, "%s/MYRaf" % (hm[1])]

        return ret

    def get_tmp_dir(self):
        ret = [False, None]
        hm = self.get_home_dir()
        if hm[0]:
            ret = [True, "%s/MYRaf/tmp" % (hm[1])]

        return ret

    def get_analyzed_dir(self):
        ret = [False, None]
        hm = self.get_home_dir()
        if hm[0]:
            ret = [True, "%s/MYRaf/tmp/analyzed" % (hm[1])]

        return ret

    def get_atrack_dir(self):
        ret = [False, None]
        hm = self.get_home_dir()
        if hm[0]:
            ret = [True, "%s/MYRaf/tmp/atrack" % (hm[1])]

        return ret

    def get_home_dir(self):
        ret = [False, None]
        try:
            home = os.path.expanduser("~")
            ret = [True, home]
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def get_file_name_list(self, home, expr):
        ret = [False, None]
        files = []
        try:
            for i in glob.glob("%s/%s" % (home, expr)):
                files.append(os.path.basename(i).split(".")[0])
            ret = [True, files]
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def get_base_name(self, file_path):
        ret = [False, None]
        try:
            pn = os.path.dirname(os.path.realpath(file_path))
            fn = os.path.basename(os.path.realpath(file_path))
            ret = [True, [pn, fn]]
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def get_extension(self, in_file):
        ret = [False, None]
        try:
            file_extension = os.path.splitext(in_file)[1]
            ret = [True, file_extension]
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def create_obs_file(self, observat, name, longitude, latitude, altitude,
        timezone, comm=""):
        ret = False
        try:
            obs_file = "./observatories/%s" % (observat.lower())
            if self.is_file(obs_file):
                self.fetc.print_if("%s:File already exist. Going for an update")
            obs = open(obs_file, "w")
            if not comm == "":
                obs.write("#%s\n" % (comm.replace(
                    "\n", "\n#").encode('utf8', 'replace')))
            obs.write("observatory = \"%s\"\n" % (observat))
            obs.write("\tname = \"%s\"\n" % (name))
            obs.write("\tlongitude = %s\n" % (longitude))
            obs.write("\tlatitude = %s\n" % (latitude))
            obs.write("\taltitude = %s\n" % (altitude))
            obs.write("\ttimezone = %s\n" % (timezone))
            obs.close()

            ret = True
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def get_values_from_obs_file(self, observat):
        obs_file = "./observatories/%s" % (observat.lower())
        ret = [False, None]
        values = {}
        comm = ""
        try:
            obs = open(obs_file, "r")
            for i in obs:
                if not i.startswith("#"):
                    if i.strip().startswith("observatory"):
                        values["observatory"] = i.strip().split(
                            "=")[1].strip().replace("\"", "")
                    elif i.strip().startswith("name"):
                        values["name"] = i.strip().split(
                            "=")[1].strip().replace("\"", "")
                    elif i.strip().startswith("longitude"):
                        values["longitude"] = i.strip().split(
                            "=")[1].strip().replace("\"", "")
                    elif i.strip().startswith("latitude"):
                        values["latitude"] = i.strip().split(
                            "=")[1].strip().replace("\"", "")
                    elif i.strip().startswith("altitude"):
                        values["altitude"] = i.strip().split(
                            "=")[1].strip().replace("\"", "")
                    elif i.strip().startswith("timezone"):
                        values["timezone"] = i.strip().split(
                            "=")[1].strip().replace("\"", "")
                else:
                    comm = "%s\n%s" % (comm, i.strip())

            obs.close()

            values["commands"] = comm.strip().replace("#", "")
            ret = [True, values]
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def cp_file(self, in_file, dest):
        ret = False
        try:
            cifir(in_file, dest)
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def delete_file(self, file_name):
        ret = False
        try:
            os.remove(file_name)
            ret = True
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def rename_file(self, source_name, destination_name):
        ret = False
        try:
            os.rename(source_name, destination_name)
            ret = True
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def join_text_files(self, in_files, out_file):
        if type(in_files) == list:
            with open(out_file, 'w') as outfile:
                for fname in in_files:
                    with open(fname) as infile:
                        outfile.write(infile.read())

    def save_1d_array_to_file(self, out_file, array):
        ret = False
        try:
            if self.is_file(out_file):
                self.fetc.print_if("%s:Going to overwrite it." % (out_file))

            file_to_save = open(out_file, "w")
            for i in array:
                file_to_save.write("%s\n" % (i))
            file_to_save.close()
            ret = True

        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def write_list_to_file(self, list_to_write, file_name):
        ret = False
        try:
            outfile = open(file_name, "w")
            outfile.write("\n".join(list_to_write))
            outfile.write("\n")
            outfile.close()
            ret = True
        except Exception as e:
            self.fetc.print_if(e)

        return ret


class time_operation():

    def __init__(self, verb=True):
        self.verb = verb

    def get_jd(self, utc_timestamp):
        ret = [False, None]
        try:
            tm = Time(utc_timestamp, format='isot', scale='utc')
            tm_jd = tm.jd
            ret = [True, tm_jd]
        except Exception as e:
            self.fetc.print_if(e)

        return ret

    def get_mjd(self, utc_timestamp):
        ret = [False, None]
        try:
            tm = Time(utc_timestamp, format='isot', scale='utc')
            tm_mjd = tm.mjd
            ret = [True, tm_mjd]
        except Exception as e:
            self.fetc.print_if(e)

        return ret
