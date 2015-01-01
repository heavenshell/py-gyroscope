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

    def compare_filestat(self, src, dest):
        if not os.path.exists(src) or not os.path.exists(dest):
            return False

        src_stat = os.stat(src)
        dest_stat = os.stat(dest)
        if src_stat.st_mtime == dest_stat.st_mtime:
            self.logger.info('{0} and {1} is same file.'.format(src, dest))
            return True

        return False

    def run(self, filepath, rotation_count, force_rotate=False):
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
            #: Check lastfile and lastfile - 1 file is same.
            ret = self.compare_filestat('{0}.{1}'.format(filepath, i), lastfile)
            if ret is False:
                self.logger.info('{0}, file is last.'.format(lastfile))
                os.remove(lastfile)
                self.logger.info('{0}, delete success'.format(lastfile))

        j = 0
        while i >= 1:
            j = i + 1
            dest = '{0}.{1}'.format(filepath, j)
            src = '{0}.{1}'.format(filepath, i)
            if os.path.exists(src):
                ret = self.compare_filestat(src, dest)
                if ret is False:
                    self.logger.info('Start move {0} to {1}'.format(src, dest))
                    os.rename(src, dest)
                    self.logger.info('Move {0} to {1} success.'.format(src, dest))

            i -= 1

        ret = self.compare_filestat(filepath, '{0}.1'.format(filepath))
        if ret is False:
            self.logger.info('Start move {0} to {0}.1'.format(filepath))
            shutil.copy2(filepath, '{0}.{1}'.format(filepath, 1))
            self.logger.info('Move {0} to {0}.1 success.'.format(filepath))


        self.logger.info('-----------------End rotation.-----------------')
def main(filepath, rotation_count, force_rotate=False):
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
    g.run(filepath, rotation_count, force_rotate)


def parse_option():
    """Parse option.

    A lot of system Python's version is still 2.6.
    `argparse` requires Python2.7, so use optparse instead.
    """
    usage = 'usage: %prog [options] keyword'
    parser = optparse.OptionParser(usage)
    parser.add_option('-p', '--path', default=None)
    parser.add_option('-n', '--rotation-number', default=3, type='int')
    parser.add_option('-l', '--logfile-path', default='./rotation.log')
    parser.add_option('-f', '--force-rotate', default=False)

    options, args = parser.parse_args()

    return options


if __name__ == '__main__':
    options = parse_option()
    main(options.path, options.rotation_number, options.force_rotate)
