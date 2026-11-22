"""素杪（SUMIAO）· 底层原子算子库

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：底层原子算子库。

边界：本件为算子骨架 v0——接口先立、实现随进化轮补齐；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Sumiao:
    """素杪（SUMIAO）算子骨架 v0。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "SUMIAO"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕

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
        """原子算子准入登记（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("SUMIAO.register 骨架桩，候进化轮补齐")

    def call(self, op_name, args):
        """起于微杪：调用已登记原子算子（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("SUMIAO.call 骨架桩，候进化轮补齐")
