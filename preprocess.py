import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.preprocessing import LabelEncoder

# Load the data
data = pd.read_csv('purchase_history.csv')

# Preprocess the data
def preprocess_data(data):
    # Convert timestamps to datetime objects
    data['timestamp'] = pd.to_datetime(data['timestamp'])

    # Label encode user_id and product_id columns
    user_encoder = LabelEncoder()
    product_encoder = LabelEncoder()

    data['user_id_encoded'] = user_encoder.fit_transform(data['user_id'])
    data['product_id_encoded'] = product_encoder.fit_transform(data['product_id'])

    return data, user_encoder, product_encoder

data, user_encoder, product_encoder = preprocess_data(data)

# Create a user-item interaction matrix
def create_interaction_matrix(data, user_col, item_col, interaction_col, threshold=0):
    interactions = data.groupby([user_col, item_col])[interaction_col] \
        .sum().unstack().reset_index().fillna(0) \
        .set_index(user_col)

    interactions = interactions.applymap(lambda x: 1 if x > threshold else 0)
    return interactions

interaction_matrix = create_interaction_matrix(data,
                                               user_col='user_id_encoded',
                                               item_col='product_id_encoded',
                                               interaction_col='timestamp')

# Save the preprocessed data and interaction matrix
data.to_csv('preprocessed_purchase_history.csv', index=False)
interaction_matrix.to_csv('interaction_matrix.csv')

print("Preprocessed data and interaction matrix saved.")
