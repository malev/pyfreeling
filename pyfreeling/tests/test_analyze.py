import unittest
from .. import find_binary, Analyzer


class FindBinaryTestCase(unittest.TestCase):
    def test_find_binary(self):
        self.assertTrue(find_binary().endswith('analyze'))


class AnalyzeTestCase(unittest.TestCase):
    def test__build_param(self):
        self.assertEqual(
            Analyzer()._build_param('lang', 'en'),
            ('--lang', 'en')
        )

    def test__build_flag(self):
        self.assertEqual(Analyzer()._build_flag('noflush'), '--noflush')

    def test__build_cmd(self):
        cmd = Analyzer(config='config.cfg')._build_cmd('noflush', lang='en')
        self.assertEqual(
            cmd[1:],
            [
                '-f', 'config.cfg', '--noflush',
                '--lang', 'en', '--output', 'json'
            ]
        )
