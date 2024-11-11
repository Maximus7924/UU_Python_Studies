import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        m = Runner('Maxim')
        counter = 0
        while counter < 10:
            m.walk()
            counter += 1
        self.assertEqual(m.distance, 50)
    
    
    def test_run(self):
        d = Runner('Dima')
        counter = 0
        while counter < 10:
            d.run()
            counter +=1
        self.assertEqual(d.distance, 100)
        
        
    def test_challenge(self):
        c1 = Runner('Sergey')
        c2 = Runner('Anatoly')
        counter = 0
        while counter < 10:
            c1.run()
            c2.walk()
            counter +=1
        self.assertNotEqual(c1.distance, c2.distance)
    
    
if __name__ == '__main__':
    unittest.main()