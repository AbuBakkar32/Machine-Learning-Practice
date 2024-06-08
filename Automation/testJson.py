import json
from jsonschema import validate, ValidationError

# Load schema
with open('schema.json') as schema_file:
    schema = json.load(schema_file)

# Load JSON responses
with open('cars.json') as responses_file:
    responses = json.load(responses_file)

# Validate each response
for idx, response in enumerate(responses):
    try:
        validate(instance=response, schema=schema)
        print(f"Response {idx} is valid")
    except ValidationError as e:
        print(f"Response {idx} is invalid: {e.message}")
