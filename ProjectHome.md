# myraflib project started #

For further information: [myraflib](myraflib.md)

# MYRaf 2.0 Beta released! #

The MYRaf is a practicable astronomical image reduction and photometry software and interface for IRAF. For this purpose, MYRaf uses iraf, PyRAF and alipy via great programming language Python and Qt framework. Also MYRaf is a absolutely free software and distributed with GPLv3 license. You can use it without restrictive licenses, make copies for your friends, school or business.

We tried MYRaf's all beta versions on;

  * [Ubuntu](http://www.ubuntu.com/) >= 12.04
  * [Distro Astro](http://www.distroastro.org/) 2.0
  * [Fedora](http://fedoraproject.org/) >= 18
  * [Debian](https://www.debian.org/index.tr.html) >= 6.0
  * [Pardus](http://www.pardus.org.tr/) 2013 RC2

GNU/Linux distributions. Have fun with MYRaf! :)

# MYRaf 2.0 Beta #

### For all GNU/Linux distributions, MYRaf requires the following packages. ###

  * [python-pip](https://pypi.python.org/pypi/pip) and [subversion](http://subversion.apache.org/)
    * sudo yum/apt-get install python-pip subversion

  * [pyqt4-dev-tools](http://www.riverbankcomputing.com/software/pyqt/download)
    * sudo apt-get install pyqt4-dev-tools (Ubuntu)
    * sudo yum install pyqt4-devel (Fedora)

  * [IRAF v2.14 and later](http://iraf.noao.edu/)
    * If you are using Ubuntu its's easy to install from this [link](http://www.astrosen.unam.mx/~favilac/IRAF/).

  * [matplotlib](http://matplotlib.org/) and [SciPy](http://www.scipy.org/install.html)
    * sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose kde-style-oxygen (Ubuntu)
    * sudo yum install python-matplotlib python-matplotlib-qt4 numpy scipy ipython python-pandas sympy python-nose gcc python-devel libX11-devel (Fedora)

  * [PyRAF 2.0 and later](http://www.stsci.edu/institute/software_hardware/pyraf)
    * sudo pip install pyraf

  * [astropy](http://www.astropy.org/)
    * sudo pip install astropy

  * [Ginga](http://ginga.readthedocs.org/en/latest/)
    * sudo pip install ginga
    * To use Ginga on MYRaf 2.0 Beta please check [this tutorial](http://ginga.readthedocs.org/en/latest/quickref.html).

  * [Alipy 2.0](http://obswww.unige.ch/~tewes/alipy/) : For installation instructions of alipy visit Malte Tewes’s alipy project website. Alipy also requires [Sextractor (=>2.8.6)](http://www.astromatic.net/software/sextractor) and [AstroAsciiData](http://www.stecf.org/software/PYTHONtools/astroasciidata/).
    * You can find a debian package for Sextractor in [Downloads](DownloadList.md) section.

Note: For multiple file selection and filtering problem please see [issue 11](https://code.google.com/p/myrafproject/issues/detail?id=11).

### Installation (2.0 Beta) ###

  * Get MYRaf directly from its public repository, by typing:

```
$ svn checkout http://myrafproject.googlecode.com/svn/trunk/ myrafproject

$ cd myrafproject

$ sudo python setup.py install
```

To run MYRaf 2.0 Beta,

```
$ myraf2
```

maybe or clicking,

Applications > Education > Science > MYRaf v2.0 Beta.


# MYRaf 1.5 #

### For all GNU/Linux distributions, MYRaf requires the following packages. ###

  * [IRAF v2.14](http://iraf.noao.edu/)

  * [PyRAF 2.0](http://www.stsci.edu/institute/software_hardware/pyraf)

  * [pyqt4-dev-tools](http://www.riverbankcomputing.com/software/pyqt/download)

  * [ImageMagic >6.0](http://www.imagemagick.org/script/index.php)

  * [Alipy 2.0](http://obswww.unige.ch/~tewes/alipy/) : For installation instructions of alipy visit Malte Tewes’s alipy project website. Alipy also requires [Sextractor](http://www.astromatic.net/software/sextractor), [AstroAsciiData](http://www.stecf.org/software/PYTHONtools/astroasciidata/).


### Installation (1.5 Beta) ###

  * [Ubuntu](Ubuntu.md) ([tr](UbuntuTurkish.md))
  * [Fedora](Fedora.md) ([tr](FedoraTurkish.md))
  * [Standalone](Standalone.md) ([tr](StandaloneTurkish.md))