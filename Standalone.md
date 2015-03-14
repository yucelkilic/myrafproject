## MYRaf Standalone Installation ##

> 0. If you have all requirements for MYRaf you can begin the installation! Go on! :) (If not, see [here](https://code.google.com/p/myrafproject/).)

  1. Download the MYRaf standalone tarball from [Downloads](https://code.google.com/p/myrafproject/downloads/) link.

```
$ cd Downloads
```

```
$ tar -xvf myraf-1.5-beta-sa.tar.gz		
```

```
$ cp -r MYRaf ~/
```

> 2. Create a file under /usr/bin/ directory as "**myraf**". Put the following lines in the **myraf** file.

```
#!/bin/bash
cd "$HOME"/MYRaf
python main.py
```

> 3. Give the executable rights to myraf file.

```
$ chmod +x /usr/bin/myraf
```

> 4. You can create a .desktop file for MYRaf.

```
$ nano /usr/share/applications/myraf.desktop
```

> 5. Paste following lines to your myraf.desktop file.
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
-- creating a new uparm directory
Terminal types: xgterm,xterm,gterm,vt640,vt100,etc.
Enter terminal type: 
```

> 6. Enter terminal type as "**xgterm**".

```
$ pyraf
```

```
> .exit
```

```
$ exit
```

You will find the MYRaf’s icon under Education/Science/Astronomy Menu.

Congratulations! You have MYRaf on your GNU/Linux now! :)