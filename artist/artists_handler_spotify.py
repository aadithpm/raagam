

class ArtistsResponse():

    def __init__(self, response):
        self.data = response
        self.artists = self.data["items"]

    def extract_artist_id(self, name):
        for artist_number in self.artists:
            if self.artists[artist_number]["name"] == name:
                return self.artists[artist_number]["id"]
