from ascii_logo_art import logo
from music import song_list

def playlist():
    print('\n🎵 AVAILABLE SONGS:\n')
    for b_index, (band, songs) in enumerate(song_list, 1):
        for song_num, song in songs:
            print(f'{b_index}:{song_num} {band} - {song}')
 
# def get_music(userchoice): #1:2
#     choice = userchoice.split(':')
#     first, second = choice[0], choice[1]
#     band_index = song_list[int(first)-1][0]
#     song_index = song_list[int(first)-1][1][int(second)-1][1]
#     return f'{song_index} by {band_index} playing now.'

def get_music(userchoice):
    try:
        first, second = map(int, userchoice.split(':'))
        band_name, songs = song_list[first - 1]
        song_title = songs[second - 1][1]
        return f'{song_title} by {band_name} is now playing...'
    except (ValueError, IndexError):
        return 'Invalid song choice. Try again.'

def main():
    print(logo)
    playlist()

    while True:
        user_input = input('\nSelect a song to play (format: Band#:Song#) → ').strip()

        if not user_input:
            print('⚠️ Please enter a valid input.')
            continue

        print(get_music(user_input))

        change_input = input('\nPress [C] to change song, or any key to exit: ').lower()
        if change_input != 'c':
            break

    print('\n🎧 Thank you for listening!')

if __name__ == '__main__':
    main()
