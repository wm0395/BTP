#!/bin/bash

# filepath: /home/wm0395/BTP/wav2mel/run_wav2mel.sh

# Input directory containing .wav files
INPUT_DIR=$1

# Check if input directory is provided
if [ -z "$INPUT_DIR" ]; then
    echo "Usage: $0 <input_directory>"
    exit 1
fi

# Check if the input directory exists
if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Directory $INPUT_DIR does not exist."
    exit 1
fi

# Process each .wav file in the input directory
for wav_file in "$INPUT_DIR"/*.wav; do
    # Skip if no .wav files are found
    if [ ! -e "$wav_file" ]; then
        echo "No .wav files found in $INPUT_DIR."
        exit 1
    fi

    # Generate output .mel file name
    mel_file="${wav_file%.wav}.mel"

    # Run wav2mel
    echo "Processing $wav_file -> $mel_file"
    wav2mel < "$wav_file" > "$mel_file"

    # Check if wav2mel succeeded
    if [ $? -ne 0 ]; then
        echo "Error processing $wav_file"
        exit 1
    fi
done

echo "All .wav files processed successfully."