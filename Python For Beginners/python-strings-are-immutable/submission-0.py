def remove_fourth_character(word: str) -> str:
    first = word[:3]
    second = word[4:]

    final = first + second

    return final


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
