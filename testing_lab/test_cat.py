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


class Cat:
    def __init__(self, name):
        _log.info("Cat.__init__ - called... name: %s", name)
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        _log.info("Cat.cat - called ... self : '%r'", self)

        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

        _log.info("Cat.cat ... done! (fed: %r, sleepy: %r, size: %r)", self.fed, self.sleepy, self.size)

    def sleep(self):
        _log.info("Cat.sleep - called...self: %r", self)

        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False

        _log.info("Cat.sleep ... Done! (fed: %r, sleepy: %r)", self.fed, self.sleepy)

    def __repr__(self) -> str:
        return "%s(name=%r, fed= %r, sleepy=%r, size=%d)" % (
            type(self).__name__,
            self.name,
            self.fed,
            self.sleepy,
            self.size
        )


from unittest import TestCase
from unittest import main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Test")

    def test_cat_is_initialized_correctly(self):
        self.assertEqual("Test", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_eat(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_cat_eat_is_fed_raises(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_cat_tries_to_sleep_is_not_fed_raises(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)

    def test_cat_is_fed_and_can_go_to_sleep(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.assertTrue(self.cat.fed)

        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    init_logging()  # Comment this for judge
    main()
