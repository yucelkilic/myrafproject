## MYRaf Bağımsız Kurulum ##

> 0. Eğer MYRaf için bütün gereksinimlere sahipseniz kuruluma başlayabilirnisiz.(Değise, [bu](https://code.google.com/p/myrafproject/) linke bakınız.)

  1. [Downloads](https://code.google.com/p/myrafproject/downloads/) sayfasından Standalone dosyasını indiriniz.

```
$ cd Downloads
```

```
$ tar -xvf myraf-1.5-beta-sa.tar.gz
```

```
$ cp -r MYRaf ~/
```

> 2.  /usr/bin/ dizininde "**myraf**" adında bir dosya oluşturup içine aşağıdaki satırları yazınız.

```
#!/bin/bash
cd "$HOME"/MYRaf
python main.py
```

> 3. myraf dosyasına çalıştırma haklarını veriniz.

```
$ chmod +x /usr/bin/myraf
```

> 4. Aşağıdaki komutla MYRaf için bir .desktop dosyası oluşturabilirsiniz.

```
$ nano /usr/share/applications/myraf.desktop
```

> 5. myraf.desktop dosyasına aşağıdaki satırları kopyalayınız.
```
[Desktop Entry]
Encoding=UTF-8
Version=1.5
Terminal=false
Type=Application
Categories=Astronomy;Education;Science;MYRaf
Exec=myraf
Name=MYRaf
Comment=An Easy GUI for IRAF Photometry
Icon=/home/USERNAME/MYRaf/img/MYRaf.png
```

```
$ exit
```

```
$ cd ~/MYRaf
```

```
$ mkiraf
-- uparm dizinini oluşturmak
Terminal types: xgterm,xterm,gterm,vt640,vt100,etc.
Enter terminal type: 
```

> 6. Terminal tipini "**xgterm**" olarak giriniz.

```
$ pyraf
```

```
> .exit
```

```
$ exit
```

MYRaf kısayolunu Education/Science/Astronomy Menüsünde bulabilirsiniz.

Tebrikler! Artık GNU/Linux'unuzda MYRaf var! :)