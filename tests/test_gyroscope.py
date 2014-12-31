# -*- coding: utf-8 -*-
"""
    gyroscope.tests.test_gyroscope
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for gyroscope.


    :copyright: (c) 2015 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import logging
from unittest import TestCase
from gyroscope import Gyroscope


class TestGyroscope(TestCase):
    def setUp(self):
        logger = logging.getLogger('gyroscope')
        logger.level = logging.ERROR
        self.gyroscope = Gyroscope(logger)

        self.current = os.path.dirname(os.path.abspath(__file__))
        print(self.current)
        fixtures = [
            '{0}/test.txt.1'.format(self.current),
            '{0}/test.txt.2'.format(self.current),
            '{0}/test.txt.3'.format(self.current)
        ]
        for f in fixtures:
            if os.path.exists(f):
                os.remove(f)

    def test_do_rotate_1(self):
        self.gyroscope.run('{0}/test.txt'.format(self.current), 3)
        self.assertTrue(os.path.exists('{0}/test.txt.1'.format(self.current)))
        self.assertFalse(os.path.exists('{0}/test.txt.2'.format(self.current)))
        self.assertFalse(os.path.exists('{0}/test.txt.3'.format(self.current)))

    def test_do_rotate_2(self):
        self.gyroscope.run('{0}/test.txt'.format(self.current), 3)
        self.assertTrue(os.path.exists('{0}/test.txt.1'.format(self.current)))
        self.gyroscope.run('{0}/test.txt'.format(self.current), 3)
        self.assertTrue(os.path.exists('{0}/test.txt.2'.format(self.current)))
        self.assertFalse(os.path.exists('{0}/test.txt.3'.format(self.current)))

    def test_do_rotate_3(self):
        self.gyroscope.run('{0}/test.txt'.format(self.current), 3)
        self.assertTrue(os.path.exists('{0}/test.txt.1'.format(self.current)))
        self.gyroscope.run('{0}/test.txt'.format(self.current), 3)
        self.assertTrue(os.path.exists('{0}/test.txt.2'.format(self.current)))
        self.gyroscope.run('{0}/test.txt'.format(self.current), 3)
        self.assertTrue(os.path.exists('{0}/test.txt.3'.format(self.current)))

    def test_do_rotate_4(self):
        self.gyroscope.run('{0}/test.txt'.format(self.current), 3)
        self.assertTrue(os.path.exists('{0}/test.txt.1'.format(self.current)))
        self.gyroscope.run('{0}/test.txt'.format(self.current), 3)
        self.assertTrue(os.path.exists('{0}/test.txt.2'.format(self.current)))
        self.gyroscope.run('{0}/test.txt'.format(self.current), 3)
        self.assertTrue(os.path.exists('{0}/test.txt.3'.format(self.current)))
        self.gyroscope.run('{0}/test.txt'.format(self.current), 3)
        self.assertFalse(os.path.exists('{0}/test.txt.4'.format(self.current)))
