class UserDatabase:
    """
    A simple database for storing user accounts.
    In a real application, this would connect to an actual database.
    """
    
    def __init__(self):
        """Initialize the user database."""
        self.__users = {}  # Dictionary to store users by username
    
    def add_user(self, user):
        """
        Add a user to the database.
        
        Args:
            user (User): The user to add
            
        Returns:
            bool: True if the user was added, False if the username already exists
        """
        if user.username not in self.__users:
            self.__users[user.username] = user
            return True
        return False
    
    def get_user(self, username):
        """
        Get a user by username.
        
        Args:
            username (str): The username of the user
            
        Returns:
            User or None: The user, or None if not found
        """
        return self.__users.get(username)
    
    def update_user(self, username, user):
        """
        Update a user.
        
        Args:
            username (str): The username of the user
            user (User): The updated user
            
        Returns:
            bool: True if the user was updated, False if not found
        """
        if username in self.__users:
            self.__users[username] = user
            return True
        return False
    
    def delete_user(self, username):
        """
        Delete a user.
        
        Args:
            username (str): The username of the user
            
        Returns:
            bool: True if the user was deleted, False if not found
        """
        if username in self.__users:
            del self.__users[username]
            return True
        return False
    
    def get_all_users(self):
        """
        Get all users in the database.
        
        Returns:
            list: All users in the database
        """
        return list(self.__users.values())
    
    def authenticate_user(self, username, password):
        """
        Authenticate a user.
        
        Args:
            username (str): The username of the user
            password (str): The password of the user
            
        Returns:
            User or None: The authenticated user, or None if authentication failed
        """
        user = self.get_user(username)
        if user and user.verify_password(password):
            return user
        return None


class UserService:
    """
    Service for managing user operations.
    """
    
    def __init__(self):
        """Initialize the user service."""
        self.__database = UserDatabase()
        self.__current_user = None
        self.__initialize_sample_users()
    
    def __initialize_sample_users(self):
        """Add some sample users to the database."""
        from models.user import User
        
        # Add some sample users
        samples = [
            User("john_doe", "john@example.com", "password123"),
            User("jane_smith", "jane@example.com", "securepass"),
            User("music_lover", "music@example.com", "tunes4life")
        ]
        
        # Make one user premium
        samples[1].upgrade_to_premium()
        
        for user in samples:
            self.__database.add_user(user)
    
    @property
    def current_user(self):
        """Get the currently logged-in user."""
        return self.__current_user
    
    def register_user(self, username, email, password):
        """
        Register a new user.
        
        Args:
            username (str): The username of the user
            email (str): The email of the user
            password (str): The password of the user
            
        Returns:
            User or str: The registered user, or an error message
        """
        from models.user import User
        
        # Check if the username already exists
        if self.__database.get_user(username):
            return "⚠️ Username already exists!"
        
        # Create and add the user
        user = User(username, email, password)
        if self.__database.add_user(user):
            return user
        
        return "⚠️ Failed to register user!"
    
    def login(self, username, password):
        """
        Log a user in.
        
        Args:
            username (str): The username of the user
            password (str): The password of the user
            
        Returns:
            str: Message about the login
        """
        user = self.__database.authenticate_user(username, password)
        if user:
            self.__current_user = user
            return user.login()
        
        return "⚠️ Invalid username or password!"
    
    def logout(self):
        """
        Log the current user out.
        
        Returns:
            str: Message about the logout
        """
        if self.__current_user:
            message = self.__current_user.logout()
            self.__current_user = None
            return message
        
        return "⚠️ No user is currently logged in!"
    
    def upgrade_user_to_premium(self):
        """
        Upgrade the current user to premium.
        
        Returns:
            str: Message about the upgrade
        """
        if not self.__current_user:
            return "⚠️ No user is currently logged in!"
        
        return self.__current_user.upgrade_to_premium()
    
    def downgrade_user_to_free(self):
        """
        Downgrade the current user to free.
        
        Returns:
            str: Message about the downgrade
        """
        if not self.__current_user:
            return "⚠️ No user is currently logged in!"
        
        return self.__current_user.downgrade_to_free()
    
    def change_password(self, old_password, new_password):
        """
        Change the current user's password.
        
        Args:
            old_password (str): The old password
            new_password (str): The new password
            
        Returns:
            str: Message about the password change
        """
        if not self.__current_user:
            return "⚠️ No user is currently logged in!"
        
        if self.__current_user.change_password(old_password, new_password):
            return "✅ Password changed successfully!"
        
        return "⚠️ Incorrect old password!"
    
    def create_playlist(self, name, description=None):
        """
        Create a playlist for the current user.
        
        Args:
            name (str): The name of the playlist
            description (str, optional): A description of the playlist
            
        Returns:
            Playlist or str: The created playlist, or an error message
        """
        if not self.__current_user:
            return "⚠️ No user is currently logged in!"
        
        return self.__current_user.create_playlist(name, description)
    
    def get_user_profile(self):
        """
        Get the current user's profile information.
        
        Returns:
            str: The user's profile information, or an error message
        """
        if not self.__current_user:
            return "⚠️ No user is currently logged in!"
        
        return self.__current_user.get_profile_info()
    
    def get_user_playlists(self):
        """
        Get all playlists created by the current user.
        
        Returns:
            list or str: The user's playlists, or an error message
        """
        if not self.__current_user:
            return "⚠️ No user is currently logged in!"
        
        return self.__current_user.playlists
    
    def like_track(self, track):
        """
        Like a track for the current user.
        
        Args:
            track (Music): The track to like
            
        Returns:
            str: Message about the like
        """
        if not self.__current_user:
            return "⚠️ No user is currently logged in!"
        
        if self.__current_user.like_track(track):
            return f"❤️ You liked '{track.title}' by {track.artist}"
        
        return f"⚠️ You already liked '{track.title}' by {track.artist}"
    
    def unlike_track(self, track):
        """
        Unlike a track for the current user.
        
        Args:
            track (Music): The track to unlike
            
        Returns:
            str: Message about the unlike
        """
        if not self.__current_user:
            return "⚠️ No user is currently logged in!"
        
        if self.__current_user.unlike_track(track):
            return f"💔 You unliked '{track.title}' by {track.artist}"
        
        return f"⚠️ You haven't liked '{track.title}' by {track.artist}"
    
    def get_liked_tracks(self):
        """
        Get all tracks liked by the current user.
        
        Returns:
            list or str: The user's liked tracks, or an error message
        """
        if not self.__current_user:
            return "⚠️ No user is currently logged in!"
        
        return self.__current_user.liked_tracks