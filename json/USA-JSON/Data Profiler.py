import json

from dataprofiler import Data, Profiler

# Load and profile a CSV file
data = Data("Country suicide rate.csv")  # Auto-Detect & Load: CSV, AVRO, Parquet, JSON, Text, URL
profile = Profiler(data)  # Calculate Statistics, Entity Recognition, etc

# Update the profile with new data:
new_data = Data("new_data.csv")
profile.update_profile(new_data)

# Print the report using json to prettify.
readable_report = profile.report(report_options={"output_format": "pretty"})
print(json.dumps(readable_report, indent=4))
