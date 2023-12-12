import pytest
from flask_testing import TestCase
from app import app
from flask import url_for

class TestIntegration(TestCase):
    def create_app(self):
        return app

    def test_main_route(self):
        response = self.client.get('/')
        self.assert200(response)

    def test_update_route(self):
        response = self.client.post('/update')
        self.assertEqual(response.status_code, 302)  

    def test_fan_happiness_level_route(self):
        response = self.client.get('/fan-happiness-level?team_db=lakers.db')
        self.assert200(response)

    def test_main_route_redirect(self):
     with app.test_request_context():
        redirect_url = url_for('display_mood', _external=True) + '?team_db=lakers.db'
        print(redirect_url)
     response = self.client.post('/', data={'team': 'lakers'})
     self.assertEqual(response.location, redirect_url[len('http://localhost'):])



if __name__ == '__main__':
    pytest.main()
