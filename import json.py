
import re

#step 1

input_encoding = 'utf-'
# Read the dataset from the text file
with open('D:/MQ/Fourth Session/BigData/Assignment/Assignment 2/Python/10000_tweets_1.json', 'r', encoding='utf-8') as file:
    data = file.read()

# Use regex to remove comments (lines starting with /* and ending with */)
data = re.sub(r'/\*.*?\*/', '', data, flags=re.DOTALL)

# Extract valid JSON from the entire content
matches = re.findall(r'\{.*?\}', data, re.DOTALL)

valid_json_list = []
for match in matches:
    try:
        parsed_data = json.loads(match)
        valid_json_list.append(parsed_data)
    except json.JSONDecodeError:
        pass

# Now you can work with the valid_json_list, which contains all valid JSON objects.

# To print the cleaned JSON data
print(json.dumps(valid_json_list, indent=4))

# To write the cleaned JSON data to a new file
with open('cleaned_file.json', 'w', encoding='utf-8') as output_file:
    json.dump(valid_json_list, output_file, indent=4)





