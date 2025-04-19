import unittest
import threading
from creational_patterns.singleton import DatabaseConnection

class TestSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        instance1 = DatabaseConnection()
        instance2 = DatabaseConnection()
        self.assertIs(instance1, instance2)
        self.assertEqual(instance1.get_connection(), "Connected to DB")

    def test_thread_safety(self):
        instances = []

        def create_instance():
            instances.append(DatabaseConnection())

        threads = [threading.Thread(target=create_instance) for _ in range(10)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        for instance in instances:
            self.assertIs(instance, instances[0])

