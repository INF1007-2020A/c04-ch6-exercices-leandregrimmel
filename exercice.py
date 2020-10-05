#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = []
        while len(values) < 10:
            values.append(input("Entrez une seule valeur\n"))

    print("The sorted list is:", sorted(values))
    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        words = []
        while len(words) < 2:
            words.append(input("Entrez un mot:\n"))

        print(sorted(words[0]))
        print(sorted(words[1]))
    print("Ces deux mots sont des anagrames:", sorted(words[0]) == sorted(words[1]))

    return sorted(words[0]) == sorted(words[1])


def contains_doubles(items: list) -> bool:
    return len(set(items)) != len(items)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key, value in student_grades.items():
        avg = sum(value) / len(value)

        if len(best_student) == 0 or list(best_student.values())[0] < avg:
            best_student = {key: avg}

    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequency = dict()
    for letter in sentence:
        frequency[letter] = sentence.count(letter)
        sorted_keys = sorted(frequence, key=frequency.__getitem__, reverse=True)
        for key in sorted_keys:
            if frequency[key] > 5:
                print("le charactère {0} revient {1} fois.".format(key, frequency[key]))

    return frequency


def get_recipes(dictionnaire):
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Entrez le nom de votre recette\n")
    ingrediants = input("Entrez la liste d'ingrédiants de la recette, svp séparer les ingrédients par une ,")
    dictionnaire[name] = ingrediants

    return dictionnaire


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Entrez le nom d'une recette")
    if name in ingredients:
        print(ingredients[name])
    else:
        print("la recette demandé n'existe pas")
        print("Les recettes existance sont:", list)
        print_recipe(ingredients)


def main() -> None:
    print(list(range(3, 22, 2))[-7:-2:3])
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")

    recipes = get_recipes({})
    recipes = get_recipes(recipes)

    print("On affiche une recette au choix...")

    print_recipe(recipes)


if __name__ == '__main__':
    main()
