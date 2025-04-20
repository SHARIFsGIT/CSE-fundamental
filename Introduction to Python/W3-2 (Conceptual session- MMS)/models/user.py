class Subscription:
    """Class to represent subscription types and features."""
    
    # Subscription types
    FREE = "Free"
    PREMIUM = "Premium"
    
    # Features and limits by subscription type
    FEATURES = {
        FREE: {
            "max_playlists": 3,
            "max_tracks_per_playlist": 50,
            "offline_listening": False,
            "ads": True,
            "high_quality": False,
            "can_download": False,
            "price": 0.00
        },
        PREMIUM: {
            "max_playlists": float('inf'),  # Unlimited
            "max_tracks_per_playlist": float('inf'),  # Unlimited
            "offline_listening": True,
            "ads": False,
            "high_quality": True,
            "can_download": True,
            "price": 9.99
        }
    }
    
    @classmethod
    def get_features(cls, subscription_type):
        """
        Get the features for a subscription type.
        
        Args:
            subscription_type (str): The subscription type (FREE or PREMIUM)
            
        Returns:
            dict: The features for the subscription type
        """
        return cls.FEATURES.get(subscription_type, cls.FEATURES[cls.FREE])


class User:
    """
    Class representing a user of the music system.
    """
    
    def __init__(self, username, email, password):
        """
        Initialize a User object.
        
        Args:
            username (str): The user's username
            email (str): The user's email
            password (str): The user's password (should be hashed in a real system)
        """
        self.__username = username
        self.__email = email
        self.__password = password  # In a real system, this would be hashed
        self.__subscription_type = Subscription.FREE
        self.__playlists = []
        self.__liked_tracks = []
        self.__is_online = False
    
    @property
    def username(self):
        """Get the username."""
        return self.__username
    
    @property
    def email(self):
        """Get the email."""
        return self.__email
    
    @email.setter
    def email(self, email):
        """Set the email."""
        self.__email = email
    
    @property
    def subscription_type(self):
        """Get the subscription type."""
        return self.__subscription_type
    
    @property
    def is_premium(self):
        """Check if the user has a premium subscription."""
        return self.__subscription_type == Subscription.PREMIUM
    
    @property
    def playlists(self):
        """Get all playlists created by the user."""
        return self.__playlists.copy()
    
    @property
    def liked_tracks(self):
        """Get all tracks liked by the user."""
        return self.__liked_tracks.copy()
    
    @property
    def is_online(self):
        """Check if the user is currently online."""
        return self.__is_online
    
    def upgrade_to_premium(self):
        """
        Upgrade the user to a premium subscription.
        
        Returns:
            str: Message about the upgrade
        """
        if self.__subscription_type == Subscription.PREMIUM:
            return "⚠️ You already have a Premium subscription!"
        
        self.__subscription_type = Subscription.PREMIUM
        return "🌟 Successfully upgraded to Premium subscription!"
    
    def downgrade_to_free(self):
        """
        Downgrade the user to a free subscription.
        
        Returns:
            str: Message about the downgrade
        """
        if self.__subscription_type == Subscription.FREE:
            return "⚠️ You already have a Free subscription!"
        
        self.__subscription_type = Subscription.FREE
        return "Successfully downgraded to Free subscription."
    
    def verify_password(self, password):
        """
        Verify the user's password.
        
        Args:
            password (str): The password to verify
            
        Returns:
            bool: True if the password is correct, False otherwise
        """
        # In a real system, this would compare hashed passwords
        return password == self.__password
    
    def change_password(self, old_password, new_password):
        """
        Change the user's password.
        
        Args:
            old_password (str): The old password
            new_password (str): The new password
            
        Returns:
            bool: True if the password was changed, False otherwise
        """
        if self.verify_password(old_password):
            self.__password = new_password  # In a real system, this would be hashed
            return True
        return False
    
    def create_playlist(self, name, description=None):
        """
        Create a new playlist.
        
        Args:
            name (str): The name of the playlist
            description (str, optional): A description of the playlist
            
        Returns:
            Playlist or str: The created playlist, or an error message
        """
        from models.playlist import Playlist
        
        # Check if the user has reached their playlist limit
        features = Subscription.get_features(self.__subscription_type)
        if len(self.__playlists) >= features["max_playlists"]:
            return f"⚠️ You have reached your playlist limit ({features['max_playlists']})!"
        
        playlist = Playlist(name, self, description)
        self.__playlists.append(playlist)
        return playlist
    
    def delete_playlist(self, playlist):
        """
        Delete a playlist.
        
        Args:
            playlist (Playlist): The playlist to delete
            
        Returns:
            bool: True if the playlist was deleted, False otherwise
        """
        if playlist in self.__playlists:
            self.__playlists.remove(playlist)
            return True
        return False
    
    def like_track(self, track):
        """
        Like a track.
        
        Args:
            track (Music): The track to like
            
        Returns:
            bool: True if the track was liked, False if it was already liked
        """
        if track not in self.__liked_tracks:
            self.__liked_tracks.append(track)
            track.add_like()
            return True
        return False
    
    def unlike_track(self, track):
        """
        Unlike a track.
        
        Args:
            track (Music): The track to unlike
            
        Returns:
            bool: True if the track was unliked, False if it wasn't liked
        """
        if track in self.__liked_tracks:
            self.__liked_tracks.remove(track)
            track.remove_like()
            return True
        return False
    
    def login(self):
        """
        Log the user in.
        
        Returns:
            str: Message about the login
        """
        self.__is_online = True
        return f"👋 Welcome back, {self.__username}!"
    
    def logout(self):
        """
        Log the user out.
        
        Returns:
            str: Message about the logout
        """
        self.__is_online = False
        return f"👋 Goodbye, {self.__username}!"
    
    def get_subscription_features(self):
        """
        Get the features of the user's subscription.
        
        Returns:
            dict: The features of the user's subscription
        """
        return Subscription.get_features(self.__subscription_type)
    
    def get_profile_info(self):
        """
        Get information about the user's profile.
        
        Returns:
            str: Formatted information string
        """
        features = self.get_subscription_features()
        
        info = f"--- User Profile: {self.__username} ---\n"
        info += f"Email: {self.__email}\n"
        info += f"Subscription: {self.__subscription_type}"
        if self.__subscription_type == Subscription.PREMIUM:
            info += " 🌟"
        info += "\n"
        
        info += f"Playlists: {len(self.__playlists)}/{features['max_playlists'] if features['max_playlists'] != float('inf') else 'Unlimited'}\n"
        info += f"Liked Tracks: {len(self.__liked_tracks)}\n"
        
        info += "\nSubscription Features:\n"
        info += f"- {'✅' if features['offline_listening'] else '❌'} Offline Listening\n"
        info += f"- {'❌' if features['ads'] else '✅'} Ad-free Experience\n"
        info += f"- {'✅' if features['high_quality'] else '❌'} High Quality Audio\n"
        info += f"- {'✅' if features['can_download'] else '❌'} Download Tracks\n"
        
        return info