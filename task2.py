import os
with open("4.txt", "w", encoding="utf-8") as file:
    dict_={}
    dict_text={}
    for filename in os.listdir("sorted"):
        with open(os.path.join("sorted", filename), 'r', encoding='utf-8') as f:
            text=f.read()
            text2=text.split("\n")
            len_=len(text)
            dict_text[len(text2)]= text
            dict_[filename]= len(text2)
    sorted_tuple = dict(sorted(dict_.items(), key=lambda x: x[1]))
    for x, y in sorted_tuple.items():
        file.write(str(x))
        file.write('\n')
        file.write(str(sorted_tuple[x]))
        file.write('\n')
        file.write(str(dict_text[y]))
        file.write('\n')
