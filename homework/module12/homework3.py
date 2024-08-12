import unittest
from unittest import TextTestRunner


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


def skip_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_frozen
    def test_walk(self):
        runner = Runner(name="John", speed=10)  # Исправлена скорость
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_frozen
    def test_run(self):
        runner = Runner(name="Jane", speed=10)  # Исправлена скорость
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_frozen
    def test_challenge(self):
        runner1 = Runner(name="Alice", speed=10)  # Исправлена скорость
        runner2 = Runner(name="Bob", speed=10)  # Исправлена скорость

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @skip_frozen
    def test_race_usain_nik(self):
        tournament = Tournament(distance=90, participants=[self.usain, self.nik])
        result = tournament.start()
        self.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @skip_frozen
    def test_race_andrey_nik(self):
        tournament = Tournament(distance=90, participants=[self.andrey, self.nik])
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @skip_frozen
    def test_race_usain_andrey_nik(self):
        tournament = Tournament(distance=90, participants=[self.usain, self.andrey, self.nik])
        result = tournament.start()
        self.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == "Ник")


# Модуль suite_12_3.py
if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    runner = TextTestRunner(verbosity=2)

    runner.run(suite)
