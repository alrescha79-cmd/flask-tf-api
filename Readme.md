# Flask TensorFlow API for Corn Leaf Disease Detection

A simple REST API built with Flask that uses a TensorFlow model to predict corn leaf diseases. This API accepts images of corn leaves, processes them, and returns the predicted class along with the prediction confidence.

## Dataset

[Kaggle](https://www.kaggle.com/datasets/smaranjitghose/corn-or-maize-leaf-disease-dataset)

## Features

- Upload an image of a corn leaf and get a disease prediction.
- Supports multiple classes: Blight, Common Rust, Gray Leaf Spot, and Healthy.
- Easily deployable with minimal dependencies.

## Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

## Installation

### Clone the Repository

 ```bash
   git clone https://github.com/alrescha79-cmd/flask-tf-api.git
```

#### change directory

```bash
    cd flask-tf-api
```

### Create a Virtual Environment

```bash
python -m venv venv
```

#### For Linux/MacOS

```bash
source venv/bin/activate 
```

##### For Windows

```bash
venv\Scripts\activate 
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

## Usage/Examples

### Start the API

Run the Flask server with the following command:

```bash
python app.py
```

By default, the server will start on <http://localhost:5000>.

### Make a Prediction

Use curl or tools like Postman to send a POST request to the /predict endpoint with an image file:

```bash
curl -X POST -F 'file=@/path/to/your/image.jpg' http://localhost:5000/predict
```

Replace /path/to/your/image.jpg with the path to your image file. The API will return a JSON response containing the predicted class and its confidence percentage.

## Testing

To test the API:

### Unit Tests

Create unit tests to validate model predictions and API responses. If using pytest, you can run:

```bash
pytest
```

### Manual Testing

Upload different images of corn leaves to test if the model returns the correct prediction.

### Example Response

After sending a request with an image, you should receive a JSON response like this:

```json
{
  "predicted_class": "Healthy",
  "predicted_percentage": "95.67%",
  "probabilities": {
    "Blight": "1.23%",
    "Common_Rust": "2.45%",
    "Gray_Leaf_Spot": "0.65%",
    "Healthy": "95.67%"
  }
}
```

## Notes

Make sure model.h5 is placed in the `model/model.h5` directory or update the model path in the code.

Adjust the image preprocessing size if your model requires a different input size.

*This model.h5 still does not have perfect accuracy because this is only an example.*

## Acknowledgements

TensorFlow for providing a powerful framework for deep learning.

Flask for making it easy to create APIs.

The agricultural community for contributing datasets of corn leaf diseases.
