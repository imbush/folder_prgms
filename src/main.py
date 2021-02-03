import os


def replace_spaces(path="", walk=False, replacement="_"):
    """Replace spaces with undersceres in all file names.

    Ignores hidden files and folders.
    """
    if not path:
        path = os.getcwd()

    if path[-1] == "/":
        path = path[:-1]

    if walk:
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if not d[0] == "."]
            for filename in files:
                if filename[0] != ".":
                    os.rename(root + "/" + filename, root + "/" + filename.replace(" ", replacement))
    else:
        for filename in next(os.walk(path))[2]:
            if filename[0] != ".":
                os.rename(path + "/" + filename, path + "/" + filename.replace(" ", replacement))


def replace(to_repl: str, repl: str, path="", walk=False):
    """Replace to_repl string with repl string in all file names.

    Ignores hidden files and folders.
    """
    if not path:
        path = os.getcwd()

    if path[-1] == "/":
        path = path[:-1]

    if walk:
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if not d[0] == "."]
            for filename in files:
                if filename[0] != ".":
                    print(filename)
                    file, file_extension = os.path.splitext(filename)
                    print(file, file_extension)
                    os.rename(root + "/" + filename, root + "/" + file.replace(to_repl, repl) + file_extension)
    else:
        for filename in next(os.walk(path))[2]:
            if filename[0] != ".":
                file, file_extension = os.path.splitext(filename)
                print(file, file_extension)
                os.rename(path + "/" + filename, path + "/" + file.replace(to_repl, repl) + file_extension)


def add_prefix(prefix: str, extension="", path="", walk=False):
    """Add prefix to filename."""
    if not path:
        path = os.getcwd()

    if path[-1] == "/":
        path = path[:-1]
    if not extension:
        if walk:
            for root, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if not d[0] == "."]
                for filename in files:
                    if filename[0] != ".":
                        os.rename(root + "/" + filename, root + "/" + prefix + filename)
        else:
            for filename in next(os.walk(path))[2]:
                if filename[0] != ".":
                    os.rename(path + "/" + filename, path + "/" + prefix + filename)
    else:
        if walk:
            for root, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if not d[0] == "."]
                file_extension = os.path.splitext(filename)[1]
                print(file_extension)
                for filename in files:
                    if filename[0] != "." and file_extension == extension:
                        os.rename(root + "/" + filename, root + "/" + prefix + filename)
        else:
            for filename in next(os.walk(path))[2]:
                file_extension = os.path.splitext(filename)[1]
                if filename[0] != "." and file_extension == extension:
                    os.rename(path + "/" + filename, path + "/" + prefix + filename)


def add_suffix(suffix: str, extension="", path="", walk=False):
    """Add suffix to filename, before filetype."""
    if not path:
        path = os.getcwd()

    if path[-1] == "/":
        path = path[:-1]

    if not extension:
        if walk:
            for root, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if not d[0] == "."]
                for filename in files:
                    if filename[0] != "." and "." in filename:
                        file, file_extension = os.path.splitext(filename)
                        os.rename(
                                root + "/" + filename,
                                root + "/" + file + suffix + file_extension)
        else:
            for filename in next(os.walk(path))[2]:
                if filename[0] != "." and "." in filename:
                    file, file_extension = os.path.splitext(filename)
                    os.rename(
                                path + "/" + filename,
                                path + "/" + file + suffix + file_extension)
    else:
        if walk:
            for root, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if not d[0] == "."]
                for filename in files:
                    file, file_extension = os.path.splitext(filename)
                    if file_extension == extension:
                        os.rename(
                                root + "/" + filename,
                                root + "/" + file + suffix + file_extension)
        else:
            for filename in next(os.walk(path))[2]:
                if filename[0] != ".":
                    file, file_extension = os.path.splitext(filename)
                    if file_extension == extension:
                        os.rename(
                                path + "/" + filename,
                                path + "/" + file + suffix + file_extension)


replace(repl="hey", to_repl="hel", walk=True)
# add_prefix(prefix="inle's_", extension=".docx")
# add_suffix(suffix="_inle", extension=".docx")
