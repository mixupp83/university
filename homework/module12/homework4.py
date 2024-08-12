import unittest
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
    filename='runner_tests.log',
    filemode='w',
    encoding='UTF-8'
)


class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if speed < 0:
            raise ValueError("Speed must be non-negative")
        self.name = name
        self.speed = speed
        self.distance = 0

    def walk(self):
        self.distance += self.speed * 0.5

    def run(self):
        self.distance += self.speed

    def __eq__(self, other):
        return self.name == other.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            runner = Runner(name="John", speed=-1)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(name=123, speed=10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        runner1 = Runner(name="Alice", speed=10)
        runner2 = Runner(name="Bob", speed=10)

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()