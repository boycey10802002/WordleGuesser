import utils
import re
dictionary_input = utils.Dictionary_Path().joinpath("raw_word_list.txt")
dictionary_output = utils.Project_Path().joinpath("wordle_dictionary.txt")

def filter(word_list : str):
    new_list = []
    for word in word_list:
        word = word.strip()
        if len(word) == 5:
            if re.search(r"[0-9_\-']", word) is not None:
                continue
            new_list.append(word.upper())
    print(new_list)
    return "\n".join(new_list)


if __name__ == "__main__":
    new_dictionary = None
    with open(dictionary_input, 'r') as f_in:
        new_dictionary = filter(f_in.readlines())

    with open(dictionary_output, 'w+') as f_out:
        f_out.writelines(new_dictionary)

