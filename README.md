Here's a GitHub README file for your Python script that processes files or folders, including colored output and EXIF data manipulation:

---

# File Processor & EXIF Tool 🗂️✨

A Python script to interactively process files or folders, allowing you to read, write, or remove EXIF metadata. The script features colored terminal output and a simple interface to streamline the task of managing file metadata.

## Features ✨

- **Interactive File Processing:** Choose to read, write, or remove EXIF data from files.
- **Folder Support:** Recursively processes all files within a given folder.
- **Colored Output:** Highlights messages in different colors to enhance readability.
- **Cross-Platform Compatibility:** Works on both Windows and Unix-based systems.

## Prerequisites 📦

- **Python 3.x**: Ensure Python is installed on your machine.
- **ExifTool**: The script relies on `ExifTool` to manage EXIF metadata. You can install it [here](https://exiftool.org/).

## How to Use 🛠️

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hu5o-dev/MetadataTool.git
   cd MetadataTool
   ```

2. **Install Required Packages:**

   The script uses no external libraries beyond `ExifTool`. Ensure it is installed and accessible in your system's PATH.

3. **Run the Script:**

   Execute the script from your terminal:

   ```bash
   python MetaToolV2.py
   ```

4. **Input Files or Folders:**

   - When prompted, enter the file names or folder paths you want to process, separated by commas.
   - For each file, choose whether to read, write, or remove EXIF metadata.

5. **EXIF Options:**

   - **Read**: Displays the file's EXIF metadata.
   - **Write**: Adds or updates the copyright notice in the file's EXIF data.
   - **Remove**: Removes all EXIF metadata from the file.

6. **Repeat or Exit:**

   After processing, you can choose to process more files or exit the script.

## Example Output 📸

When running the script, you'll see colorful output guiding you through the options:

```bash
Enter the file names or folder path (separated by comma):
> sample.jpg
File: "sample.jpg"
------------------------------
1. Read
2. Write
3. Remove
------------------------------
Enter your option:
```

## Customization 🛠️

- **Typing Speed:** Adjust the `typing_speed` parameter in `print_colored_typing` to change the speed of the text animation.
- **Color Codes:** Modify the color codes in `print_colored_typing` to customize the appearance of different messages.

## Troubleshooting 🛠️

- **ExifTool Not Found:** Ensure `ExifTool` is installed and accessible in your system's PATH.
- **Invalid File Paths:** Double-check the paths you enter for typos or errors.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributions 🤝

Contributions are welcome! Feel free to fork this repository, submit a pull request, or open an issue if you have any suggestions or improvements.

## Acknowledgments 🙌

- Thanks to the developers of `ExifTool` for providing such a robust tool for managing EXIF data.

---

Feel free to update the URLs, placeholders, and any other details as necessary!
