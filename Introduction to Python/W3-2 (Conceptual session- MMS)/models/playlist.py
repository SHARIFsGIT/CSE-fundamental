from datetime import datetime

class Playlist:
    """
    Class representing a collection of music tracks.
    """
    
    def __init__(self, name, creator, description=None):
        """
        Initialize a Playlist object.
        
        Args:
            name (str): The name of the playlist
            creator (User): The user who created the playlist
            description (str, optional): A description of the playlist
        """
        self.__name = name
        self.__creator = creator
        self.__description = description
        self.__tracks = []
        self.__created_at = datetime.now()
        self.__is_private = False
        self.__current_track_index = -1  # No track selected initially
    
    @property
    def name(self):
        """Get the playlist name."""
        return self.__name
    
    @name.setter
    def name(self, name):
        """Set the playlist name."""
        self.__name = name
    
    @property
    def description(self):
        """Get the playlist description."""
        return self.__description
    
    @description.setter
    def description(self, description):
        """Set the playlist description."""
        self.__description = description
    
    @property
    def creator(self):
        """Get the creator of the playlist."""
        return self.__creator
    
    @property
    def tracks(self):
        """Get all tracks in the playlist."""
        return self.__tracks.copy()
    
    @property
    def created_at(self):
        """Get the creation date of the playlist."""
        return self.__created_at
    
    @property
    def is_private(self):
        """Check if the playlist is private."""
        return self.__is_private
    
    @is_private.setter
    def is_private(self, value):
        """Set the privacy status of the playlist."""
        self.__is_private = value
    
    @property
    def total_duration(self):
        """Calculate the total duration of the playlist."""
        return sum(track.duration for track in self.__tracks)
    
    def add_track(self, track):
        """
        Add a track to the playlist.
        
        Args:
            track (Music): The track to add
            
        Returns:
            bool: True if the track was added, False if it already exists
        """
        if track not in self.__tracks:
            self.__tracks.append(track)
            return True
        return False
    
    def remove_track(self, track):
        """
        Remove a track from the playlist.
        
        Args:
            track (Music): The track to remove
            
        Returns:
            bool: True if the track was removed, False if it wasn't in the playlist
        """
        if track in self.__tracks:
            self.__tracks.remove(track)
            # Adjust current track index if needed
            if self.__current_track_index >= len(self.__tracks):
                self.__current_track_index = len(self.__tracks) - 1
            return True
        return False
    
    def clear(self):
        """Remove all tracks from the playlist."""
        self.__tracks = []
        self.__current_track_index = -1
    
    def play(self):
        """
        Start playing the playlist from the beginning.
        
        Returns:
            str: Message about what's playing
        """
        if not self.__tracks:
            return "⚠️ Playlist is empty!"
        
        # Stop any currently playing track
        self.__stop_current_track()
        
        # Start from the beginning
        self.__current_track_index = 0
        current_track = self.__tracks[self.__current_track_index]
        
        return f"▶️ Playing playlist: {self.__name}\n{current_track.play()}"
    
    def __stop_current_track(self):
        """Helper method to stop the current track if one is playing."""
        if 0 <= self.__current_track_index < len(self.__tracks):
            current_track = self.__tracks[self.__current_track_index]
            if current_track.is_playing:
                current_track.stop()
    
    def next_track(self):
        """
        Play the next track in the playlist.
        
        Returns:
            str: Message about what's playing
        """
        if not self.__tracks:
            return "⚠️ Playlist is empty!"
        
        self.__stop_current_track()
        
        # Move to the next track or wrap around to the beginning
        self.__current_track_index = (self.__current_track_index + 1) % len(self.__tracks)
        current_track = self.__tracks[self.__current_track_index]
        
        return f"⏭️ Next track: {current_track.play()}"
    
    def previous_track(self):
        """
        Play the previous track in the playlist.
        
        Returns:
            str: Message about what's playing
        """
        if not self.__tracks:
            return "⚠️ Playlist is empty!"
        
        self.__stop_current_track()
        
        # Move to the previous track or wrap around to the end
        self.__current_track_index = (self.__current_track_index - 1) % len(self.__tracks)
        current_track = self.__tracks[self.__current_track_index]
        
        return f"⏮️ Previous track: {current_track.play()}"
    
    def stop(self):
        """
        Stop the currently playing track.
        
        Returns:
            str: Message about stopping
        """
        if not self.__tracks:
            return "⚠️ Playlist is empty!"
        
        if 0 <= self.__current_track_index < len(self.__tracks):
            current_track = self.__tracks[self.__current_track_index]
            return current_track.stop()
        else:
            return "⚠️ No track is currently selected!"
    
    def shuffle(self):
        """
        Shuffle the tracks in the playlist.
        
        Returns:
            str: Message about shuffling
        """
        import random
        
        if not self.__tracks:
            return "⚠️ Playlist is empty!"
        
        # Stop any currently playing track
        self.__stop_current_track()
        
        # Shuffle the tracks
        random.shuffle(self.__tracks)
        self.__current_track_index = -1  # Reset the current track
        
        return f"🔀 Playlist '{self.__name}' has been shuffled!"
    
    def get_info(self):
        """
        Get information about the playlist.
        
        Returns:
            str: Formatted information string
        """
        privacy = "Private" if self.__is_private else "Public"
        created_date = self.__created_at.strftime("%Y-%m-%d")
        
        info = f"Playlist: {self.__name} ({privacy})\n"
        info += f"Created by: {self.__creator.username} on {created_date}\n"
        if self.__description:
            info += f"Description: {self.__description}\n"
        
        info += f"Tracks: {len(self.__tracks)}\n"
        info += f"Total Duration: {self.total_duration:.2f} minutes\n"
        
        return info
    
    def list_tracks(self):
        """
        List all tracks in the playlist.
        
        Returns:
            str: Formatted list of tracks
        """
        if not self.__tracks:
            return "Playlist is empty!"
        
        track_list = "Tracks in playlist:\n"
        for i, track in enumerate(self.__tracks, 1):
            # Add a "▶️" indicator for the currently playing track
            playing = "▶️ " if (i-1) == self.__current_track_index and track.is_playing else "  "
            track_list += f"{playing}{i}. {track.title} by {track.artist} ({track.duration:.2f} min)\n"
        
        return track_list