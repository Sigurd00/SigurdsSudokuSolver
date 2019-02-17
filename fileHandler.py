import os


def load(name):
    """
    This method creates and loads a new Sudoko
    :param name: The base name of the Sudoko to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_path_name(name)

    if os.path.exists(filename):
        with open(filename, 'r') as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):

    filename = get_full_path_name(name)
    print("...Saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_path_name(name):
    filename = os.path.abspath(os.path.join('.', 'journals/', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    return None
