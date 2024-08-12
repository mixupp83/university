import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def walk(self):
        self.distance += self.speed * 0.5

    def run(self):
        self.distance += self.speed

    def __eq__(self, other):
        return self.name == other.name

class Tournament:
    def __init__(self, distance, participants):
        self.distance = distance
        self.participants = participants

    def start(self):
        results = {}
        for i, participant in enumerate(self.participants, start=1):
            while participant.distance < self.distance:
                participant.run()
            results[i] = participant.name
        return results

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner(name="Усэйн", speed=10)
        self.andrey = Runner(name="Андрей", speed=9)
        self.nik = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(cls.all_results[key])

    def test_race_usain_nik(self):
        tournament = Tournament(distance=90, participants=[self.usain, self.nik])
        result = tournament.start()
        self.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_andrey_nik(self):
        tournament = Tournament(distance=90, participants=[self.andrey, self.nik])
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_usain_andrey_nik(self):
        tournament = Tournament(distance=90, participants=[self.usain, self.andrey, self.nik])
        result = tournament.start()
        self.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()