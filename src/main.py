import os


def replace_spaces(path="", walk=False, replacement="_"):
    """Replace spaces with undersceres in all file names."""
    if not path:
        path = os.getcwd()

    if path[-1] == "/":
        path = path[:-1]

    if walk:
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if not d[0] == '.']
            for filename in files:
                if filename[0] != '.':
                    os.rename(root + "/" + filename, root + "/" + filename.replace(" ", replacement))
    else:
        for filename in next(os.walk(path))[2]:
            if filename[0] != ".":
                os.rename(path + "/" + filename, path + "/" + filename.replace(" ", replacement))
