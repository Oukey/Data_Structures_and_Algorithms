import unittest
import testLL

link_list_suite = unittest.TestSuite()
link_list_suite.addTest(unittest.makeSuite(testLL.LinkedListTest))
link_list_suite.addTest(unittest.makeSuite(testLL.LinkedListTest1))
link_list_suite.addTest(unittest.makeSuite(testLL.LinkedListTest3))
print('count of test: ' + str(link_list_suite.countTestCases()) + '\n')

runner = unittest.TextTestRunner(verbosity=2)
runner.run(link_list_suite)
