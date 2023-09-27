import json

def is_valid_json(10000_tweets_1.json):
    try:
        json.loads(10000_tweets_1.json)
        return True
    except ValueError as e:
        return False

# Example usage:
json_data = '{"key": "value"}'
if is_valid_json(json_data):
    print("Valid JSON")
else:
    print("Invalid JSON")
