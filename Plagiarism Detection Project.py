# pip install difflib (diffrent library)

# using diiflib library
from difflib import SequenceMatcher

# read the content of files
with open("demo1.txt") as file1 , open("demo2.txt") as file2:
    data_file1 = file1.read()
    data_file2 = file2.read()

    # check the content in two files are similar or not
    matches = SequenceMatcher(None , data_file1 , data_file2).ratio()
    
    # print the persentage of the similarity
    print(f"the content in two files matches with {matches * 100}%")

