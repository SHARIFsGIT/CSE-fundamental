class MusicDatabase:
    """
    A simple database for storing music tracks.
    In a real application, this would connect to an actual database.
    """
    
    def __init__(self):
        """Initialize the music database."""
        self.__tracks = {}  # Dictionary to store tracks by ID
        self.__next_id = 1  # Auto-increment ID
    
    def add_track(self, track):
        """
        Add a track to the database.
        
        Args:
            track (Music): The track to add
            
        Returns:
            int: The ID of the added track
        """
        track_id = self.__next_id
        self.__tracks[track_id] = track
        self.__next_id += 1
        return track_id
    
    def get_track(self, track_id):
        """
        Get a track by ID.
        
        Args:
            track_id (int): The ID of the track
            
        Returns:
            Music or None: The track, or None if not found
        """
        return self.__tracks.get(track_id)
    
    def update_track(self, track_id, track):
        """
        Update a track.
        
        Args:
            track_id (int): The ID of the track
            track (Music): The updated track
            
        Returns:
            bool: True if the track was updated, False if not found
        """
        if track_id in self.__tracks:
            self.__tracks[track_id] = track
            return True
        return False
    
    def delete_track(self, track_id):
        """
        Delete a track.
        
        Args:
            track_id (int): The ID of the track
            
        Returns:
            bool: True if the track was deleted, False if not found
        """
        if track_id in self.__tracks:
            del self.__tracks[track_id]
            return True
        return False
    
    def get_all_tracks(self):
        """
        Get all tracks in the database.
        
        Returns:
            list: All tracks in the database
        """
        return list(self.__tracks.values())
    
    def search_tracks(self, query):
        """
        Search for tracks by title, artist, or album.
        
        Args:
            query (str): The search query
            
        Returns:
            list: Matching tracks
        """
        query = query.lower()
        results = []
        
        for track in self.__tracks.values():
            if (query in track.title.lower() or 
                query in track.artist.lower() or 
                (track.album and query in track.album.lower())):
                results.append(track)
        
        return results
    
    def filter_by_genre(self, genre):
        """
        Filter tracks by genre.
        
        Args:
            genre (str): The genre to filter by
            
        Returns:
            list: Tracks with the specified genre
        """
        return [track for track in self.__tracks.values() if track.genre == genre]


class MusicService:
    """
    Service for managing music operations.
    """
    
    def __init__(self):
        """Initialize the music service."""
        self.__database = MusicDatabase()
        self.__initialize_sample_tracks()
    
    def __initialize_sample_tracks(self):
        """Add some sample tracks to the database."""
        from models.music import Music
        
        # Add some sample tracks
        samples = [
            Music("Shape of You", 3.9, "Ed Sheeran", "Pop", "÷ (Divide)", "2017-01-06"),
            Music("Bohemian Rhapsody", 5.9, "Queen", "Rock", "A Night at the Opera", "1975-10-31"),
            Music("Sicko Mode", 5.2, "Travis Scott", "Hip Hop", "Astroworld", "2018-08-03"),
            Music("Für Elise", 3.7, "Ludwig van Beethoven", "Classical", None, "1810-04-27"),
            Music("Take Five", 5.2, "Dave Brubeck", "Jazz", "Time Out", "1959-09-29"),
            Music("Strobe", 10.3, "Deadmau5", "Electronic", "For Lack of a Better Name", "2009-09-22"),
            Music("Jolene", 2.7, "Dolly Parton", "Country", "Jolene", "1973-10-15"),
            Music("No Diggity", 5.0, "Blackstreet", "R&B", "Another Level", "1996-09-10"),
            Music("Master of Puppets", 8.6, "Metallica", "Metal", "Master of Puppets", "1986-03-03"),
            Music("The Times They Are a-Changin'", 3.2, "Bob Dylan", "Folk", "The Times They Are a-Changin'", "1964-01-13")
        ]
        
        for track in samples:
            self.__database.add_track(track)
    
    def get_all_tracks(self):
        """
        Get all tracks.
        
        Returns:
            list: All tracks
        """
        return self.__database.get_all_tracks()
    
    def search_tracks(self, query):
        """
        Search for tracks.
        
        Args:
            query (str): The search query
            
        Returns:
            list: Matching tracks
        """
        return self.__database.search_tracks(query)
    
    def get_track(self, track_id):
        """
        Get a track by ID.
        
        Args:
            track_id (int): The ID of the track
            
        Returns:
            Music or None: The track, or None if not found
        """
        return self.__database.get_track(track_id)
    
    def add_track(self, track):
        """
        Add a track.
        
        Args:
            track (Music): The track to add
            
        Returns:
            int: The ID of the added track
        """
        return self.__database.add_track(track)
    
    def update_track(self, track_id, track):
        """
        Update a track.
        
        Args:
            track_id (int): The ID of the track
            track (Music): The updated track
            
        Returns:
            bool: True if the track was updated, False if not found
        """
        return self.__database.update_track(track_id, track)
    
    def delete_track(self, track_id):
        """
        Delete a track.
        
        Args:
            track_id (int): The ID of the track
            
        Returns:
            bool: True if the track was deleted, False if not found
        """
        return self.__database.delete_track(track_id)
    
    def get_tracks_by_genre(self, genre):
        """
        Get tracks by genre.
        
        Args:
            genre (str): The genre
            
        Returns:
            list: Tracks with the specified genre
        """
        return self.__database.filter_by_genre(genre)
    
    def get_available_genres(self):
        """
        Get all available genres.
        
        Returns:
            list: All available genres
        """
        from models.music import Genre
        return Genre.get_all_genres()