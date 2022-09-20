

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label


class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist


def get_song_string(song):
    result = '"'+song.name+'" - ' + song.artist.name + ' (' + str(song.year) + ')'
    return result


if __name__ == "__main__":
    new_artist = Artist("Taylor Swift", "Big Machine Records, LLC")
    new_song = Song("You Belong With Me", "Fearless", 2008, new_artist)
    print(get_song_string(new_song))
