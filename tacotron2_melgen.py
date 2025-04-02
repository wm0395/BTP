import torch
import csv
import os
import numpy as np
from nemo.collections.tts.helpers import text_to_sequence
from torch.hub import load

# Check if GPU is available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

# Load Tacotron2 model from PyTorch Hub
try:
    tacotron2 = load('nvidia/DeepLearningExamples:torchhub', 'nvidia_tacotron2').to(device)
    tacotron2.eval()
    print("Tacotron2 model loaded successfully.")
except Exception as e:
    print(f"Error loading Tacotron2 model: {e}")
    exit(1)

# File paths
input_csv = '/home/wm0395/BTP/Dataset/metadata.csv'
output_dir = '/home/wm0395/BTP/Dataset/mels'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to convert text to mel spectrogram
def text_to_mel(text, model):
    try:
        sequence = torch.tensor(text_to_sequence(text, ['english_cleaners']), dtype=torch.long).unsqueeze(0).to(device)
        with torch.no_grad():
            mel_outputs, _, _ = model.infer(sequence)
        return mel_outputs.squeeze(0).cpu().numpy()
    except Exception as e:
        print(f"Error generating mel spectrogram for text '{text}': {e}")
        return None

# Read text from CSV and generate mel spectrograms
with open(input_csv, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
        if len(row) < 2:
            continue  # Skip rows without sufficient data
        filename = row[0].strip()  # Use the first column as the filename
        text = row[1].strip()      # Use the second column as the text input

        if not text:
            print(f"Skipping empty text entry for file: {filename}")
            continue

        # Generate mel spectrogram
        mel_spectrogram = text_to_mel(text, tacotron2)

        if mel_spectrogram is not None:
            # Save mel spectrogram as a .npy file
            output_path = os.path.join(output_dir, f"{filename}.npy")
            np.save(output_path, mel_spectrogram)
            print(f"Saved mel spectrogram for '{text}' to {output_path}")
        else:
            print(f"Failed to generate mel spectrogram for '{text}'")
