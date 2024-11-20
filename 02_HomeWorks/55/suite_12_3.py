import unittest
import test_12_3
import tests_12_1


tts = unittest.TestSuite()


tts.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
tts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tts)

