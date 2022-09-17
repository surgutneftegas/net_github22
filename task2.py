import os
for filename in os.listdir("sorted"):
    with open(os.path.join("sorted", filename), 'r', encoding='utf-8') as f:
        text = f.readlines()
        len_ = len(text)
        dict_ = {filename: len_}
        print(dict_)