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
git clone https://github.com/roystondz/Sign-Language-Recognition.git
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
- Each saved image is timestamped to avoid duplicates

**Tips for better training data:**
- Ensure good lighting and clear hand visibility
- Capture gestures from different angles and positions
- Collect at least 50-100 images per gesture class
- Keep hand centered in the frame when capturing

## Project Structure

```
sign_language/
├── Data/              # Training data storage
│   ├── A/            # Images for gesture A
│   ├── B/            # Images for gesture B
│   └── C/            # Images for gesture C
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

You have two options for training new gesture models:

### Option 1: Using Google Teachable Machine (Recommended)

Google Teachable Machine provides an easy-to-use web interface for training image classification models:

1. **Collect Training Data:**
   - Use `data_collection.py` to capture gesture images
   - Organize images into separate folders for each gesture class
   - Example structure: `Data/A/`, `Data/B/`, `Data/C/`

2. **Train with Teachable Machine:**
   - Go to [Teachable Machine](https://teachablemachine.withgoogle.com/)
   - Select "Image Project" → "Standard Image Model"
   - Upload your gesture images to different classes
   - Train the model (this may take a few minutes)
   - Test the model with the webcam preview

3. **Export the Model:**
   - Click "Export Model"
   - Select "TensorFlow" format
   - Choose "Keras" or "TensorFlow.js" (Keras recommended)
   - Download the model files

4. **Integrate with Project:**
   - Replace `Model/keras_model.h5` with the downloaded model
   - Update `Model/labels.txt` with your class names
   - Ensure the labels match the order used in Teachable Machine

### Option 2: Custom Training

For advanced users who want to train models locally:

1. Use `data_collection.py` to collect training data
2. Update the `labels.txt` file with new class names
3. Train a new model using your preferred deep learning framework
4. Replace `Model/keras_model.h5` with your trained model

**Teachable Machine Advantages:**
- No coding required for training
- Built-in data augmentation
- Automatic hyperparameter tuning
- Easy model testing and validation
- Export in multiple formats

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
