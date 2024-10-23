from flask import Flask, request, jsonify
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf
import os

app = Flask(__name__)

model = tf.keras.models.load_model('model/model-Corn-Leaf-Diseases-Exception-92.12.h5')

class_labels = {0: 'Blight', 1: 'Common_Rust', 2: 'Gray_Leaf_Spot', 3: 'Healthy'}

@app.route('/')
def index():
    return 'Server is running...'


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    img_path = os.path.join('uploads', file.filename)
    file.save(img_path)

    try:
        image = Image.open(img_path)

        if image.mode == 'RGBA':
            image = image.convert('RGB')

        image = ImageOps.fit(image, (224, 224))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array)[0]
        predicted_class_index = np.argmax(prediction)
        predicted_class = class_labels[predicted_class_index]
        predicted_percentage = prediction[predicted_class_index] * 100

        os.remove(img_path)

        return jsonify({
            'predicted_class': predicted_class,
            'predicted_percentage': f"{predicted_percentage:.2f}%",
            'probabilities': {
                class_labels[i]: f"{prob * 100:.2f}%" for i, prob in enumerate(prediction)
            },
            'success': True,
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

