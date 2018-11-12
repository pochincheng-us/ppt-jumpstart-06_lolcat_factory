import os
import platform
import subprocess

import cat_service


def print_the_header():
    app_name = 'CAT FACTORY'
    dashes = '-' * (5 + len(app_name) + 5)
    spaces = ' ' * 5
    print("{}".format(dashes))
    print("{}{}{}".format(spaces, app_name, spaces))
    print("{}".format(dashes))
    print('')


def get_or_create_output_folder():
    folder = 'cat_pictures'
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}...'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)
    print('done.')


def display_cats(folder):
    # open folder
    print('Displaying cats in OS window.')
    print(folder)
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        # subprocess.call(['start', folder], shell=True) // This works
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())
    pass


def main():
    print_the_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    download_cats(folder)
    display_cats(folder)


if __name__ == '__main__':
    main()
