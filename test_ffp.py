from main import app
class TestClass(object):
    def setup_class(self):
        self.app = app.test_client()
    def test_home_page(self):
        rv = self.app.get('/')
        assert rv.status_code == 302
        assert rv.data == 'ffp'