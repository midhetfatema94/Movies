import webbrowser

class Movie():
    def __init__ (self, title, poster_image, storyline, youtube_url):
        self.title = title;
        self.poster_image_url = poster_image;
        self.storyline = storyline;
        self.trailer_youtube_url = youtube_url;

    def show_trailer(self):
        webbrowser.open(self.youtube_url);
