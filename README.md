# Sign Language Recognition

A computer vision project that recognizes American Sign Language (ASL) hand gestures using MediaPipe and TensorFlow/Keras.

## Overview

This project uses webcam input to detect hand gestures and classify them into ASL letters. Currently trained to recognize letters A, B, and C with real-time prediction capabilities.

## Features

- Real-time hand detection using MediaPipe
- Gesture classification using TensorFlow/Keras model
- Data collection script for training new gestures
- Confidence threshold filtering for accurate predictions
- Visual feedback with bounding boxes and predictions

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- TensorFlow/Keras
- cvzone

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sign_language
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Real-time Gesture Recognition

Run the main recognition script:
```bash
python test.py
```

- Press 'q' to quit the application
- The camera will detect your hand and display the predicted letter
- Predictions with confidence below 20% are filtered out

### Data Collection

To collect training data for new gestures:
```bash
python data_collection.py
```

- Press 's' to save the current hand gesture
- Press 'q' to quit
- Images are saved to the `Data/` directory

## Project Structure

```
sign_language/
├── Data/              # Training data storage
├── Model/             # Trained model and labels
│   ├── keras_model.h5 # TensorFlow model
│   └── labels.txt     # Class labels
├── data_collection.py # Data collection script
├── test.py           # Main recognition script
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Current Model

The model is currently trained to recognize:
- **A** - Letter A in ASL
- **B** - Letter B in ASL  
- **C** - Letter C in ASL

## How It Works

1. **Hand Detection**: MediaPipe detects hand landmarks from webcam feed
2. **Image Processing**: Hand region is cropped, resized, and normalized to 300x300 pixels
3. **Classification**: TensorFlow model predicts the ASL gesture
4. **Filtering**: Low-confidence predictions are filtered out for accuracy

## Training New Gestures

1. Use `data_collection.py` to collect sample images for new gestures
2. Update the `labels.txt` file with new class names
3. Train a new model using your preferred deep learning framework
4. Replace `Model/keras_model.h5` with your trained model

## System Requirements

- Webcam or camera device
- Sufficient lighting for hand detection
- Python environment with required dependencies

## Contributing

Feel free to contribute by:
- Adding support for more ASL letters
- Improving model accuracy
- Enhancing the user interface
- Adding new features

## License

This project is open source. Please check the license file for details.
