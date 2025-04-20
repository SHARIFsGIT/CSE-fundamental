# This file makes the services directory a Python package
# It can be left empty or can be used to expose certain classes directly

from services.music_service import MusicService
from services.user_service import UserService

__all__ = ['MusicService', 'UserService']