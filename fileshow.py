# !/usr/bin/python3
#
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


class C:
    """
    colors from string sentences 

    red -> exit 1
    green -> status ok
    """

    r = "\033[0;31m"
    g = "\033[32m"
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

    def __time(self) -> dict:
        """
        This function is in charge of using the datetime class to be able to calculate the result of the stat function, with the ctime and mtime method. Giving us the result at the time of creation and time of last time used.
        """
        time_creation = str(datetime.datetime.fromtimestamp(
            stat(self.__file).st_ctime))[:19]
        last_time = str(datetime.datetime.fromtimestamp(
            stat(self.__file).st_mtime))[:19]

        return {"ctime": time_creation, "mtime": last_time}

    def __file_extencion(self) -> str:
        """

        """
        tmp_file = self.__file
        file_type = ""
        # .st_mode
        if S_ISREG(self.__mode):
            if access(self.__file, X_OK):
                file_type = "Executable"
            elif tmp_file.endswith(".c++") or tmp_file.endswith(".cxx") or tmp_file.endswith(".cc"):
                file_type = "C++ Source Code"
            elif tmp_file.endswith(".c"):
                file_type = "C Source Code"
            elif tmp_file.endswith(".h"):
                file_type = "C/C++ Header"
            elif tmp_file.endswith(".py"):
                file_type = "Python Source Code"
            elif tmp_file.endswith(".sh"):
                file_type = "Bash Script"
            elif tmp_file.endswith(".java"):
                file_type = "Java Source Code"
            elif tmp_file.endswith(".js"):
                file_type = "JavaScript Source Code"

        return file_type

    def run(self):
        # rint(self.__size_file())
        # print(self.__time())
        print(self.__file_extencion())


if __name__ == "__main__":
    file = argv

    if len(file) != 2:
        exit(f"{c.r}[!] use {file[0]} filename {c.off}")

    check = Check_file(file[1])

    check.run()

    print(file)
