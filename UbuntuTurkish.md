# Ubuntu (tr) #

  * **IRAF** : Ubuntu'ya iraf kolay kurulumu için [bu](http://yadi.sk/d/Zt_EICu00J_lZ) link'teki iso dosyasını kullanabilirsiniz. Bu iso dosyasında PyRAF ve birçok astronomi aracı bulunmaktadır. (Örneğin: ds9, PyFITS, GEMINI vs.)


  * **PyRAF**

  * **pyqt4-dev-tools**

  * **Image Magic**

  * **Alipy** : Kurulum talimatları için Malte TEWES'in alipy proje'si web sayfasını ziyaret ediniz.

Eğer yukarıdaki gereksinimlere sahip değilseniz, MYRaf'ın Ubuntu ve Ubuntu tabanlı sistemlere (Tavsiye edilen sistem Kubuntu) kurulumu için aşağıdaki talimatları takip ediniz.

  1. [myraf-1.5-beta.tar.gz](http://code.google.com/p/myrafproject/wiki/DownloadList) dosyasını indiriniz.

> 2- Arşiv dosyasını aşağıdaki komutu kullanarak açınız:

```
$ tar -xvf myraf-1.5-beta.tar.gz
```

> 3- myraf-1.5-beta dizinine geçiş yapıp install\_myraf.sh dosyasına çalıştırma hakkı veriniz.

```
$ cd myraf-1.5-beta
```
```
$ chmod +x install_myraf.sh
```

> 4- sudo komutuyla dosyayı çalıştırınız.

```
$ sudo ./install_myraf.sh
```

> 5- IRAF ve PyRAF için yapılandırma dosyalarını oluşturunuz.

```
$ cd $HOME"/MYRaf"
```
```
$ mkiraf
```

> 6- Terminal tipini seçiniz: Önerilen **xgterm**.


```
$ pyraf
```
```
> .exit
```
```
$ exit
```

İşte bu kadar!
MYRaf kısayolunu Education/Science/Astronomy menüsünde bulabilirsiniz.