

class ArtistsResponse():

    def __init__(self, response):
        self.data = response
        self.artists = self.data["items"]

    def get_all_artist_names(self):
        """
        Response from API is all artists that match a user-inputted string.
        This method simply returns all those artists as a list. Looking to
        use this for when a user enters a string and suggestions pop up in
        the input field
        """
        return [self.artists[artist]["name"] for artist in self.artists]

    def extract_artist_id(self, name):
        for artist_number in self.artists:
            if self.artists[artist_number]["name"] == name:
                return self.artists[artist_number]["id"]
