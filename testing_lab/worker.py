import logging

_log = logging.getLogger(__name__)
_log.addHandler(logging.NullHandler())


def init_logging():
    import sys  # noqa
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)3d | %(levelname)9s | %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout
    )


class Worker:
    def __init__(self, name, salary, energy):
        _log.info("Worker.__init__ - called... (name: '%s', salary: %s, energy: %s)", name, salary, energy)
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        _log.info("Worker.work - called ... self: %r", self)
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1
        _log.info("Worker.work ...done! (energy: %s, money: %s)", self.energy, self.money)

    def rest(self):
        _log.info("Worker.rest - called ... Worker info: %r", self)
        self.energy += 1
        _log.info("Worker.rest ... done! energy: %r", self.energy)

    def get_info(self):
        # raise NotImplemented()
        _log.info("Worker.get_info called... self: %r", self)
        result = f'{self.name} has saved {self.money} money.'
        _log.info("Worker.get_info ...done! result: '%s'", result)
        return result

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return "%s(name=%r, salary=%.2f, energy=%d, money=%.2f)" % (
            type(self).__name__,
            self.name,
            self.salary,
            self.energy,
            self.money
        )


from unittest import TestCase
from unittest import main


class WorkerTests(TestCase):
    def test_worker_is_initialized_correctly(self):
        # Act
        worker = Worker("Test", 1000, 60)

        # Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(60, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_works(self):
        worker = Worker("Test", 1000, 60)

        # Arrange
        self.assertEqual(0, worker.money)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(60, worker.energy)

        # Act
        worker.work()

        # Assert
        current_expected_money = 1000
        self.assertEqual(current_expected_money, worker.money)
        expected_energy = 60 - 1
        self.assertEqual(expected_energy, worker.energy)

        # worker works again
        # Act
        worker.work()

        # Assert
        current_expected_money = 1000 + 1000
        self.assertEqual(current_expected_money, worker.money)
        expected_energy = 60 - 1 - 1
        self.assertEqual(expected_energy, worker.energy)

    def test_worker_has_no_energy_cannot_work(self):
        worker = Worker("Test", 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", ex.exception.args[0])

    def test_worker_cannot_work_with_negative_energy(self):
        worker = Worker("Test", 1000, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", ex.exception.args[0])

    def test_worker_energy_is_increased_when_worker_rests(self):
        worker = Worker("Test", 1000, 60)

        # Arrange
        self.assertEqual(60, worker.energy)

        # Act
        worker.rest()

        # Assert
        expected_energy = 60 + 1
        self.assertEqual(expected_energy, worker.energy)

        # Act
        worker.rest()

        # Assert
        expected_energy = 60 + 1 + 1
        self.assertEqual(expected_energy, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker("Test", 1000, 60)

        # Act
        result = worker.get_info()

        # Assert
        expected_result = "Test has saved 0 money."
        self.assertEqual(expected_result, result)

        # Act
        worker.work()
        result = worker.get_info()

        # Assert
        expected_result = "Test has saved 1000 money."
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    init_logging()  # Comment this for judge
    main()
