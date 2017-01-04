# PlexDownloader

Desktop sync client and server-to-server sync client

## Features

* Lightweight
* WebUI to manage sync items! (desktop+mobile)
* Cross platform Python Script
* Does not require Plex Pass.
* Movie Support
* TV Show Support
* Music Support [By Artists]
* Photo Support [By Albums]
* Custom Movie Sync Directory
* Custom TV Show Sync Directory
* Custom Music Sync Directory
* Custom Photo Sync Directory
* TV Show Custom Sync (Latest Episode, Current Season, or All Episodes)
* TVShow Auto Delete functionality to delete old episodes when new episode becomes available.
* Full Server Sync [Will sync all content from one server to another]
* myPlex Support for Remote Downloading (Customized code from HTPC-Manager to get this working)
* Transcoded Downloading - So you can convert on the fly and save to drive and conserve disk space.
* Unwatched sync option for TV/Movies.
* WebUI Force Search Buttons
* File deletion upon unsync [optional]
* Autosync new movies/tvshows from recently added, recently viewed, recently released, on deck, etc
* myPlex Token Caching [Only connects to myPlex once for token, so sync will work even if myPlex is down.]
* Easy to access search Buttons for TMDB, TVDB, TADB, IMDB, Traileraddict, etc in webui.

## Website

Plex Forum: https://forums.plex.tv/discussion/115593/beta-plex-downloader-desktop-sync

## Configuration:

1. Rename the user.ini.config to user.ini.
2. Edit the user.ini with information that is relevant to your install.
3. If you are downloading/syncing remotely you must enter your myplex information and enable myplex.
4. Start by running "python plexdl.py".

## Find the section ID
You can find your movie/music/tv/photo section ID by visiting your Plex Web and going to the category you want to sync. Example:
```
http://192.168.3.5/web/index.html#!/server/.../section/2
```
The ID you are looking for is the number at the end which in the above example is 2.

You can also find your content section ID by visiting:
```
http://localhost:32400/library/sections/
```

## Find the transcode profiles
Transcoder client profiles can be found in the Plex server installed folder \Plex\Plex Media Server\Resources\Profiles.
Use the file name of the appropriate profile. Default is `HTML TV App`.

## User.ini

Note that if you need to give a `%` (percent) sign in one of the following fields, you will
actually need to double it. So for example if your password is `my%password`, you will need
to set the field as such: `password=my%%password`.

```ini
[User.Ini Options]

[general]

# Time in seconds that you want to wait between checking for new content. Default is 600 seconds (10 minutes).
sleeptime = 600  # seconds
# Enter your IP here make sure to have no "/" at the end of the ip. For example
plexurl = http://127.0.0.1:32400

[webui]

# Enable or disable the web ui for managing synced items (disable | enable)
status = enable
# Port of the web ui, default is 8585 but you can change to whatever port you want
port = 8585

[myplex]

# Used to download remotely (disable | enable)
status = disable
# Your myplex email
username = user@email.com
# Your myplex password
password = password

[tvshows]

# Activates the category so it will be scanned (disable | enable)
active = enable
# Your tv show section plex id
plexid = 4
# File whose content if the list of the tv shows you want to sync. One tv show per line. Enter exactly how you see it in plex.
tvfile = tvshows.txt
# episode|recent|all. Recent will download on the most current season. All will download every season
tvtype = recent
# Download location for your synced tvshows
tvlocation = /Users/plexdl/Downloads/TV Shows/
# Will download everything it finds, will follow tvtype so you can sync the most recent of every show (disable | enable)
fullsync = enable
# Will automatically delete old episodes (disable | enable)
autodelete = enable
# (default | server) Server uses plex server naming convention. For example .../Season X/Show s1e1 - desc.mkv
folderstructure = server
# Will download Poster, Fanart, and NFO file (disable | enable)
metadata = enable

[movies]

# Activates the category so it will be scanned (disable | enable)
active = enable
# Your movie section plex id
plexid = 5
# File whose content if the list of the movies you want to sync. One movie per line. Format: Movie (year) EX: Avatar (2009)
moviefile = movies.txt
# Download location for your synced movies
movielocation = /Users/plexdl/Downloads/Movies/
# Will download everything it finds (disable | enable)
fullsync = enable
# Will download Poster, Fanart, and NFO file (disable | enable)
metadata = enable

[music]

# Activates the category so it will be scanned (disable | enable)
active = enable
# Your music section plex id
plexid = 6
# File whose content if the list of the music artists you want to sync. One artist per line.
musicfile = music.txt
# Download location for your synced music
musiclocation = /Users/plexdl/Downloads/Music/
# Will download everything it finds (disable | enable)
fullsync = enable

[pictures]

# Activates the category so it will be scanned (disable | enable)
active = enable
# Your pictures section plex id
plexid = 7
# File whose content if the list of the picture albums you want to sync. One album per line.
picturefile = pictures.txt
# Download location for your synced pictures
picturelocation = /Users/plexdl/Downloads/Pictures/
# Will download everything it finds (disable | enable)
fullsync = enable
```

## Examples of location files:

### tvshows.txt
```
Warehouse 13
Eureka
```

### movies.txt
```
Avatar (2009)
```

### music.txt
```
The Beatles
```

### pictures.txt
```
Family Trip To France
```