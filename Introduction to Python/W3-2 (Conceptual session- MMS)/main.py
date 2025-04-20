import os
import sys
import time
from models.music import Music, Genre
from models.playlist import Playlist
from services.music_service import MusicService
from services.user_service import UserService

class MusicApp:
    """
    Main class for the music management application.
    Handles user interaction and ties all components together.
    """
    
    def __init__(self):
        """Initialize the music application."""
        self.__music_service = MusicService()
        self.__user_service = UserService()
        self.__current_playlist = None
    
    def clear_screen(self):
        """Clear the console screen."""
        # Check operating system and use appropriate command
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self, title, options, show_back=True):
        """
        Display a menu with options.
        
        Args:
            title (str): The title of the menu
            options (list): List of option text strings
            show_back (bool): Whether to show a "Back" option
            
        Returns:
            int: The selected option index (0-based)
        """
        self.clear_screen()
        print(f"\n===== {title} =====")
        
        # Print options
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        # Add Back option if requested
        if show_back:
            print(f"{len(options) + 1}. Back")
        
        # Get user choice
        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                if 1 <= choice <= len(options) + (1 if show_back else 0):
                    # Return 0-based index
                    return choice - 1
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
    
    def display_login_menu(self):
        """Display the login menu and handle user selection."""
        options = ["Login", "Register", "Exit"]
        choice = self.display_menu("MUSIC MANAGEMENT SYSTEM", options, show_back=False)
        
        if choice == 0:  # Login
            self.login()
        elif choice == 1:  # Register
            self.register()
        elif choice == 2:  # Exit
            print("\nThank you for using the Music Management System. Goodbye!")
            sys.exit(0)
    
    def login(self):
        """Handle user login."""
        self.clear_screen()
        print("\n===== LOGIN =====")
        
        username = input("Username: ")
        password = input("Password: ")
        
        result = self.__user_service.login(username, password)
        print(f"\n{result}")
        
        if "Invalid" not in result:  # Successful login
            time.sleep(1.5)
            self.display_main_menu()
        else:
            time.sleep(1.5)
            self.display_login_menu()
    
    def register(self):
        """Handle user registration."""
        self.clear_screen()
        print("\n===== REGISTER =====")
        
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        
        result = self.__user_service.register_user(username, email, password)
        
        if isinstance(result, str):  # Error message
            print(f"\n{result}")
            time.sleep(1.5)
            self.display_login_menu()
        else:
            print("\n✅ Registration successful! You can now log in.")
            time.sleep(1.5)
            self.display_login_menu()
    
    def display_main_menu(self):
        """Display the main menu and handle user selection."""
        options = [
            "Browse Music",
            "Search Music",
            "Manage Playlists",
            "Liked Tracks",
            "Account Settings",
            "Logout"
        ]
        
        choice = self.display_menu("MAIN MENU", options, show_back=False)
        
        if choice == 0:  # Browse Music
            self.browse_music()
        elif choice == 1:  # Search Music
            self.search_music()
        elif choice == 2:  # Manage Playlists
            self.manage_playlists()
        elif choice == 3:  # Liked Tracks
            self.view_liked_tracks()
        elif choice == 4:  # Account Settings
            self.account_settings()
        elif choice == 5:  # Logout
            result = self.__user_service.logout()
            print(f"\n{result}")
            time.sleep(1.5)
            self.display_login_menu()
    
    def browse_music(self):
        """Browse music tracks."""
        options = [
            "View All Tracks",
            "Browse by Genre"
        ]
        
        choice = self.display_menu("BROWSE MUSIC", options)
        
        if choice == 0:  # View All Tracks
            self.view_all_tracks()
        elif choice == 1:  # Browse by Genre
            self.browse_by_genre()
        else:  # Selected Back
            self.display_main_menu()
    
    def view_all_tracks(self):
        """View all music tracks."""
        tracks = self.__music_service.get_all_tracks()
        
        # Create a list of track display strings
        track_options = [f"{track.title} by {track.artist}" for track in tracks]
        
        choice = self.display_menu("ALL TRACKS", track_options)
        
        if choice < len(track_options):  # Selected a track
            selected_track = tracks[choice]
            self.display_track_options(selected_track)
        else:  # Selected Back
            self.browse_music()
    
    def browse_by_genre(self):
        """Browse music tracks by genre."""
        genres = self.__music_service.get_available_genres()
        
        choice = self.display_menu("BROWSE BY GENRE", genres)
        
        if choice < len(genres):  # Selected a genre
            selected_genre = genres[choice]
            tracks = self.__music_service.get_tracks_by_genre(selected_genre)
            
            if not tracks:
                print(f"\nNo tracks found for genre: {selected_genre}")
                time.sleep(1.5)
                self.browse_music()
                return
            
            # Create a list of track display strings
            track_options = [f"{track.title} by {track.artist}" for track in tracks]
            
            track_choice = self.display_menu(f"GENRE: {selected_genre}", track_options)
            
            if track_choice < len(track_options):  # Selected a track
                selected_track = tracks[track_choice]
                self.display_track_options(selected_track)
            else:  # Selected Back
                self.browse_music()
        else:  # Selected Back
            self.browse_music()
    
    def search_music(self):
        """Search for music tracks."""
        self.clear_screen()
        print("\n===== SEARCH MUSIC =====")
        
        query = input("Enter search term: ")
        
        if not query.strip():
            print("\n⚠️ Search term cannot be empty.")
            time.sleep(1.5)
            self.display_main_menu()
            return
        
        tracks = self.__music_service.search_tracks(query)
        
        if not tracks:
            print(f"\nNo tracks found for: {query}")
            time.sleep(1.5)
            self.display_main_menu()
            return
        
        # Create a list of track display strings
        track_options = [f"{track.title} by {track.artist}" for track in tracks]
        
        choice = self.display_menu(f"SEARCH RESULTS FOR: {query}", track_options)
        
        if choice < len(track_options):  # Selected a track
            selected_track = tracks[choice]
            self.display_track_options(selected_track)
        else:  # Selected Back
            self.display_main_menu()
    
    def display_track_options(self, track):
        """
        Display options for a selected track.
        
        Args:
            track (Music): The selected track
        """
        options = ["Play", "View Details", "Add to Playlist", "Like/Unlike"]
        
        choice = self.display_menu(f"TRACK: {track.title}", options)
        
        if choice == 0:  # Play
            result = track.play()
            print(f"\n{result}")
            input("\nPress Enter to stop playing...")
            track.stop()
            self.display_track_options(track)
        elif choice == 1:  # View Details
            self.view_track_details(track)
        elif choice == 2:  # Add to Playlist
            self.add_to_playlist(track)
        elif choice == 3:  # Like/Unlike
            if track in self.__user_service.get_liked_tracks():
                result = self.__user_service.unlike_track(track)
            else:
                result = self.__user_service.like_track(track)
            print(f"\n{result}")
            time.sleep(1.5)
            self.display_track_options(track)
        else:  # Selected Back
            self.browse_music()
    
    def view_track_details(self, track):
        """
        View detailed information about a track.
        
        Args:
            track (Music): The track to view
        """
        self.clear_screen()
        print(f"\n===== TRACK DETAILS =====")
        print(track.get_full_info())
        
        input("\nPress Enter to go back...")
        self.display_track_options(track)
    
    def view_liked_tracks(self):
        """View tracks liked by the current user."""
        tracks = self.__user_service.get_liked_tracks()
        
        if isinstance(tracks, str):  # Error message
            print(f"\n{tracks}")
            time.sleep(1.5)
            self.display_main_menu()
            return
        
        if not tracks:
            print("\n⚠️ You haven't liked any tracks yet!")
            time.sleep(1.5)
            self.display_main_menu()
            return
        
        # Create a list of track display strings
        track_options = [f"{track.title} by {track.artist}" for track in tracks]
        
        choice = self.display_menu("LIKED TRACKS", track_options)
        
        if choice < len(track_options):  # Selected a track
            selected_track = tracks[choice]
            self.display_track_options(selected_track)
        else:  # Selected Back
            self.display_main_menu()
    
    def manage_playlists(self):
        """Manage user playlists."""
        playlists = self.__user_service.get_user_playlists()
        
        if isinstance(playlists, str):  # Error message
            print(f"\n{playlists}")
            time.sleep(1.5)
            self.display_main_menu()
            return
        
        # Create options list
        options = ["Create New Playlist"]
        if playlists:
            options.extend([playlist.name for playlist in playlists])
        
        choice = self.display_menu("MANAGE PLAYLISTS", options)
        
        if choice == 0:  # Create New Playlist
            self.create_playlist()
        elif choice < len(options):  # Selected a playlist
            selected_playlist = playlists[choice - 1]  # Adjust for "Create New Playlist" option
            self.__current_playlist = selected_playlist
            self.display_playlist_options(selected_playlist)
        else:  # Selected Back
            self.display_main_menu()
    
    def create_playlist(self):
        """Create a new playlist."""
        self.clear_screen()
        print("\n===== CREATE PLAYLIST =====")
        
        name = input("Playlist Name: ")
        description = input("Description (optional): ")
        
        if not name.strip():
            print("\n⚠️ Playlist name cannot be empty.")
            time.sleep(1.5)
            self.manage_playlists()
            return
        
        result = self.__user_service.create_playlist(name, description if description.strip() else None)
        
        if isinstance(result, str):  # Error message
            print(f"\n{result}")
        else:
            print(f"\n✅ Playlist '{name}' created successfully!")
            self.__current_playlist = result
        
        time.sleep(1.5)
        self.manage_playlists()
    
    def display_playlist_options(self, playlist):
        """
        Display options for a selected playlist.
        
        Args:
            playlist (Playlist): The selected playlist
        """
        options = [
            "View Tracks",
            "Add Tracks",
            "Remove Tracks",
            "Play Playlist",
            "View Details",
            "Toggle Privacy",
            "Edit Name/Description",
            "Delete Playlist"
        ]
        
        choice = self.display_menu(f"PLAYLIST: {playlist.name}", options)
        
        if choice == 0:  # View Tracks
            self.view_playlist_tracks(playlist)
        elif choice == 1:  # Add Tracks
            self.add_tracks_to_playlist(playlist)
        elif choice == 2:  # Remove Tracks
            self.remove_tracks_from_playlist(playlist)
        elif choice == 3:  # Play Playlist
            self.play_playlist(playlist)
        elif choice == 4:  # View Details
            self.view_playlist_details(playlist)
        elif choice == 5:  # Toggle Privacy
            playlist.is_private = not playlist.is_private
            status = "private" if playlist.is_private else "public"
            print(f"\n✅ Playlist is now {status}.")
            time.sleep(1.5)
            self.display_playlist_options(playlist)
        elif choice == 6:  # Edit Name/Description
            self.edit_playlist(playlist)
        elif choice == 7:  # Delete Playlist
            self.delete_playlist(playlist)
        else:  # Selected Back
            self.manage_playlists()
    
    def view_playlist_tracks(self, playlist):
        """
        View tracks in a playlist.
        
        Args:
            playlist (Playlist): The playlist to view
        """
        self.clear_screen()
        print(f"\n===== TRACKS IN PLAYLIST: {playlist.name} =====")
        print(playlist.list_tracks())
        
        input("\nPress Enter to go back...")
        self.display_playlist_options(playlist)
    
    def add_tracks_to_playlist(self, playlist):
        """
        Add tracks to a playlist.
        
        Args:
            playlist (Playlist): The playlist to add tracks to
        """
        tracks = self.__music_service.get_all_tracks()
        
        # Create a list of track display strings
        track_options = [f"{track.title} by {track.artist}" for track in tracks]
        
        choice = self.display_menu("SELECT TRACK TO ADD", track_options)
        
        if choice < len(track_options):  # Selected a track
            selected_track = tracks[choice]
            
            if playlist.add_track(selected_track):
                print(f"\n✅ Added '{selected_track.title}' to playlist.")
            else:
                print(f"\n⚠️ '{selected_track.title}' is already in the playlist.")
            
            time.sleep(1.5)
            self.add_tracks_to_playlist(playlist)  # Allow adding more tracks
        else:  # Selected Back
            self.display_playlist_options(playlist)
    
    def remove_tracks_from_playlist(self, playlist):
        """
        Remove tracks from a playlist.
        
        Args:
            playlist (Playlist): The playlist to remove tracks from
        """
        tracks = playlist.tracks
        
        if not tracks:
            print("\n⚠️ Playlist is empty!")
            time.sleep(1.5)
            self.display_playlist_options(playlist)
            return
        
        # Create a list of track display strings
        track_options = [f"{track.title} by {track.artist}" for track in tracks]
        
        choice = self.display_menu("SELECT TRACK TO REMOVE", track_options)
        
        if choice < len(track_options):  # Selected a track
            selected_track = tracks[choice]
            
            if playlist.remove_track(selected_track):
                print(f"\n✅ Removed '{selected_track.title}' from playlist.")
            else:
                print(f"\n⚠️ Failed to remove track.")
            
            time.sleep(1.5)
            
            if playlist.tracks:  # If there are still tracks in the playlist
                self.remove_tracks_from_playlist(playlist)  # Allow removing more tracks
            else:
                self.display_playlist_options(playlist)
        else:  # Selected Back
            self.display_playlist_options(playlist)
    
    def play_playlist(self, playlist):
        """
        Play a playlist.
        
        Args:
            playlist (Playlist): The playlist to play
        """
        if not playlist.tracks:
            print("\n⚠️ Playlist is empty!")
            time.sleep(1.5)
            self.display_playlist_options(playlist)
            return
        
        # Start playing the playlist
        result = playlist.play()
        print(f"\n{result}")
        
        # Player controls loop
        while True:
            print("\nPlayer Controls:")
            print("1. Next Track")
            print("2. Previous Track")
            print("3. Stop")
            print("4. Shuffle")
            print("5. Back to Playlist")
            
            try:
                choice = int(input("\nEnter your choice: "))
                
                if choice == 1:  # Next Track
                    result = playlist.next_track()
                    print(f"\n{result}")
                elif choice == 2:  # Previous Track
                    result = playlist.previous_track()
                    print(f"\n{result}")
                elif choice == 3:  # Stop
                    result = playlist.stop()
                    print(f"\n{result}")
                    time.sleep(1.5)
                    break
                elif choice == 4:  # Shuffle
                    result = playlist.shuffle()
                    print(f"\n{result}")
                elif choice == 5:  # Back to Playlist
                    playlist.stop()
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
        
        self.display_playlist_options(playlist)
    
    def view_playlist_details(self, playlist):
        """
        View detailed information about a playlist.
        
        Args:
            playlist (Playlist): The playlist to view
        """
        self.clear_screen()
        print(f"\n===== PLAYLIST DETAILS =====")
        print(playlist.get_info())
        
        input("\nPress Enter to go back...")
        self.display_playlist_options(playlist)
    
    def edit_playlist(self, playlist):
        """
        Edit a playlist's name and description.
        
        Args:
            playlist (Playlist): The playlist to edit
        """
        self.clear_screen()
        print(f"\n===== EDIT PLAYLIST =====")
        print(f"Current Name: {playlist.name}")
        print(f"Current Description: {playlist.description or 'None'}")
        
        name = input("\nNew Name (leave empty to keep current): ")
        description = input("New Description (leave empty to keep current): ")
        
        if name.strip():
            playlist.name = name
        
        if description.strip():
            playlist.description = description
        
        print("\n✅ Playlist updated successfully!")
        time.sleep(1.5)
        self.display_playlist_options(playlist)
    
    def delete_playlist(self, playlist):
        """
        Delete a playlist.
        
        Args:
            playlist (Playlist): The playlist to delete
        """
        self.clear_screen()
        print(f"\n===== DELETE PLAYLIST =====")
        print(f"Are you sure you want to delete playlist '{playlist.name}'?")
        print("This action cannot be undone.")
        
        confirmation = input("\nType 'yes' to confirm: ")
        
        if confirmation.lower() == "yes":
            if self.__user_service.current_user.delete_playlist(playlist):
                print(f"\n✅ Playlist '{playlist.name}' deleted successfully!")
                self.__current_playlist = None
                time.sleep(1.5)
                self.manage_playlists()
            else:
                print("\n⚠️ Failed to delete playlist.")
                time.sleep(1.5)
                self.display_playlist_options(playlist)
        else:
            print("\nPlaylist deletion cancelled.")
            time.sleep(1.5)
            self.display_playlist_options(playlist)
    
    def add_to_playlist(self, track):
        """
        Add a track to a playlist.
        
        Args:
            track (Music): The track to add
        """
        playlists = self.__user_service.get_user_playlists()
        
        if isinstance(playlists, str):  # Error message
            print(f"\n{playlists}")
            time.sleep(1.5)
            self.display_track_options(track)
            return
        
        if not playlists:
            print("\n⚠️ You don't have any playlists. Create one first.")
            time.sleep(1.5)
            self.display_track_options(track)
            return
        
        # Create a list of playlist display strings
        playlist_options = [playlist.name for playlist in playlists]
        
        choice = self.display_menu("SELECT PLAYLIST", playlist_options)
        
        if choice < len(playlist_options):  # Selected a playlist
            selected_playlist = playlists[choice]
            
            if selected_playlist.add_track(track):
                print(f"\n✅ Added '{track.title}' to playlist '{selected_playlist.name}'.")
            else:
                print(f"\n⚠️ '{track.title}' is already in the playlist.")
            
            time.sleep(1.5)
            self.display_track_options(track)
        else:  # Selected Back
            self.display_track_options(track)
    
    def account_settings(self):
        """Display and manage account settings."""
        options = [
            "View Profile",
            "Change Password",
            "Manage Subscription"
        ]
        
        choice = self.display_menu("ACCOUNT SETTINGS", options)
        
        if choice == 0:  # View Profile
            self.view_profile()
        elif choice == 1:  # Change Password
            self.change_password()
        elif choice == 2:  # Manage Subscription
            self.manage_subscription()
        else:  # Selected Back
            self.display_main_menu()
    
    def view_profile(self):
        """View the current user's profile."""
        self.clear_screen()
        print("\n===== USER PROFILE =====")
        print(self.__user_service.get_user_profile())
        
        input("\nPress Enter to go back...")
        self.account_settings()
    
    def change_password(self):
        """Change the current user's password."""
        self.clear_screen()
        print("\n===== CHANGE PASSWORD =====")
        
        old_password = input("Current Password: ")
        new_password = input("New Password: ")
        confirm_password = input("Confirm New Password: ")
        
        if not new_password.strip():
            print("\n⚠️ Password cannot be empty.")
            time.sleep(1.5)
            self.account_settings()
            return
        
        if new_password != confirm_password:
            print("\n⚠️ New passwords do not match.")
            time.sleep(1.5)
            self.account_settings()
            return
        
        result = self.__user_service.change_password(old_password, new_password)
        print(f"\n{result}")
        
        time.sleep(1.5)
        self.account_settings()
    
    def manage_subscription(self):
        """Manage the current user's subscription."""
        user = self.__user_service.current_user
        
        if user.is_premium:
            options = ["Downgrade to Free"]
        else:
            options = ["Upgrade to Premium"]
        
        options.append("View Subscription Details")
        
        choice = self.display_menu("MANAGE SUBSCRIPTION", options)
        
        if choice == 0:  # Upgrade/Downgrade
            if user.is_premium:
                result = self.__user_service.downgrade_user_to_free()
            else:
                result = self.__user_service.upgrade_user_to_premium()
            
            print(f"\n{result}")
            time.sleep(1.5)
            self.manage_subscription()
        elif choice == 1:  # View Subscription Details
            self.view_subscription_details()
        else:  # Selected Back
            self.account_settings()
    
    def view_subscription_details(self):
        """View details of the current subscription."""
        user = self.__user_service.current_user
        features = user.get_subscription_features()
        
        self.clear_screen()
        print(f"\n===== SUBSCRIPTION DETAILS: {user.subscription_type} =====")
        
        if user.is_premium:
            print("\n🌟 You are currently on a Premium subscription.")
            print(f"Price: ${features['price']:.2f}/month")
        else:
            print("\nYou are currently on a Free subscription.")
            print(f"Premium Price: ${features['price']}/month")
        
        print("\nFeatures:")
        print(f"- Playlists: {features['max_playlists'] if features['max_playlists'] != float('inf') else 'Unlimited'}")
        print(f"- Tracks per Playlist: {features['max_tracks_per_playlist'] if features['max_tracks_per_playlist'] != float('inf') else 'Unlimited'}")
        print(f"- {'✅' if features['offline_listening'] else '❌'} Offline Listening")
        print(f"- {'❌' if features['ads'] else '✅'} Ad-free Experience")
        print(f"- {'✅' if features['high_quality'] else '❌'} High Quality Audio")
        print(f"- {'✅' if features['can_download'] else '❌'} Download Tracks")
        
        input("\nPress Enter to go back...")
        self.manage_subscription()


def main():
    """Main entry point for the application."""
    app = MusicApp()
    
    # Display welcome message
    print("\n" + "=" * 50)
    print(" " * 10 + "🎵 MUSIC MANAGEMENT SYSTEM 🎵")
    print("=" * 50)
    print("\nWelcome to the Music Management System!")
    print("This system allows you to browse music, create playlists,")
    print("and manage your music library.")
    print("\nSample Users:")
    print("- Username: john_doe, Password: password123 (Free)")
    print("- Username: jane_smith, Password: securepass (Premium)")
    print("- Username: music_lover, Password: tunes4life (Free)")
    
    input("\nPress Enter to start...")
    
    # Start the application
    app.display_login_menu()


if __name__ == "__main__":
    main()