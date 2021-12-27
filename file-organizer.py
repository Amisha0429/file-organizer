# File organizer

# Import modules
import os
from gui import GUI

PATH = "./"


# A dictionary that will store different extensions into folders of the keys
EXTENSIONS = {
    "EXECUTABLES": [".exe", ".msi", ".jar", ".apk"],
    "IMAGES": [".jpeg",".jpg",".tiff",".gif",".bmp",".png",".PNG",".bpg",".svg",".heif",".psd"],
    "VIDEOS": [".3gp",".avi",".flv",".mng",".mov",".mp4",".mpeg",".mpg",".qt",".vob",".webm",".wmv"],
    "DOCUMENTS": [".accdb",".doc",".docm",".docx",".dotx",".dox",".epub",".fdf",".ods",".odt",".pages",".ppt",".pptx",".txt",".xls",".xlsx",".xps"],
    "PDFS": [".pdf"],
    "COMPRESSED": [".rar",".zip",".7z",".bzip2",".gzip",".tar",".wim",".xz"],
    "SCRIPTS": [".ahk", ".js", ".json", ".mq5"],
}


# To get the list of files in said folder
def get_files(path):
    return os.listdir(path)


# To craete a folder to stores files of certain types
def create_folder(file_folder):
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)
        

# To move files of certain stype into their respective folder
def move_to_folder(path, file_name, folder_name):
    file_path = os.path.join(path, file_name)
    folder_path = os.path.join(path, folder_name.capitalize(), file_name)
    try:
        os.rename(file_path, folder_path)
        print("Successfully moved-"+file_name)
    except FileExistsError as e:
        print("\n Error:Unsuccessful moving-"+file_name)


# To create a folder and move the files by calling necessary functions
def organize_files(path, file_name, destiny_folder):
    create_folder(os.path.join(path, destiny_folder.capitalize()))
    move_to_folder(path, file_name, destiny_folder)


# To get the file extension by reading everything after the '.'
def get_file_extension(file_name):
    return str(file_name[file_name.rfind("."):])


def main():
    gui = GUI()
    files_list = get_files(gui.path)
    for file_name in files_list:
        file_extension = get_file_extension(file_name)

        for file_type, extensions in EXTENSIONS.items():
            for extension in extensions:
                if file_extension == extension:
                    organize_files(gui.path, file_name, file_type)
    print("\nFiles are organized !\n")


if __name__ == "__main__":
    main()
    input('Press any key to exit')