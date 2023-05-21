# !/usr/bin/python3
#
#   GOD IS FIRTS
#   Copyright (C) <2023>  <JuanPerdomo00> <nanezomg@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from sys import argv, exit
from os import stat
from stat import *
from os import *
import datetime


tuxhad = """
+------------------------------------------------------------------------------+
|                                                                     ____     |
|                                                                    |    |    |
|          .--------------------------------------------------------.|    |    |
|          |                                                         |    |    |
|          |   "No is a file or dierectory"                          |    |    |
|          |                                                       ._|____|_.  |
|          '-------------------------------------------------------\||o_o |    |
|                                                                    |:_/ |    |
|                                                                   //   \ \   |
|                                                                  (|     | )  |
+------------------------------------------------------------------------------+
"""


class C:
    """
    colors from string sentences 

    red -> exit 1
    green -> status ok
    """

    r = "\033[0;31m"
    g = "\033[32m"
    y = "\033[0;33m"
    off = "\033[0m"


c = C()


class Check_file:
    def __init__(self, file: str):
        self.__file: str = file
        # It is simply the path where it will look for where the file is located
        self.__mode = stat(file).st_mode

    def __size_file(self) -> str:
        """
        !This function is responsible for calling a method to see the size of the file
        """
        return str(stat(self.__file).st_size)

    def __time(self) -> str:
        """
        This function is in charge of using the datetime class to be able to calculate the result of the stat function, with the ctime and mtime method. Giving us the result at the time of creation and time of last time used.
        """
        last_time = str(datetime.datetime.fromtimestamp(
            stat(self.__file).st_mtime))[:19]

        return last_time

    def __file_extencion(self) -> str:
        """
            This function will have a dictionary with the description and extension of the files, with the library we can interpret the results with stat.
        """
        tmp_file = self.__file
        file_extencion = path.splitext(tmp_file)[1]

        file_type = {".cpp": "C++ Source Code",
                     ".cc": "C++ Source Code",
                     ".cxx": "C++ Source Code",
                     ".c": "C Source Code",
                     ".h": "C/C++ Header",
                     ".py": "Python Source Code",
                     ".sh": "Bash Script",
                     ".java": "Java Source Code",
                     ".js": "Javascript Source Code",
                     ".rb": "Ruby Source Code",
                     ".pl": "Perl Source Code",
                     ".pm": "Perl Source Code",
                     ".php": "PHP Source Code",
                     ".swift": "Swift Source Code",
                     ".kt": "Kotlin Source Code",
                     ".rs": "Rust Source Code",
                     ".go": "Go Source Code",
                     ".ts": "Typescript Source Code",
                     ".scala": "Scala Source Code",
                     ".lua": "Lua Source Code",
                     ".hs": "Haskell Source code",
                     ".r": "R Source Code",
                     ".m": "Matlab Source Code",
                     ".asm": "Assembly Source Code",
                     ".S": "Assembly Source Code",
                     ".txt": "Text File",
                     ".pdf": "Image File",
                     ".jpg": "Image File",
                     ".jpeg": "Image File",
                     ".doc": "Microsoft Word Document",
                     ".docx": "Microsoft Word Document",
                     ".xls": "Microsoft Excel Spreadsheet",
                     ".xlsx": "Microsoft Excel Spreadsheet",
                     ".ppt": "Microsoft Powerpoint Presentation",
                     ".pptx": "Microsoft Powerpoint Presentation",
                     ".gif": "Graphics Interchange Format",
                     ".mp3": "Audio file",
                     ".mp4": "Video File",
                     ".mkv": "Video File",
                     ".zip": "Zip Archive File",
                     ".tar": "Tape Archive File",
                     ".exe": "Windows Executable File",
                     ".deb": "Debian/Ubuntu Package file",
                     ".rpm": "Red Hat/Fedora Package File",
                     ".iso": "CD/DVD Disk Image File",
                     ".so": "Linux Shared Object Library File",
                     ".odt": "OpenDocument text",
                     ".rtf": "Rich Text Format",
                     ".html": "Hypertext Markup Language",
                     ".xml": "eXtensible Markup Language",
                     ".ods": "OpenDocument Spreadsheet",
                     ".csv": "Comma-Separated Values",
                     ".tsv": "Tab-Separated Values",
                     ".odp": "OpenDocument Presentation",
                     ".bmp": "Bitmap Image",
                     ".tiff": "Tagged Image File Format",
                     ".svg": "Scalable Vector Graphics",
                     ".psd": "Adobe Photoshop Document",
                     ".wav": "Waveform Audio File Format",
                     ".aac": "Advanced Audio Coding",
                     ".flac": "Free Lossless Audio Codec",
                     ".ogg": "Ogg Vorbis",
                     ".midi": "Musical Instrument Digital Interface",
                     ".avi": "Audio Video Interleave",
                     ".mov": "QuickTime Movie",
                     ".wmv": "Windows Media Video",
                     ".flv": "Flash Video",
                     ".rar": "Roshal Archive",
                     ".7z": "7-zip Compressed File",
                     ".bz2": "Bzip2 Compressed File",
                     ".sql": "Structured Query Language",
                     ".db": "Database File",
                     ".accdb": "Microsoft Access Database",
                     ".json": "Javascript Object Notation",
                     ".dll": "Dynamic Link Library",
                     ".apk": "Android Package File",
                     ".ttf": "TrueType Font File",
                     ".otf": "OpenType Font file"
                     }

        if path.islink(self.__file):
            return "Is  A Symbolic Link"
        elif S_ISDIR(self.__mode):
            return "Directory"

        for exten, descip in file_type.items():
            if S_ISREG(self.__mode):
                if access(self.__file, X_OK):
                    return "Executable"
                elif exten == file_extencion:
                    return descip

        return "Regular File"

    def __permisson(self):
        """
        In this function we will take the user constants in integer and with the bit operator and we will add them and depending on the result in decimal 1 or 0, rwx is printed
        """

        permisson_file = ""

        # Owner permissions
        permisson_file += "r" if self.__mode & S_IRUSR else "-"
        permisson_file += "w" if self.__mode & S_IWUSR else "-"
        permisson_file += "x" if self.__mode & S_IXUSR else "-"

        # Group permissions
        permisson_file += "r" if self.__mode & S_IRGRP else "-"
        permisson_file += "w" if self.__mode & S_IWGRP else "-"
        permisson_file += "x" if self.__mode & S_IXGRP else "-"

        # Others permissions
        permisson_file += "r" if self.__mode & S_IROTH else "-"
        permisson_file += "w" if self.__mode & S_IWOTH else "-"
        permisson_file += "x" if self.__mode & S_IXOTH else "-"

        return permisson_file

    def run(self) -> None:
        size: str = self.__size_file()
        time: str = self.__time()
        type_file: str = self. __file_extencion()
        permissions: str = self.__permisson()

        print(f"File Name: {c.g}{self.__file}{c.off}")
        print(f"File Size: {c.y}{size} {c.y}bytes{c.off}")
        print(f"Last Modified: {c.g}{time}{c.off}")
        print(f"File Type: {c.g}{type_file}{c.off}")
        print(f"Permissions: {c.r}{permissions}{c.off}")


if __name__ == "__main__":
    try:
        file: str = argv

        if len(file) != 2:
            exit(f"{c.r}[!] use {file[0]} filename {c.off}")

        check = Check_file(file[1])
        check.run()
    except FileNotFoundError:
        exit(tuxhad)
