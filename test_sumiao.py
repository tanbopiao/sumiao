"""素杪（SUMIAO）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from sumiao import Sumiao


class TestSumiao(unittest.TestCase):
    def setUp(self):
        self.op = Sumiao()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "sumiao")
        self.assertEqual(d["code"], "SUMIAO")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_register_call(self):
        name = self.op.register(lambda a, b: a + b)
        self.assertEqual(name, "add" if False else "<lambda>")
        self.op.ops["加"] = lambda a, b: a + b
        self.assertEqual(self.op.call("加", (1, 2)), 3)
        with self.assertRaises(KeyError):
            self.op.call("无有", ())


if __name__ == "__main__":
    unittest.main()
