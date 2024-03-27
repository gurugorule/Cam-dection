#!/bin/bash

# Define the source directory
src_dir="./src"

# List of Python files to run
files=("Hand.py" "Face.py" "Body.py" "Motion.py")

# Function to display menu and get user choice
display_menu() {
    echo "Select a file to run:"
    for ((i=0; i<${#files[@]}; i++)); do
        echo "$(($i+1)). ${files[$i]}"
    done
    echo "0. Quit"
    read -p "Enter your choice: " choice
    echo $choice
}

# Loop to display menu and execute user's choice
while true; do
    choice=$(display_menu)
    case $choice in
        0)
            echo "Exiting..."
            exit 0
            ;;
        [1-4])
            selected_file=${files[$(($choice-1))]}
            if [ -f "$src_dir/$selected_file" ]; then
                echo "Running $selected_file..."
                python "$src_dir/$selected_file"
            else
                echo "File $selected_file not found."
            fi
            ;;
        *)
            echo "Invalid choice. Please enter a number between 0 and 4."
            ;;
    esac
done
