import unittest
from artist import artists_handler_spotify


class Unittest(unittest.TestCase):

    def test_canary(self):
        self.assertTrue(True)


class ArtistsHandlerTest(unittest.TestCase):

    def setUp(self):
        self.test_data_simple = {
            "artists": {
                "items": {
                    0: {
                        "id": "12Chz98pHFMPJEknJQMWvI",
                        "name": "Muse",
                    },
                    1: {
                        "id": "123456",
                        "name": "I Don't Exist",
                    }
                }
            }
        }
        self.test_data_multiple = {}

    def test_extract_artist_gets_artist_data(self):
        test_artist = self.test_data_simple["artists"]["items"][0]
        name_to_use = test_artist["name"]
        id_to_check = test_artist["id"]
        response_handler = artists_handler_spotify.ArtistsResponse(
            self.test_data_simple["artists"]
        )

        self.assertEquals(
            id_to_check, response_handler.extract_artist_id(name_to_use))
