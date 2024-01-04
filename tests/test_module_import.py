import unittest

class TestModuleImport(unittest.TestCase):
    def setUp(self):
        import sys
        sys.path.insert(0, '..')

    def test_no_error_test_import(self):
        try:
            import qcge
        except Exception as error:
            self.fail(f"Failed import: {error}")

if __name__ == '__main__':
    unittest.main()
