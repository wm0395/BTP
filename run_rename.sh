#!/bin/bash

# filepath: /home/wm0395/BTP/wav2mel/rename_mel_to_npy.sh

# Input directory containing .mel files
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

# Rename all .mel files to .npy
for mel_file in "$INPUT_DIR"/*.mel; do
    # Skip if no .mel files are found
    if [ ! -e "$mel_file" ]; then
        echo "No .mel files found in $INPUT_DIR."
        exit 1
    fi

    # Generate new file name with .npy extension
    npy_file="${mel_file%.mel}.npy"

    # Rename the file
    echo "Renaming $mel_file -> $npy_file"
    mv "$mel_file" "$npy_file"

    # Check if renaming succeeded
    if [ $? -ne 0 ]; then
        echo "Error renaming $mel_file"
        exit 1
    fi
done

echo "All .mel files renamed to .npy successfully."