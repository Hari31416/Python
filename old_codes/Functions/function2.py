#8.6
def city_country(city, country):
	text = f"{city.title()}, {country.title()}"
	return text
print_text = city_country('agra', 'india')
print(print_text)
print_text = city_country('delhi', 'india')
print(print_text)
print_text = city_country('alaska', 'america')
print(print_text)
print_text = city_country('alethar', 'roshar')
print(print_text)

#8.7

def make_album(artist, album_name, number_songs = "NA"):
	album = {'artist' : artist.title(), 'album' : album_name.title(), 'number of songs' : number_songs}
	return album
album_details = make_album('taylor swift', 'Fearless', 18)
print(album_details)
album_details = make_album('celine dion', 'a new day has come')
print(album_details)
album_details = make_album('ed sheeran', '+', 11)
print(album_details)

#8.8
def make_album(artist, album):
	album_detail = {'artist' : artist.title(), 'album' : album.title()}
	return album_detail
while True:
	artist_name = input("Tell me the name of the artist: ")
	if artist_name == 'q':
		break
	album_name = input("Tell me the name of the album: ")
	if album_name== 'q':
		break
	album_details = make_album(artist_name, album_name)
	print(album_details)


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
    	break
    l_name = input("Last name: ")
    if l_name == 'q':
    	break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
