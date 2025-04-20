from abc import ABC, abstractmethod

class Description:
    """A class for handling descriptions of media items."""
    
    def __init__(self, description):
        """
        Initialize a Description object.
        
        Args:
            description (str): The description text
        """
        self.__description = description
    
    def get_description(self):
        """
        Get the description text.
        
        Returns:
            str: The description text
        """
        return self.__description
    
    def set_description(self, description):
        """
        Update the description text.
        
        Args:
            description (str): The new description text
        """
        self.__description = description


class Media(ABC):
    """
    Abstract base class for all media types.
    ABC ensures this class cannot be instantiated directly.
    """
    
    def __init__(self, title, duration, release_date=None):
        """
        Initialize a Media object.
        
        Args:
            title (str): The title of the media
            duration (float): The duration in minutes
            release_date (str, optional): Release date in YYYY-MM-DD format
        """
        self.__title = title
        self.__duration = duration
        self.__release_date = release_date
        # Track if media is currently playing
        self.__is_playing = False
    
    @property
    def title(self):
        """Get the title of the media."""
        return self.__title
    
    @property
    def duration(self):
        """Get the duration of the media in minutes."""
        return self.__duration
    
    @property
    def release_date(self):
        """Get the release date of the media."""
        return self.__release_date
    
    @property
    def is_playing(self):
        """Check if the media is currently playing."""
        return self.__is_playing
    
    @is_playing.setter
    def is_playing(self, value):
        """Set the playing status of the media."""
        self.__is_playing = value
    
    @abstractmethod
    def play(self):
        """
        Play the media. This method must be implemented by subclasses.
        """
        pass
    
    @abstractmethod
    def stop(self):
        """
        Stop playing the media. This method must be implemented by subclasses.
        """
        pass
    
    def get_info(self):
        """
        Get basic information about the media.
        
        Returns:
            str: Formatted information string
        """
        info = f"Title: {self.__title}, Duration: {self.__duration} minutes"
        if self.__release_date:
            info += f", Released: {self.__release_date}"
        return info