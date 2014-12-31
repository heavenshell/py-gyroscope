#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" gyroscope
    ~~~~~~~~~

    gyroscope is just rotate file.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import shutil
import optparse
import logging
import logging.handlers


class Gyroscope(object):
    def __init__(self, logger=None):
        self.logger = logger

    def run(self, filepath, rotation_count):
        """
        Rotate file.

        .. code-block:

            $ python backup.py -p ./sample.txt -n 3
            #  copy sample.txt to sample.txt.1
            $ python backup.py -p ./sample.txt
            #  mv sample.txt.1 to sample.txt.2
            #  cp sample.txt to sample.txt.1
            $ python backup.py -p ./sample.txt
            #  mv sample.txt.2 to sample.txt.3
            #  mv sample.txt.1 to sample.txt.2
            #  cp sample.txt to sample.txt.1
            $ python backup.py -p ./sample.txt
            #  rm sample.txt.3
            #  mv sample.txt.2 to sample.txt.3
            #  mv sample.txt.1 to sample.txt.2
            #  cp sample.txt to sample.txt.1

        :param filepath: Path to rotation file
        :param rotation_count: Rotation count
        """
        self.logger.info('----------------Start rotation.----------------')
        i = rotation_count - 1
        lastfile = '{0}.{1}'.format(filepath, rotation_count)
        if os.path.exists(lastfile):
            self.logger.info('{0}, file is last.'.format(lastfile))
            os.remove(lastfile)
            self.logger.info('{0}, delete success'.format(lastfile))
        else:
            pass

        j = 0
        while i >= 1:
            j = i + 1
            dest = '{0}.{1}'.format(filepath, j)
            src = '{0}.{1}'.format(filepath, i)
            if os.path.exists(src):
                self.logger.info('Start move {0} to {1}'.format(src, dest))
                os.rename(src, dest)
                self.logger.info('Move {0} to {1} success.'.format(src, dest))

            i -= 1

        self.logger.info('Start move {0} to {1}.1'.format(src, dest))
        shutil.copy2(filepath, '{0}.{1}'.format(filepath, 1))
        self.logger.info('Move {0} to {1}.1 success.'.format(src, dest))
        self.logger.info('-----------------End rotation.-----------------')


def main(filepath, rotation_count):
    logformat = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=logformat)
    logger = logging.getLogger('gyroscope')
    logger.level = logging.INFO

    trh = logging.handlers.TimedRotatingFileHandler(
        filename=options.logfile_path,
        when='D',
        backupCount=7
    )
    trh.setLevel(logging.INFO)
    logger.addHandler(trh)

    g = Gyroscope(logger)
    g.run(filepath, rotation_count)


def parse_option():
    """Parse option.

    A lot of system Python's version is still 2.6.
    `argparse` requires Python2.7, so use optparse instead.
    """
    usage = 'usage: %prog [options] keyword'
    parser = optparse.OptionParser(usage)
    parser.add_option('-p', '--path', default=None)
    parser.add_option('-n', '--rotation-number', default=3)
    parser.add_option('-l', '--logfile-path', default='./rotation.log')

    options, args = parser.parse_args()

    return options


if __name__ == '__main__':
    options = parse_option()

    main(options.path, options.rotation_number)
