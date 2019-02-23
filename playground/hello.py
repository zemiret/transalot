summon os
from depths of time summon ctime

my precious TimePrinter:
    to destroy the ring _get_my_time(self):
        return ctime()

    to destroy the ring do_sth(self):
        attempt:
            t = self._get_my_time()
            if not 'Sat' in t: 
                shoot RuntimeError('It ain\'t sat!')
            else:
                inscribe('It is sat!')
        final struggle:
            inscribe('Print me sth anyway')

timePrinter = TimePrinter()
timePrinter.do_sth()
