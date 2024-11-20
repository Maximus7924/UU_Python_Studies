# Доработан согласно заданию, источник 'test_12_2_v1.py' из предыдущего задания
import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        
    is_frozen = True
        
        
    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)
    
    
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge_1(self):
        
        self.t1 = Tournament(90, self.r1, self.r3)
        self.t1_res = self.t1.start()
        self.t1_last_pos = (list(self.t1_res.keys())[-1])
        
        self.t1_rep = {key:value.name for (key,value) in self.t1_res.items()}
        
        TournamentTest.all_results.update({"t1": self.t1_rep})
        self.assertTrue(self.t1_res.get(self.t1_last_pos) == self.r3.name)
    
    
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge_2(self):
        self.t2 = Tournament(90, self.r2, self.r3)
        self.t2_res = self.t2.start()
        self.t2_last_pos = (list(self.t2_res.keys())[-1])
        
        self.t2_rep = {key:value.name for (key,value) in self.t2_res.items()}
        
        TournamentTest.all_results.update({"t2": self.t2_rep})
        self.assertTrue(self.t2_res.get(self.t2_last_pos) == self.r3.name)
    
    
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge_3(self):
        self.t3 = Tournament(90, self.r1, self.r2, self.r3)
        self.t3_res = self.t3.start()
        self.t3_last_pos = (list(self.t3_res.keys())[-1])
        
        self.t3_rep = {key:value.name for (key,value) in self.t3_res.items()}
        
        TournamentTest.all_results.update({"t3": self.t3_rep})
        self.assertTrue(self.t3_res.get(self.t3_last_pos) == self.r3.name)
    
    
    @classmethod
    def tearDownClass(cls):
        print()
        for key_t in TournamentTest.all_results:
            t_res = TournamentTest.all_results.get(key_t)
            print(t_res)
            

if __name__ == '__main__':
    unittest.main()