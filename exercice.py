#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def compare_files(nom_fichier_1: str, nom_fichier_2: str):
    with open(nom_fichier_1, "r") as f1, open(nom_fichier_2, "r") as f2:
        same = True

        while same:
            a = f1.read()
            b = f2.read()

            same = a == b

    return -1 if same else f1.tell()


def final_space(file1, file2):
    with open(file1, "r") as data, open(file2, "w") as result:
        result.write(data.read().replace(" ", "   "))


def check_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def increasing_numbers():
    with open('exemple.txt', 'r') as f1:
        data = f1.read()
        words = data.split()
        numbers = []
        for word in words:
            if check_number(word):
                numbers.append(int(word))
        sorted_numbers = sorted(numbers)
    return sorted_numbers


def read_half(name_file1: str, name_file2: str):
    with open(name_file1, 'r') as f1, open(name_file2, 'w') as f2:
        count = 0
        for line in f1:
            count += 1
            if count % 2 == 0:
                f2.writelines(line)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    read_half('texte.txt', 'half.txt')
