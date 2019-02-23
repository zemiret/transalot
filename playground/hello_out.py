import os
from time import ctime

class TimePrinter:
    def _get_my_time(self):
        return ctime()

    def do_sth(self):
        try:
            t = self._get_my_time()
            if not 'Sat' in t: 
                raise RuntimeError('It ain\'t sat!')
            else:
                print('It is sat!')
        finally:
            print('Print me sth anyway')

timePrinter = TimePrinter()
timePrinter.do_sth()
