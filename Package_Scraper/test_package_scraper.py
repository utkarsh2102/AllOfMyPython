#! /usr/bin/env python3

''' Unit testing file for the package_scraper.py script '''

import unittest
import os
import shutil
import package_scraper

class TestPackageScraper(unittest.TestCase):
    ''' Test class to make the methods for testing the original utility methods '''

    __test_url = 'https://qa.debian.org/developer.php?login=guptautkarsh2102@gmail.com'

    def test_get_file_name(self):
        ''' Test method for testing get_file_name function '''
        # matching cases
        self.assertEqual(package_scraper.get_file_name(self.__test_url), 'guptautkarsh2102')
        self.assertEqual(package_scraper.get_file_name('https://qa.debian.org/developer.php?login=silvertaurus4869@gmail.com'), 'silvertaurus4869')
        self.assertEqual(package_scraper.get_file_name('https://qa.debian.org/developer.php?login=3258224624@gmail.com'), '3258224624')
        self.assertEqual(package_scraper.get_file_name('https://qa.debian.org/developer.php?login=random_something@gmail.com'), 'random_something')
    
        # non-matching cases
        with self.assertRaises(IndexError):
            self.assertEqual(package_scraper.get_file_name('https://qa.debian.org/developer.php?login=random?something#randomrandom@gmail.com'), 'random?something#randomrandom ')
            self.assertEqual(package_scraper.get_file_name('https://qa.debian.org/developer.php?login=?#_wet%$67389@random@gmail.com'), '?#_wet%$67389@random')

    def test_package_file(self):
        ''' Test method for testing package_file function '''
        file_name = package_scraper.get_file_name(self.__test_url)
        os.mkdir('test')
        os.chdir('./test')
        for _ in package_scraper.package_file((file_name), self.__test_url):
            continue
        self.assertEqual(os.path.exists('./{}.txt'.format(file_name)), True)
        os.chdir('../')
        shutil.rmtree('./test')

    def test_log_file(self):
        ''' Test method for testing log_file function '''
        file_name = package_scraper.get_file_name(self.__test_url)
        os.mkdir('test')
        os.chdir('./test')
        package_scraper.log_file(file_name, set())
        self.assertEqual(os.path.exists('./{}_log.txt'.format(file_name)), True)
        os.chdir('../')
        shutil.rmtree('./test')


if __name__ == '__main__':
    unittest.main()