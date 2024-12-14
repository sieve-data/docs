import json
import os

def update_job_schema():
    # Read the file with proper encoding
    with open("docs/openapi.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Define timestamp fields and their descriptions
    timestamp_fields = {
        "created_at": "The time the job was created",
        "started_at": "The time the job started processing",
        "completed_at": "The time the job was completed"
    }

    # Look for Job-related schemas in components/schemas
    schemas = data.get("components", {}).get("schemas", {})
    job_schemas = {
        name: schema for name, schema in schemas.items()
        if ("Job" in name or name == "Job") and "properties" in schema
    }

    # Update timestamp fields in all job-related schemas
    for schema_name, schema in job_schemas.items():
        for field, base_desc in timestamp_fields.items():
            if field in schema["properties"]:
                schema["properties"][field].update({
                    "type": "string",
                    "format": "date-time",
                    "description": f"{base_desc} (ISO8601 format with milliseconds in UTC timezone, e.g. 2024-12-14T20:19:31.680000)"
                })

    # Write back with proper formatting
    with open("docs/openapi.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    update_job_schema()
