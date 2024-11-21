import unittest
from rt_with_exceptions import Runner
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(funcName)s at line %(lineno)s | %(message)s')
handler = logging.FileHandler('runner_test.log', 'w', 'UTF-8')
handler.setFormatter(formatter)
logger.addHandler(handler)


class RunnerTest(unittest.TestCase):
    is_frozen = False
    
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            m = Runner('Maxim', -5)
            logger.info('"test_walk" выполнен успешно')
            counter = 0
            while counter < 10:
                m.walk()
                counter += 1
            self.assertEqual(m.distance, 50)
        except ValueError as wrn:
            logger.warning(f"Неверная скорость для Runner,\n\t {wrn}")
    
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            d = Runner([1, 2, 3], 25)
            logger.info('"test_run" выполнен успешно')
            counter = 0
            while counter < 10:
                d.run()
                counter += 1
            self.assertEqual(d.distance, 100)
        except TypeError as wrn:
            logger.warning(f"Неверный тип данных для объекта Runner,\n\t {wrn}")
    
    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        c1 = Runner('Sergey', 10)
        c2 = Runner('Anatoly', 12)
        counter = 0
        while counter < 10:
            c1.run()
            c2.walk()
            counter += 1
        self.assertNotEqual(c1.distance, c2.distance)


if __name__ == '__main__':
    unittest.main()