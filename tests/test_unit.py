import unittest
from artist import artists_handler_spotify


class ArtistsHandlerTest(unittest.TestCase):

    def setUp(self):
        self.test_data_simple = {
            "artists": {
                "items": [
                    {
                        "id": "12Chz98pHFMPJEknJQMWvI",
                        "name": "Muse",
                        "href": "http://open.spotify.com/muse",
                    },
                    {
                        "id": "123456",
                        "name": "I Don't Exist",
                        "href": "http://open.spotify.com/idontexist",
                    }
                ]
            }
        }

        self.test_data_multiple = {}
        self.response_handler = artists_handler_spotify.ArtistsResponse(
            self.test_data_simple["artists"]
        )

    def test_canary(self):
        self.assertTrue(True)

    def test_extract_artist_gets_artist_data(self):
        test_artist = self.test_data_simple["artists"]["items"][0]
        name_to_use = test_artist["name"]
        id_to_check = test_artist["id"]

        self.assertEqual(
            id_to_check, self.response_handler.extract_artist_id(name_to_use))

    def test_extract_artist_returns_none_when_no_artist(self):
        name_to_use = "I Should Return None"

        self.assertEqual(
            None, self.response_handler.extract_artist_id(name_to_use))

    def test_get_all_artist_names(self):
        self.assertEqual(
            ["Muse", "I Don't Exist"],
            self.response_handler.get_all_artist_names()
        )

    def test_get_artist_url(self):
        test_artist_id = "123456"

        self.assertEqual(
            "http://open.spotify.com/idontexist",
            self.response_handler.get_artist_url(test_artist_id)
        )
