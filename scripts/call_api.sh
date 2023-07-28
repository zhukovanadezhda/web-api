#!/bin/bash

# Check if an XML file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <path_to_xml_file>"
    exit 1
fi

# Get the XML file from the argument
xml_file="$1"

# Start the Flask app
python3 app.py &

# Wait for the app to start
sleep 5

api_url="http://localhost:5000"

# Make the POST request and save the response to a JSON file
curl -X POST -F "file=@${xml_file}" "${api_url}" -o output.json

kill $!

echo "API call completed. Response saved to 'output.json'."