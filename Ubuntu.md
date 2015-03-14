# How to Install MYRaf v1.5 Beta on Ubuntu 12.04.04 and Later #

  * **IRAF** : You can install IRAF on Ubuntu easily from [this](http://yadi.sk/d/Zt_EICu00J_lZ) ISO file. The ISO file contains also PyRAF and many astronomical tools (ds9, PyFITS, GEMINI etc.).

Note: You can download latest version of this iso file from [here](http://www.astrosen.unam.mx/~favilac/IRAF/).

  * **PyRAF**

  * **pyqt4-dev-tools**

  * **Image Magic**

  * **Alipy** : For installation instructions of alipy visit Malte Tewes’s alipy project website.

If you do not have these requirements above. You can install MYRaf on Ubuntu and Ubuntu based systems (Kubuntu is highly recommended) with these steps.

  1. Download myraf-1.5-beta.tar.gz from [here](http://code.google.com/p/myrafproject/wiki/DownloadList).

> 2- Extract the file with this command:

```
$ tar -xvf myraf-1.5-beta.tar.gz
```

> 3- Enter the myraf-1.5-beta directory and give execute permission the install\_myraf.sh file.

```
$ cd myraf-1.5-beta
```
```
$ chmod +x install_myraf.sh
```

> 4- And run it with sudo command.

```
$ sudo ./install_myraf.sh
```

> 5- Create your IRAF and PyRAF configurations.

```
$ cd $HOME"/MYRaf"
```
```
$ mkiraf
```

> 6- Select your terminal type: Recommended **xgterm**.


```
$ pyraf
```
```
> .exit
```
```
$ exit
```

That’s all!
You will find the MYRaf’s icon under Education/Science/Astronomy Menu.