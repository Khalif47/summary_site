from Summarising.HashTable import HashTable


# def input_file(new_file):
#     table = HashTable()
#     new = open(new_file, "r")
#     for line in new:
#         for word in line.split():
#             word = word.strip(',')
#             word = word.strip('.')
#             word = word.strip('?')
#             word = word.strip('-')
#             word = word.strip(':')
#             word = word.strip('"')
#             word = word.strip("'")
#             word = word.strip('[')
#             word = word.strip(']')
#             word = word.lower()
#             if table[word] is None:
#                 table[word] = 1
#             else:
#                 table[word] += 1
#             if table[word] > table.max:
#                 table.max = table[word]
#     new.close()
#     return table


def input_file(text):
    table = HashTable()
    for word in text.split():
        word = word.strip(',')
        word = word.strip('.')
        word = word.strip('?')
        word = word.strip('-')
        word = word.strip(':')
        word = word.strip('"')
        word = word.strip("'")
        word = word.strip('[')
        word = word.strip(']')
        word = word.lower()
        if table[word] is None:
            table[word] = 1
        else:
            table[word] += 1
        if table[word] > table.max:
            table.max = table[word]
    return table

# def summarize(new_file, word_list):
#     sentence_list = []
#     new = open(new_file, 'r')
#     for line in new:
#         for sentence in line.split('.'):
#             counter = 0
#             for word in sentence.split():
#                 word = word.strip(',')
#                 word = word.strip('.')
#                 word = word.strip('?')
#                 word = word.strip('-')
#                 word = word.strip(':')
#                 word = word.strip('"')
#                 word = word.strip("'")
#                 word = word.strip('[')
#                 word = word.strip(']')
#                 word = word.lower()
#                 # Now process
#                 if word in word_list:
#                     counter += 1
#             # quick check
#             # need to apply machine learning techniques
#             if counter / len(word_list) > 0.55:
#                 sentence_list.append(sentence)
#     return '\n'.join(sentence_list)


def summarize(text, word_list):
    sentence_list = []
    for sentence in text.split('.'):
        counter = 0
        for word in sentence.split():
            word = word.strip(',')
            word = word.strip('.')
            word = word.strip('?')
            word = word.strip('-')
            word = word.strip(':')
            word = word.strip('"')
            word = word.strip("'")
            word = word.strip('[')
            word = word.strip(']')
            word = word.lower()
            # Now process
            if word in word_list:
                counter += 1
        # quick check
        # need to apply machine learning techniques
        if counter / len(word_list) > 0.45:
            sentence_list.append(sentence)
    return sentence_list






