import json
from genson import SchemaBuilder


def json_file_to_schema(json_file_path, schema_file_path):
    # Read JSON data from the file
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Create a schema builder and add the JSON data
    builder = SchemaBuilder()
    builder.add_object(json_data)

    # Generate the JSON schema
    schema = builder.to_schema()

    # Save the JSON schema to a file
    with open(schema_file_path, 'w') as schema_file:
        json.dump(schema, schema_file, indent=2)

    print(f"Schema saved to {schema_file_path}")


# Example usage
if __name__ == "__main__":
    input_json_file = 'cars.json'  # Replace with your input JSON file path
    output_schema_file = 'schema.json'  # Replace with your desired output schema file path
    json_file_to_schema(input_json_file, output_schema_file)