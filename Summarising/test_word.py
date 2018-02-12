from Summarising.word_processor import input_file, summarize

t = input_file('test.txt')
words = t.word_barrier()
print(summarize('test.txt', words))