import re
from row import row as MAGIC_ROW


vector_one = MAGIC_ROW.split("\"buddy_id\"")
vector_two = []


for i in range(len(vector_one)):
    search = re.findall(
        r'("__isProfile":"User","name":"[\w\W]*","story_bucket")', 
        vector_one[i]
    )
    if search != []:
        name = search[0].replace('__isProfile":"User","name":"', '')
        name = name.replace('","story_bucket"', '')
        name = name.replace('"', '')
        vector_two.append([i, name,])


for element in vector_two:
    print(f'{element[0]}  {element[1]}')