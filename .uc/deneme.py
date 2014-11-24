import myLib

mc = myLib.myCal

c = mc.cOP()

#mf = myLib.myFit
#s = mf.sOP()
#s.deneme("d/1.fit")
#s.imcom(["d/1.fit", "d/2.fit", "d/3.fit", "d/4.fit", "d/5.fit", "d/6.fit", "d/7.fit", "d/8.fit", "d/9.fit", "d/10.fit"], "average", "mi", "a.fit", verb=True)

c.zerocombine(["d/1.fit", "d/2.fit", "d/3.fit", "d/4.fit", "d/5.fit", "d/6.fit", "d/7.fit", "d/8.fit", "d/9.fit", "d/10.fit"], "zero.fit", "MEdian", "None", ccdType=["typ", "zero"], skp=True, verb=True)
