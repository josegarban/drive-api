import pprint, os

####################################################################################################
# FILESYSTEM
####################################################################################################

def files_in_folder_byext (extensions, folder="", print_intermediate=True):
    """
    Input: folder path (optional), list of valid extensions (optional).
    Objective: find files of certain extensions in the same folder.
    Output: list with filenames.
    """
    if folder == "":
        # Find file(s) in same folder
        files = os.listdir()
    else:
        # Find file(s) in other folder
        files = os.listdir(folder)

    filepaths = [ folder+"\\"+f for f in files ]
    for e in extensions:
        # Remove extension and change spaces into underscores
        table_names = [ f.replace(e, "") if e in f else None for f in files ]
        table_names = [ f for f in table_names if f != None ]
    if print_intermediate:
        print("Files in folder:", folder)
        print("\nFiles:\n", filepaths)

    # Get a list with just file names
    file_names = []

    if extensions != "":
        for extension in extensions:
            for file in filepaths:
                if file.endswith(extension):
                    file_names.append(file)
        if len (file_names) == 0:
            if print_intermediate:
                print("No file with the searched extensions were found.")
                print("")
        else:
            if print_intermediate:
                print("The following files with the searched extensions were found:")
                pprint.pprint(file_names)
                print("")
    else:
        for file in files:
            file_names.append(file)
        if print_intermediate:
            if len (file_names) == 0:
                print("No files were found.")
                print("")
            else:
                print("The following files were found:")
                pprint.pprint(file_names)
                print("")


    return file_names, table_names
