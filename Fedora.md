# HOW TO INSTALL MYRaf on FEDORA 18 #

## IRAF Installation ##

  1. IRAF v2.14. You can use also [this](http://gabriel-ip.blogspot.com/2010/06/install-iraf-on-fedora-running-under.html) guide for installing IRAF v2.14 on Fedora 8 and greater.

> 2. Download the IRAF installation script from [here](http://skytux.fedorapeople.org/scripts/install_iraf_script.sh).

> 3. Give the commands listed below respectively.
```
 $ cd Downloads (If the file downloaded here)
```
```
 $ chmod +x install_iraf_script.sh
```
```
 $ su -c "./install_iraf_script.sh -i iraf"
```

> 4. When the script is done, IRAF should be installed with no errors. You should see the prompt line.
```
 $ su -c "./install_iraf_script.sh -i x11iraf"
```

> 5. This script creates a new account in FEDORA called "**IRAF system login**". This account has no password, so to be able to login you'll have to assign one to it. To do this, go to **System/Administration/Users** and Groups, double click on the user "iraf", go to the tab "**Account Information**" and disable "The local password is blocked." Then return to the tab "**User Data**" and write your password (in "**Password**" and in "Confirm password") in '**Login Shell**', you should select '**/bin/csh**' or '**/bin/tcsh**' (I selected '**csh**').

> 6. Or become root and set password for "**iraf**" user which is created by installation script;
```
 $ su
```
```
 $ passwd iraf
```
> 7. And continue from step **4** and **4a** on this [link](http://gabriel-ip.blogspot.com/2010/06/install-iraf-on-fedora-running-under.html).

> 8. Download DS9 from [here](http://hea-www.harvard.edu/RD/ds9/site/Download.html).

> 9. And install it;
```
$ tar -xvf ds9.linux.7.1.tar.gz
```
```
$ mv ds9 /usr/bin
```
```
exit
```

## PyRAF Installation ##
  1. Install required packages for PyRAF on Fedora;
```
$ su
```
```
$ yum install tcl tcl-devel readline readline-devel numpy numpy-f2py python-pmw python-urwid python-ipython python-matplotlib python-matplotlib-qt4 gcc gcc-gfortran libX11-devel pyqt4-devel ImageMagick cfitsio cfitsio-devel cfitsio-static pyfits scipy 
```
```
$ su iraf
```
> 2.a. Download the numpy [here](http://sourceforge.net/projects/numpy/files/latest/download?source=files) and copy iraf user's home folder. Change directory to where numpy has copied.
```
% su -c "tar -xvf numpy-[version].tar.gz"
```
```
% cd numpy-[version]
```
```
% unsetenv F77
```
```
% unsetenv F2C
```
```
% su -c "python setup.py install"
```
```
% cd ..
```

Note: You can install numpy and other python depencies via this command:

```
% sudo yum install numpy scipy python-matplotlib ipython python-pandas sympy python-nose
```

Users of Fedora 17 and earlier should then upgrade IPython using pip:
```
% sudo pip install --upgrade ipython
```

2.b. Download stsci [here](http://www.stsci.edu/institute/software_hardware/pyraf/stsci_python/current/stsci-python-download) and change directory where stsci has downloaded.
```
% tar -zxvf  stsci_python-[version].tar.gz
```

```
% cd stsci_python-[version]
```
```
% su -c "python setup.py install"
```
```
% exit
```
3. Download PyRAF [here](http://stsdas.stsci.edu/download/pyraf/pyraf-dev.tar.gz) and change directory to where it downloaded.

```
$ tar -xvf pyraf-dev.tar.gz
```
```
$ cd pyraf-dev
```
```
$ python setup.py install
```
```
$ exit
```

4. Check PyRAF! :)
```
$ pyraf
```
> 4. You will see PyRAF's prompt line!
```
> .exit
```
```
$ exit
```

Now, you can install MYRaf! Click to [Standalone](Standalone.md) link for installing MYRaf. :)