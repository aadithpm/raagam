

class ArtistsResponse():

    def __init__(self, response):
        self.data = response

    def extract_artist_id(self, name):
        # TODO: Handle multiple artists with similar name
        artists = self.data["items"]
        for artist_number in artists:
            if artists[artist_number]["name"] == name:
                return artists[artist_number]["id"]
