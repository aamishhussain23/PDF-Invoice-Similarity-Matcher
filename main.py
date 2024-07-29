import PyPDF2
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def extract_features(texts):
    vectorizer = TfidfVectorizer(stop_words='english')
    features = vectorizer.fit_transform(texts)
    return features, vectorizer

def calculate_similarity(features):
    similarity_matrix = cosine_similarity(features)
    return similarity_matrix

database = []  

def find_most_similar_invoice(input_pdf, database):
    input_text = extract_text_from_pdf(input_pdf)
    texts = [invoice[0] for invoice in database] + [input_text]
    features, vectorizer = extract_features(texts)
    similarity_matrix = calculate_similarity(features)
    
    input_index = len(database)
    similarities = similarity_matrix[input_index][:-1]
    
    most_similar_index = np.argmax(similarities)
    most_similar_score = similarities[most_similar_index]
    
    return database[most_similar_index][1], most_similar_score

def add_invoice_to_database(pdf_path, database):
    text = extract_text_from_pdf(pdf_path)
    database.append((text, pdf_path))

if __name__ == "__main__":

    # add_invoice_to_database('invoice1.pdf', database)
    add_invoice_to_database('invoice2.pdf', database)
    add_invoice_to_database('invoice3.pdf', database)
    add_invoice_to_database('invoice4.pdf', database)
    add_invoice_to_database('invoice5.pdf', database)
    add_invoice_to_database('invoice6.pdf', database)
    add_invoice_to_database('invoice7.pdf', database)
    
    input_invoice = 'invoice1.pdf'
    most_similar_invoice, similarity_score = find_most_similar_invoice(input_invoice, database)
    
    print(f"The most similar invoice is: {most_similar_invoice}")
    print(f"Similarity score: {similarity_score}")
