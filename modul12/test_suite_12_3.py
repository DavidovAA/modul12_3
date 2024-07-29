import unittest
import Ex1
import Ex2

run_test = unittest.TestSuite()
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Ex1.RunnerTest))
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Ex2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_test)
