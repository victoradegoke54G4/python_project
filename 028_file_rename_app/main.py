import pathlib as pl
print('\n================ WELCOME TO THE RENAME APP ========================')

def rename_files(file_name, new_file_name, file_type, seq_num =0):
    current_path =pl.Path.cwd()
    for item in current_path.iterdir():
        # print(item.name)
        if item.is_file() and item.suffix ==file_type:
            if item.stem == file_name:
                update_name = new_file_name + file_type
                item.rename(update_name)
                print('File name has been successfully changed from {} to {}'.format(file_name+file_type, new_file_name+file_type))
                return
            elif file_name == 'All':
                update_name = new_file_name + seq_num + file_type
                item.rename(update_name)
                print(update_name)
                print('File name has been successfully changed from {} to {}'.format(item.name + file_type, update_name))
                seq_num +=1

    if file_name != 'All': 
        print('The file {} does not exist'.format(file_name+file_type))

if __name__ == '__main__':
    rename_files('file_name', 'new_file_name', '.file_type')