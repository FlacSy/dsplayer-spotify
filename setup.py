from setuptools import setup, find_packages

setup(
    name='dsplayer-spotify',  
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        'dsplayer',
        'yt-dlp',
        'spotipy'
    ],
    entry_points={
        'dsplayer.plugins': [
            'youtube = plugin.plugin:SpotifyPlugin',
        ],
    },
)