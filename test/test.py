#!/usr/bin/python3

import pytest
from copy_fileshow import Check_file, tuxhad
from os import path

file = "main.c"

# Unit test to check if file exists
def test_file_exists():
    check = Check_file(file)
    assert path.exists(check.file) == True


# Unit test to check file size
def test_file_size():
    check = Check_file(file)
    assert check.size_file() == "74"  # bytes


# Unit test to check the last modification of the file
    check = Check_file(file)
    assert check.time() == "2023-05-26 10:42:55"


# Unit test to check file type
def test_file_type():
    check = Check_file(file)
    assert check.file_extencion() == "C Source Code"


# Unit test to check file permissions
def test_file_permissions():
    check = Check_file(file)
    assert check.permisson() == "rw-r--r--"


# Unit test to check all file properties
def test_file_properties():
    check = Check_file(file)
    # Verificar todas las propiedades del archivo
    assert check.size_file() == "74"  # bytes
    assert check.time() == "2023-05-26 10:42:55"
    assert check.file_extencion() == "C Source Code"
    assert check.permisson() == "rw-r--r--"


# Unit test to check program output in case of non-existent file
def test_file_not_found():
    try:
        check = Check_file("main.cc")
        # Verificar la salida del programa en caso de archivo inexistente
        assert check.run()
    except FileNotFoundError:
        #should print the variable tuxhad
        pass


def run_test() -> None:
    test_file_exists()
    test_file_size()
    test_file_type()
    test_file_permissions()
    test_file_properties()


if __name__ == "__main__":
    run_test()
