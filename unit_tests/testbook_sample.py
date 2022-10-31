from testbook import testbook

@testbook('./ipynb_to_test/test.json.ipynb', execute=True)
def test_func(tb):
   func = tb.ref("hello")

   assert func() == 'Hello World!'