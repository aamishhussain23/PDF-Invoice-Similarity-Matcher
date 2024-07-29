from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from skimage.metrics import structural_similarity as ssim
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import os

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

def calculate_cosine_similarity(features):
    similarity_matrix = cosine_similarity(features)
    return similarity_matrix

def calculate_jaccard_similarity(text1, text2):
    vectorizer = CountVectorizer(stop_words='english').fit([text1, text2])
    set1 = set(vectorizer.transform([text1]).toarray()[0])
    set2 = set(vectorizer.transform([text2]).toarray()[0])
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

def convert_pdf_to_images(file_path):
    return convert_from_path(file_path)

def resize_image(img, size):
    return img.resize(size, Image.LANCZOS)

def calculate_image_similarity(image1_path, image2_path):
    images1 = convert_pdf_to_images(image1_path)
    images2 = convert_pdf_to_images(image2_path)
    
    ssim_scores = []
    for img1, img2 in zip(images1, images2):
        img1 = img1.convert('L')
        img2 = img2.convert('L')
        # Resize images to the same size
        size = (min(img1.width, img2.width), min(img1.height, img2.height))
        img1 = resize_image(img1, size)
        img2 = resize_image(img2, size)
        img1 = np.array(img1)
        img2 = np.array(img2)
        ssim_scores.append(ssim(img1, img2))
    
    return np.mean(ssim_scores)

database = []

def find_most_similar_invoice(input_pdf, database):
    input_text = extract_text_from_pdf(input_pdf)
    texts = [invoice[0] for invoice in database] + [input_text]
    features, vectorizer = extract_features(texts)
    cosine_sim_matrix = calculate_cosine_similarity(features)
    
    input_index = len(database)
    cosine_similarities = cosine_sim_matrix[input_index][:-1]
    
    jaccard_similarities = [
        calculate_jaccard_similarity(input_text, invoice[0]) for invoice in database
    ]
    
    image_similarities = [
        calculate_image_similarity(input_pdf, invoice[1]) for invoice in database
    ]
    
    combined_similarities = [
        (cosine_similarities[i] + jaccard_similarities[i] + image_similarities[i]) / 3
        for i in range(len(database))
    ]
    
    most_similar_index = np.argmax(combined_similarities)
    most_similar_score = combined_similarities[most_similar_index]
    
    return database[most_similar_index][1], most_similar_score

def add_invoice_to_database(pdf_path, database):
    text = extract_text_from_pdf(pdf_path)
    database.append((text, pdf_path))

if __name__ == "__main__":
    # add_invoice_to_database('pdfs/invoice1.pdf', database)
    add_invoice_to_database('pdfs/invoice2.pdf', database)
    add_invoice_to_database('pdfs/invoice3.pdf', database)
    add_invoice_to_database('pdfs/invoice4.pdf', database)
    add_invoice_to_database('pdfs/invoice5.pdf', database)
    add_invoice_to_database('pdfs/invoice6.pdf', database)
    add_invoice_to_database('pdfs/invoice7.pdf', database)
    
    input_invoice = 'pdfs/invoice1.pdf'
    most_similar_invoice, similarity_score = find_most_similar_invoice(input_invoice, database)
    
    print(f"The most similar invoice is: {os.path.basename(most_similar_invoice)}")
    print(f"Similarity score: {similarity_score}")
