import pathlib as pl


def display_tree():
    directory = pl.Path.cwd()
    print(f'+ {directory}')
    entries = sorted(directory.rglob('*'))
    for entry in entries:
        depth = len(entry.relative_to(directory).parts)
        spacer = '    '* depth
        print(f'{spacer}+ {entry.name}')


if __name__ == '__main__':
    display_tree()