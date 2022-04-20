def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui."""
    string_list = list(word)
    if len(string_list) == 0:
        return False
    if len(string_list) == 1:
        return True
    if len(string_list) == 2:
        return string_list[0] == string_list[1]
    return string_list[0] == string_list[-1] and is_palindrome_recursive(
      "".join(string_list[1:-1]), 0, 0
      )
