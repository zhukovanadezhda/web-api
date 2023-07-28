from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    
    # Verify if there is a file in the request
    if "file" not in request.files:
        return jsonify({"error": "XML file is not found."}), 400

    file = request.files["file"]

    # Verify the format (XML)
    if file.filename.endswith(".xml"):
        tree = ET.parse(file)
        root = tree.getroot()

        matrices = []

        for data in root.findall("*"):
            if data.text is None:
                return jsonify({"error": "XML element does not contain any data."}), 400

            points = data.text.split(",")
            try:
                points = [float(point) for point in points]
            except:
                return jsonify({"error": "Invalid data in the XML file. Expected 5000 decimals per line."}), 400

            if len(points) != 5000:
                return jsonify({"error": "Wrong line size. Expected 5000 decimals per line."}), 400

            matrices.append(points)

        # Convert matrices to a NumPy array
        matrices_np = np.array(matrices)
        
        # Download the pretrained model
        model = tf.keras.models.load_model("data/model.h5")
        
        # Use the model to make predictions
        predictions = model.predict(matrices_np)

        return jsonify({"predictions": predictions.tolist()}), 200

    else:
        return jsonify({"error": "The file should be in XML format."}), 400

if __name__ == "__main__":
    app.run(port=5000)