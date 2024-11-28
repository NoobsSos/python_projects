import unittest

def run_test(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    print("\nРезультати тестування:")
    runner.run(suite)
