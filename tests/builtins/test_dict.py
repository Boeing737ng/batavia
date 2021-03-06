from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class DictTests(TranspileTestCase):
    pass


class BuiltinDictFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    function = "dict"

    def test_well_formatted_set(self):
        self.assertCodeExecution("""
            good_set = {(1, 2), (2, 3)}
            print(dict(good_set))
            """)
