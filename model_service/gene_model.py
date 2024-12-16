from tensorflow.keras.models import load_model
from Bio import SeqIO
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from io import BytesIO

# Functions for preprocessing
def load_sequences(fna_file):
    sequences = []
    for record in SeqIO.parse(fna_file, "fasta"):
        sequences.append(str(record.seq))
    return sequences

def generate_kmers(sequence, k):
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

def kmers_to_numeric(kmers, kmer_size):
    kmer_dict = {"A": 0, "C": 1, "G": 2, "T": 3}
    numeric_kmers = []
    for kmer in kmers:
        num_rep = 0
        for i, char in enumerate(kmer):
            num_rep += kmer_dict[char] * (4 ** (kmer_size - i - 1))
        numeric_kmers.append(num_rep)
    return numeric_kmers

def preprocess_data(fna_file, kmer_size=3, max_len=None):
    sequences = load_sequences(fna_file)
    kmers_list = [generate_kmers(seq, kmer_size) for seq in sequences]
    numeric_sequences = [kmers_to_numeric(kmers, kmer_size) for kmers in kmers_list]
    padded_sequences = pad_sequences(numeric_sequences, maxlen=max_len, padding='post')
    return np.array(padded_sequences)

class GeneModel:
    def __init__(self):
        self.cnn_model = load_model("mutation_prediction_cnn.h5")
        self.max_len = 35546

    def load_sequences(self, fna_file):
        sequences = []
        for record in SeqIO.parse(fna_file, "fasta"):
            sequences.append(str(record.seq))
        return sequences

    def generate_kmers(self, sequence, k):
        return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

    def kmers_to_numeric(self, kmers, kmer_size):
        kmer_dict = {"A": 0, "C": 1, "G": 2, "T": 3}
        numeric_kmers = []
        for kmer in kmers:
            num_rep = 0
            for i, char in enumerate(kmer):
                num_rep += kmer_dict[char] * (4 ** (kmer_size - i - 1))
            numeric_kmers.append(num_rep)
        return numeric_kmers

    def preprocess_data(self, fna_file, kmer_size=3, max_len=None):
        sequences = load_sequences(fna_file)
        kmers_list = [self.generate_kmers(seq, kmer_size) for seq in sequences]
        numeric_sequences = [self.kmers_to_numeric(kmers, kmer_size) for kmers in kmers_list]
        padded_sequences = pad_sequences(numeric_sequences, maxlen=max_len, padding='post')
        return np.array(padded_sequences)

    def predict(self, fna_file: bytes):
        X_new = self.preprocess_data(BytesIO(fna_file), 3, self.max_len)
        X_new_reshaped = X_new.reshape(-1, max_len, 1)

        predictions = self.cnn_model.predict(X_new_reshaped)
        predicted_classes = np.argmax(predictions, axis=1)

        return predicted_classes

def test():
    # Path to the new data file
    fna_file = "/path/to/new/gene_sequence.fna"  # Replace with your file
    kmer_size = 3
    max_len = 35546  # Use the same max_len as training

    # Load the model
    cnn_model = load_model("mutation_prediction_cnn.h5")

    # Preprocess the data
    X_new = preprocess_data(fna_file, kmer_size, max_len)
    X_new_reshaped = X_new.reshape(-1, max_len, 1)

    # Predict
    predictions = cnn_model.predict(X_new_reshaped)

    # Get class labels
    predicted_classes = np.argmax(predictions, axis=1)

    # Display results
    print("Predictions:", predictions)
    print("Predicted Classes:", predicted_classes)
