# Fedora 18, MYRaf kurulumu. #

## IRAF kurulumu ##

  1. Fedora 8 ve üst sürümlerine IRAF v2.14 kurulumu yapmak için [bu](http://gabriel-ip.blogspot.com/2010/06/install-iraf-on-fedora-running-under.html) linke bakabilirsiniz.

> 2. IRAF kurulum betiğini [buradan](http://skytux.fedorapeople.org/scripts/install_iraf_script.sh) indirebilirsiniz.

> 3. Sırasıyla açağıdaki adamları takipediniz.
```
 $ cd Downloads (betik buraya indirildiyse.)
```
```
 $ chmod +x install_iraf_script.sh
```
```
 $ su -c "./install_iraf_script.sh -i iraf"
```

> 4. Kurulum tamamlandığında IRAF kurulmuş olmalı ve aşağıdaki komtla devam ediniz.
```
 $ su -c "./install_iraf_script.sh -i x11iraf"
```

> 5. Bu betik sistemde "**IRAF system login**" adlı bir kullanıcı oluşturuyor. Söz konusu kullanıcının şifresi olmadığından arayüz'den erişim mümkün değildir. Şifre oluşturmak için, **System/Administration** menüsünden **Users and Groups**'ı tıklayınız. Açılan pencerede "iraf"a çift tıklayınız ve "**Account Information**" sekmesini açınıp "The local password is blocked." seçeneğini etkinsizleştiriniz. Daha sonra "**User Data**" sekmesine dönünüz ve kullanıcı şifrenizi yazınız ("**Password**" ve "Confirm password" alanlarını doldurduğunuzdan emin olunuz.). '**Login Shell**' seçeneği ise '**/bin/csh**' veya '**/bin/tcsh**' olmalıdır (Ben '**csh**' seçtim).

> 6. Yada root kullanıcısı olup aşağıdaki yöntemle iraf kullanıcısına yeni şifre oluşturunuz.
```
 $ su
```
```
 $ passwd iraf
```
```
 $ exit
```
> 7. Daha sonra bu [adres](http://gabriel-ip.blogspot.com/2010/06/install-iraf-on-fedora-running-under.html)'teki **4** ve **4a** adımlarından devam ediniz.

> 8. DS9'u [buradan](http://hea-www.harvard.edu/RD/ds9/site/Download.html) indiriniz.

> 9. Daha sonra kurunuz;
```
$ tar -xvf ds9.linux.7.1.tar.gz
```
```
$ mv ds9 /usr/bin
```
```
exit
```

## PyRAF Kurulumu ##
  1. Öncelikle gereksinileri kurunuz;
```
$ su
```
```
$ yum install tcl tcl-devel readline readline-devel numpy numpy-f2py python-pmw python-urwid python-ipython python-matplotlib python-matplotlib-qt4 gcc gcc-gfortran libX11-devel pyqt4-devel ImageMagick cfitsio cfitsio-devel cfitsio-static pyfits scipy 
```
```
$ su iraf
```
> 2. [buradan](http://sourceforge.net/projects/numpy/files/latest/download?source=files) numpy'yi indirip iraf kullanıcısı ev dizinine kopyalayınız. numpy'nin kopyalandığı dizine geçiş yapınız.

```
% su -c "tar -xvf numpy.tar.gz"
```
```
% cd numpy
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
```
% cd stsci_python
```
```
% su -c "python setup.py install"
```
```
% exit
```
```
$ cd ~Downloads/
```
```
$ tar -xvf pyraf-dev.tar.gz
```
```
$ cd pyraf-devel
```
```
$ python setup.py install
```
```
$ exit
```

> 3. PyRAF'ı denetleyiniz! :)
```
$ pyraf
```
> 4. PyRAF terminal'ini görmüş olmalısınız!
```
> .exit
```
```
$ exit
```

Şimdi MYRaf'ı kurabilirsiniz! [Bu](StandaloneTurkish.md) linke bakınız. :)