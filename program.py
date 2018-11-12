import os


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


def main():
    print_the_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)

    # get or create output folder
    # download cats
    # display cats


if __name__ == '__main__':
    main()
