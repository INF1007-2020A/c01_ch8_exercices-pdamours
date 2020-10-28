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


# def convert_grades() -> None:
#     pass


def grades(note_file, target_file):
    correspondances = {20: "F", 40: "D", 50: "C", 70: "B", 85: "A"}
    results = []
    with open(note_file, 'r') as note_data, open(target_file, 'w') as target:
        for line in note_data.readlines():
            note = float(line)
            for grade in correspondances.keys():
                if grade == 85 and note > grade:
                    results.append("A*\n")
                if note <= grade:
                    results.append(correspondances[grade] + "\n")
                    break
        target.writelines(results)


def check_number(n) -> bool:
    try:
        int(n)
        return True
    except ValueError:
        return False


def increasing_numbers():
    with open('exemple.txt', 'r') as f1:
        return sorted([int(word) for word in f1.read().split() if word.isdigit()])


def read_half(name_file1: str, name_file2: str):
    with open(name_file1, 'r') as f1, open(name_file2, 'w') as f2:
        count = 0
        for line in f1:
            count += 1
            if count % 2 == 0:
                f2.writelines(line)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    print(increasing_numbers())
