import logging
from subprocess import check_output, CalledProcessError, Popen, PIPE
from lxml import etree

version = (0, 1, 1)
version_string = "PyFreeling version %d.%d.%d" % version
__copyright__ = 'Copyright (c) 2016 Marcos Vanetta'


binary = None

logger = logging.getLogger(__name__)


def find_binary():
    try:
        return check_output(['which', 'analyze']).split()[0]
    except (CalledProcessError, KeyError):
        return None


class Analyzer(object):
    def __init__(self, *args, **kwargs):
        self.config = kwargs.get('config', 'analyzer.cfg')
        self.lang = kwargs.get('lang', 'en')
        self.timeout = kwargs.get('timeout', 30)
        self.binary = find_binary()

    def run(self, input, *args, **kwargs):
        cmd = self._build_cmd(*args, **kwargs)
        logger.debug(cmd)
        proc = Popen(cmd, stdin=PIPE, stdout=PIPE)
        outs, errs = proc.communicate(input)
        if errs is None:
            return etree.XML("<sentences>{}</sentences>".format(outs))
        else:
            raise Exception(errs)

    def _build_param(self, key, val):
        return '--{}'.format(key), val

    def _build_flag(self, a):
        return '--{}'.format(a)

    def _build_cmd(self, *flags, **kwargs):
        cmd = [self.binary, '-f', self.config]

        for f in flags:
            flag = self._build_flag(f)
            if flag:
                cmd.append(flag)

        for key, val in iter(kwargs.items()):
            param, value = self._build_param(key, val)
            cmd += [param, value]

        cmd += ['--output', 'xml']
        return cmd

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
