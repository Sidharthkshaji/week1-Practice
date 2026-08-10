songs = [
    "Song A",
    "Song B",
    "Song C",
    "Song D",
    "Song E",
    "Song F",
    "Song G",
    "Song H"
]

print("Complete Playlist:",songs[:])
print("First 3 Songs:",songs[:3])
print("Last 3 Songs:",songs[-3:])
print("Songs from Position 3 to 6:",songs[3:6])
print("Every Alternate Song:",songs[::2])
print("Playlist in Reversed Order:",songs[::-1])
print("Playlist Without First and Last Song:",songs[1:-1])
short_playlist = songs[2:6]
short_playlist[0] = "Song K"
print("Original Playlist",songs)
print("Short Playlist",short_playlist)