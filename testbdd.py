import unittest
from unittest.mock import patch, MagicMock
from database import BDD

class TestBDD(unittest.TestCase):

    @patch('mysql.connector.connect')
    def setUp(self, mock_connect):
        self.mock_db = MagicMock()
        mock_connect.return_value = self.mock_db
        self.bdd = BDD()

    @patch('mysql.connector.connect')
    def test_get_all_formations(self, mock_connect):
        mock_cursor = MagicMock()
        self.mock_db.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            (1, 'Formation1', 'Description1', 'Lieu1'),
            (2, 'Formation2', 'Description2', 'Lieu2')
        ]

        expected_result = [
            {"id": 1, "nom": "Formation1", "description": "Description1", "lieux": "Lieu1"},
            {"id": 2, "nom": "Formation2", "description": "Description2", "lieux": "Lieu2"}
        ]

        result = self.bdd.get_all_formations()
        self.assertEqual(result, expected_result)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM `uppa_formation`;")
        mock_cursor.close.assert_called_once()

    @patch('mysql.connector.connect')
    def test_get_all_groupe(self, mock_connect):
        mock_cursor = MagicMock()
        self.mock_db.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            (1, 'Groupe1', 'Link1'),
            (2, 'Groupe2', 'Link2')
        ]

        expected_result = [
            {"id": 1, "nom": "Groupe1", "ics_link": "Link1"},
            {"id": 2, "nom": "Groupe2", "ics_link": "Link2"}
        ]

        result = self.bdd.get_all_groupe()
        self.assertEqual(result, expected_result)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM `uppa_groupe`;")
        mock_cursor.close.assert_called_once()

    @patch('mysql.connector.connect')
    def test_get_ics_link(self, mock_connect):
        mock_cursor = MagicMock()
        self.mock_db.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('Link1',)]

        result = self.bdd.get_ics_link(1)
        self.assertEqual(result, 'Link1')
        mock_cursor.execute.assert_called_once_with("SELECT ics_link FROM `uppa_groupe` WHERE id = 1;")
        mock_cursor.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()