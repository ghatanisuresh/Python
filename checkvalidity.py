import re

# Read the dataset from the text file
with open('D:/MQ/Fourth Session/BigData/Assignment/Assignment 2/Python/10000_tweets_1.json', 'r', encoding='utf-8') as file:
    data = file.read()


def is_valid_json(json_str):
    opening_braces = re.findall(r'\{', json_str)
    closing_braces = re.findall(r'\}', json_str)
    opening_brackets = re.findall(r'\[', json_str)
    closing_brackets = re.findall(r'\]', json_str)

    return (len(opening_braces) == len(closing_braces) and
            len(opening_brackets) == len(closing_brackets))

if is_valid_json(data):
    print("JSON is valid")
else:
    print("JSON is not valid")


json_data = re.sub(r'"(.*?)"', r'"\1\\"', data)

json_data = re.sub(r',\s*([}\]])', r'\1', data)

json_data = re.sub(r'undefined', 'null', data)


with open('clean.json', 'w') as output_file:
    output_file.write(json_data)

print("Cleaned JSON data has been saved to 'clean.json'.")