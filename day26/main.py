import pandas

df = pandas.read_csv("day26/nato_phonetic_alphabet.csv")

dict = {row.letter:row.code for (index, row) in df.iterrows()}

word = input("Enter a word: ").upper()
output_list = [dict[alphabet] for alphabet in word]
print(output_list)