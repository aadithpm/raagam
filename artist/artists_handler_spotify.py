

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
        return [artist["name"] for artist in self.artists]

    def extract_artist_id(self, name):
        for artist in self.artists:
            if artist["name"] == name:
                return artist["id"]

    def get_artist_url(self, id):
        """
        Returns the Spotify page URL for an ID
        """
        for artist in self.artists:
            if artist["id"] == id:
                return artist["href"]
