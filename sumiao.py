"""素杪（SUMIAO）· 底层原子算子库

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：底层原子算子库。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Sumiao:
    """素杪（SUMIAO）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "SUMIAO"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.ops = {}

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "sumiao",
            "cn": "素杪",
            "code": self.CODE,
            "duty": "底层原子算子库",
            "mingwen": "起于微杪，成于推演",
            "anchor": self.ANCHOR,
        }

    def register(self, op):
        """微杪入库：原子算子登记。"""
        if isinstance(op, dict):
            name, fn = op.get("name"), op.get("fn")
        else:
            name, fn = getattr(op, "__name__", None), op
        if not name or not callable(fn):
            raise ValueError("原子算子须有名且可调用")
        self.ops[name] = fn
        self.events.append({"event": "register", "op": name})
        return name

    def call(self, op_name, args):
        """成于推演：按名调用原子算子。"""
        if op_name not in self.ops:
            raise KeyError("无此算子： %s" % op_name)
        result = self.ops[op_name](*args)
        self.events.append({"event": "call", "op": op_name})
        return result
