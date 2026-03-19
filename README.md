# Fashion Recommendation System (ML + FastAPI)

A machine learning-based fashion recommendation API that suggests **outfits, accessories, shoes, and colors**
based on user preferences like gender, season, occasion, dress type, and budget.

## Demo Overview
This system acts like a **virtual fashion stylist **, helping users get outfit suggestions based on their inputs.
 Example:
- Female
- Winter
- Office
- Eastern Style
- Budget: 2000

 Output:
- Kurta + Waistcoat
- Belt
- Heels
- Matching Colors


##  Features

-  Smart outfit recommendations using ML
-  Multi-label classification (products, shoes, accessories, colors)
-  Random Forest Classifier for multi-label predictions
-  FastAPI backend (fast & lightweight)
-  KNN fallback for better similarity matching
-  Input validation with predefined options
-  Clean dataset-based training system
-  API endpoint for frontend dropdown options
-  Model persistence using Joblib
-  End-to-end ML pipeline (training → saving → API inference)


##  Tech Stack

  - Python 
  - FastAPI 
  - Scikit-learn 
    - Random Forest Classifier 
    - K-Nearest Neighbors (KNN) 
    - OneHotEncoder
    - MinMaxScaler
    - MultiLabelBinarizer
  - Pandas & NumPy 
  - Joblib (model serialization )


## 📂 Project Structure
Recommendation
│
├── fashionscience/
│ ├── dataset/
│ ├── models/ # Saved ML models (.pkl via Joblib)
│ ├── fashionproduct.py # Model training script
│
├── fashionbackend/
│ ├── main.py # FastAPI application


