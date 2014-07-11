About
=====

The MYRaf is a practicable astronomical image reduction and photometry software and interface for IRAF. For this purpose, MYRaf uses iraf, PyRAF and alipy via great programming language Python and Qt framework. Also MYRaf is a absolutely free software and distributed with GPLv3 license. You can use it without restrictive licenses, make copies for your friends, school or business. 

http://myrafproject.org
Develeopers: Yücel KILIÇ 				      <yucelkilic@myrafproject.org>
             Mohammad Shameoni NIAEI	<m.shemuni@myrafproject.org> 

MYRaf 2.0 Beta
==============

For all GNU/Linux distributions, MYRaf requires the following packages.
    $ python-pip and subversion
    $ sudo yum/apt-get install python-pip subversion
    
1- IRAF v2.14 and later
  If you are using Ubuntu its's easy to install from this link (http://www.astrosen.unam.mx/~favilac/IRAF/).

2- PyRAF 2.0 and later
    $ sudo pip install pyraf

3- pyqt4-dev-tools
    $ sudo apt-get install pyqt4-dev-tools (Ubuntu)
    $ sudo yum install pyqt4-devel (Fedora)

4- astropy
    $ sudo pip install astropy
    
5- matplotlib
    $ sudo apt-get install matplotlib matplotlib-data (Ubuntu)
    $ sudo yum install python-matplotlib python-matplotlib-qt4 (Fedora)
    
6- Ginga
    $ sudo pip install ginga
    
7- Alipy 2.0 : For installation instructions of alipy visit Malte Tewes’s alipy project website. Alipy also requires Sextractor (=>2.8.6) and AstroAsciiData.
You can find a debian package for Sextractor in Downloads section.

Installation
============
Get MYRaf directly from its public repository, by typing:

$ svn checkout http://myrafproject.googlecode.com/svn/trunk/ myrafproject

$ cd myrafproject

$ sudo python setup.py install

To run MYRaf 2.0 Beta,

$ myraf2

maybe or clicking,

Applications > Education > Science > MYRaf v2.0 Beta.

Have fun with MYRaf! :)
