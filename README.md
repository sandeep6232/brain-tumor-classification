
# 🧠 Brain Tumor Classification Using Deep Learning

A deep learning project that classifies brain MRI images into four categories using a trained Convolutional Neural Network (CNN) with EfficientNetB0 transfer learning.

## 📌 Project Overview

Brain tumor classification using MRI images can help demonstrate how deep learning can be applied to medical image analysis. This project predicts the category of an uploaded MRI image using a trained Keras model.

## 🎯 Classes

The model supports four classes:

- Glioma
- Meningioma
- Pituitary Tumor
- No Tumor

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- EfficientNetB0
- Streamlit
- NumPy


## 📂 Project Structure

```text
Brain_Tumor_Proj/
├── app.py
├── brain_tumor_classifier.keras
├── class_names.txt
├── requirements.txt
├── README.md
└── .gitignore
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal and upload a brain MRI image to view the model's prediction.

## Model Information

- **Architecture:** EfficientNetB0
- **Framework:** TensorFlow / Keras
- **Input:** Brain MRI image
- **Output:** Predicted class among four categories

## Model Performance

Add your actual evaluation results here after testing the model on your validation or test dataset.

- Validation accuracy: Add your measured result
- Test accuracy: Add your measured result, if available

Do not report training accuracy as test accuracy.

## Dataset

The model was trained using brain MRI images organized into the four classification categories.

Add the original dataset name, source link, and license here before publishing the repository.

The dataset itself is not included in this repository because of its size.

## Disclaimer

This project is intended for educational and research purposes only. It is not a medical diagnostic tool and must not be used to diagnose, treat, or make clinical decisions about brain tumors.

## Future Improvements

- Improve model performance and generalization.
- Add model evaluation metrics and a confusion matrix.
- Improve the Streamlit interface.
- Add explainability techniques such as Grad-CAM.
- Deploy the application online.



