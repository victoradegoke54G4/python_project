def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))


def reset_map():
    """Reset the 3x3 map for a new round"""
    map1 =  [['⬜', '⬜', '⬜'],
                            ['⬜', '⬜', '⬜'],
                            ['⬜', '⬜', '⬜']]
    
    
map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
print("\nThis is our initial map...")
print_map(map1)