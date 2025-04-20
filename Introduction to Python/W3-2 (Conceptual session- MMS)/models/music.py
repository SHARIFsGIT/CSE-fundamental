from models.media import Media, Description

class Genre:
    """Class to represent music genres."""
    
    # Class variable to store all available genres
    GENRES = ["Pop", "Rock", "Hip Hop", "Classical", "Jazz", "Electronic", "Country", "R&B", "Metal", "Folk"]
    
    @classmethod
    def is_valid_genre(cls, genre):
        """
        Check if a genre is valid.
        
        Args:
            genre (str): The genre to check
            
        Returns:
            bool: True if the genre is valid, False otherwise
        """
        return genre in cls.GENRES
    
    @classmethod
    def get_all_genres(cls):
        """
        Get all available genres.
        
        Returns:
            list: All available genres
        """
        return cls.GENRES.copy()


class Music(Media, Description):
    """
    Class representing a music track.
    Inherits from Media and Description.
    """
    
    def __init__(self, title, duration, artist, genre=None, album=None, release_date=None):
        """
        Initialize a Music object.
        
        Args:
            title (str): The title of the song
            duration (float): The duration in minutes
            artist (str): The artist/band name
            genre (str, optional): The music genre
            album (str, optional): The album name
            release_date (str, optional): Release date in YYYY-MM-DD format
        """
        # Call parent class initializers
        Media.__init__(self, title, duration, release_date)
        Description.__init__(self, artist)
        
        # Music-specific attributes
        self.__artist = artist
        self.__genre = genre if genre and Genre.is_valid_genre(genre) else None
        self.__album = album
        self.__play_count = 0
        self.__likes = 0
        self.__file_path = None
    
    @property
    def artist(self):
        """Get the artist name."""
        return self.__artist
    
    @property
    def genre(self):
        """Get the genre."""
        return self.__genre
    
    @property
    def album(self):
        """Get the album name."""
        return self.__album
    
    @property
    def play_count(self):
        """Get the number of times the song has been played."""
        return self.__play_count
    
    @property
    def likes(self):
        """Get the number of likes."""
        return self.__likes
    
    @property
    def file_path(self):
        """Get the file path."""
        return self.__file_path
    
    @file_path.setter
    def file_path(self, path):
        """Set the file path."""
        self.__file_path = path
    
    def add_like(self):
        """Add a like to the song."""
        self.__likes += 1
        return self.__likes
    
    def remove_like(self):
        """Remove a like from the song."""
        if self.__likes > 0:
            self.__likes -= 1
        return self.__likes
    
    def play(self):
        """
        Play the music track.
        
        Returns:
            str: A message indicating the track is playing
        """
        if not self.is_playing:
            self.is_playing = True
            self.__play_count += 1
            return f"▶️ Playing music: {self.title} by {self.get_description()}"
        return f"⚠️ {self.title} is already playing!"
    
    def stop(self):
        """
        Stop playing the music track.
        
        Returns:
            str: A message indicating the track has stopped
        """
        if self.is_playing:
            self.is_playing = False
            return f"⏹️ Stopped playing: {self.title}"
        return f"⚠️ {self.title} is not currently playing!"
    
    def get_full_info(self):
        """
        Get detailed information about the music track.
        
        Returns:
            str: Formatted detailed information string
        """
        # Get basic info from parent class
        info = self.get_info()
        
        # Add music-specific details
        info += f"\nArtist: {self.__artist}"
        if self.__album:
            info += f"\nAlbum: {self.__album}"
        if self.__genre:
            info += f"\nGenre: {self.__genre}"
        
        info += f"\nPlay Count: {self.__play_count}"
        info += f"\nLikes: {self.__likes}"
        
        return info