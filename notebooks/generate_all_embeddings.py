import pandas as pd
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
import pickle
import os
from sklearn.neighbors import NearestNeighbors

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using {device}")

# Load model and tokenizer
model_ckpt = "sentence-transformers/all-mpnet-base-v2"
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = AutoModel.from_pretrained(model_ckpt)
model.to(device)

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

def get_embeddings(text_list):
    encoded_input = tokenizer(text_list, padding=True, truncation=True, return_tensors='pt')
    encoded_input = {key: val.to(device) for key, val in encoded_input.items()}
    with torch.no_grad():
        model_output = model(**encoded_input)
    embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
    embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)
    return embeddings.cpu().numpy()

# Load data
print("Loading data...")
job_posting = pd.read_csv('job_posting_data.csv')
students = pd.read_csv('students5.csv')

# Generate embeddings for job descriptions
print("Generating embeddings for job descriptions...")
job_embeddings = get_embeddings(job_posting['description'].tolist())

# Generate embeddings for student skills
print("Generating embeddings for student skills...")
student_embeddings = get_embeddings(students['skills'].tolist())

# Create and train KNN model
print("Training KNN model...")
knn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
knn.fit(student_embeddings)

# Save all files
print("Saving files...")
with open('embeddings_mpnet.pkl', 'wb') as f:
    pickle.dump(job_embeddings, f)

with open('students_position_embeddings.pkl', 'wb') as f:
    pickle.dump(student_embeddings, f)

with open('knn_model.pkl', 'wb') as f:
    pickle.dump(knn, f)

print("Done!") 