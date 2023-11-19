# Book-Recommendation-System
- Developed a book recommendation system using K-Nearest Neighbors algorithm and streamlit for the user interface. Preprocessed datasets of book ratings, book metadata, and user data containing over 100,000 entries to engineer features.
- Optimized NearestNeighbors model using brute force algorithm and sparse matrices to enable recommendations for 703 books. Built streamlit dashboard for user interaction, allowing selection of books and display of personalized recommendations and book posters. 
- Key technical skills demonstrated include Python, pandas, scikit-learn, KNN algorithms, streamlit


# Try the Book Recommendation System

https://book-recommendation-system-8e455d58e751.herokuapp.com/

# To Run

$ conda create --prefix ./env python==3.11 -y

$ conda activate ./env/

$ pip install requirements.txt

$ streamlit run app.py


# Project Work Flow

- # Data Collection and Preprocessing
- Collected 3 dataset CSV files - book ratings, book metadata, user data
- Preprocessed data - cleaned, handled missing values, engineered features like count of ratings per book
- Merged ratings data with book metadata for additional features
- Preprocessed datasets of over 100,000 entries
- # Recommendation Model Development
- Created user-book rating matrix using pivot table and sparse matrices
- Applied K-Nearest Neighbors algorithm to find most similar users and generate recommendations
- Used brute force approach for speed. Fit model on sparse matrix.
- # Building Web Application
- Developed streamlit web interface for user interaction
- Allowed user to select a book
- Integrated recommendation model to generate top 6 book suggestions
- Fetched book posters from database to display along with recommendations
- # Model Optimization
- Improved model by removing users with few ratings and low rating counts
- Parameter tuned KNN model for optimal performance
- # Deployment
- Deployed in the streamlit 
