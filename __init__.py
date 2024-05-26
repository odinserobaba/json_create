import unittest

if __name__ == '__main__':
    def test_runner(path='.'):
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover(path, pattern='*_test.py')
        test_runner = unittest.TextTestRunner()
        test_runner.run(test_suite)
    test_runner()
    test_runner('xml_parser')
