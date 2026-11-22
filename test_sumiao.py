"""素杪（SUMIAO）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_register_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.register(None)

    def test_call_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.call(None, None)


if __name__ == "__main__":
    unittest.main()
