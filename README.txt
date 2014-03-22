About
=====

The MYRaf is a practicable astronomical image reduction and photometry software and interface for IRAF. For this purpose, MYRaf uses iraf, PyRAF and alipy via great programming language Python and Qt framework. Also MYRaf is a absolutely free software and distributed with GPLv3 license. You can use it without restrictive licenses, make copies for your friends, school or business. 

http://myrafproject.org
Develeopers: Yücel KILIÇ 				<yucelkilic@myrafproject.org>
			 Mohammad Shameoni NIAEI	<m.shemuni@myrafproject.org> 

Installation
============

How to Install MYRaf v2.0 Beta on Ubuntu (>12.04), Debian (>7.0), Linux Mint and Distro Astro (2.0)

    IRAF : You can install IRAF on Debian based systems easily from this ISO file. The excellent ISO file contains also PyRAF and many astronomical tools (ds9, PyFITS, GEMINI etc.). 

Note: You can download latest version of this iso file (depending on your architecture) from here.

    PyRAF 

    pyqt4-dev-tools 

    Astropy 

    Alipy : For installation instructions of alipy visit Malte Tewes’s alipy project website. 

    python-matplotlib 

If you DO NOT HAVE these requirements above. You can install MYRaf-v2-Beta with all requirements to Debian based systems with these steps.

Note: Don't panic! :) Distro Astro 2.0 already have many requirements above, so installation script will not install which requirements already installed.

    Download the "Installation tarball" myraf-2.0-beta-debian-based.tar.gz from here. 

    2- Extract the file with this command: 

$ tar -xvf myraf-2.0-beta-debian-based.tar.gz

    3- Enter the myraf-2.0-beta-debian-based directory and give execute permission rights to the install_myraf-v2.0.sh file. 

$ cd myraf-2.0-beta-debian-based

$ chmod +x install_myraf-v2.0.sh

    4- And run it with sudo command. 

$ sudo ./install_myraf-v2.0.sh

    5- Now, almost done! Answer the mkiraf command as: xgterm 

    6- Then, exit with exit, 

$ exit

That’s all! You will find the MYRaf2’s icon under Education/Science/Astronomy Menu. 
