# Averages the numbers in a list
# Averages each list in in2DList
def sort_artists(artists_tuple):
    artists_name_list = []
    artists_sales_list = []
    for artist_tuple in artists_tuple:
        artists_name_list.append(artist_tuple[0])
        artists_sales_list.append(artist_tuple[1])
    artists_name_list.sort()
    artists_sales_list.sort()
    artists_sales_list.reverse()
    return artists_name_list, artists_sales_list


if __name__ == '__main__':
    artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
    print(sort_artists(artists))
