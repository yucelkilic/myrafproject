# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
MYRaf's Libraries.
Note that all modules with name started by 'my' such as myFit, myEnv are MYRaf's third party modules.
Dependencies: pyfits
For further information:

	import myraflib
	help(myraflib)
"""
__authors__	=[["Mohammad SHAMEONI NIAEI", "m.shemuni@myrafproject.org"], ["Yucel KILIC", "ykilic@myrafproject.org"]]
__copyright__="Copyleft 2010, The MYRaf Project"
__credits__	=["Mohammad SHAMEONI NIAEI", "Yucel KILIC"]
__license__	="GPL V3"
__version__	="1.0"
__email__="info@myrafproject.org"
__date__="19.11.2014"
__package__=__name__


import myraflib.myEnv
import myraflib.myFit
import myraflib.myCal


__all__ = ["myFit", "myEnv", "myCal"]