"""
Title: File Organizer Script

Description:
This Python script organizes image files (e.g., .png, .jpg, .jpeg, .webp) from specified directories on the C: and D: drives. It moves these files to designated folders for better file management.

Usage:
1. Run this script in a Python environment.
2. Ensure you have the required directories and file types set in the `crawler` function.
3. The script will identify image files in the specified directories, move them to new locations, and rename them as needed.

Author: XerXX9

Date: 20/08/2023
"""

# Import the os module for file and directory operations
import os

# Initialize empty lists to store file paths and names
original_path = []
file_name = []
final_path = []

def script():
    """
    Main function to organize image files from specified directories.
    """
    
    def crawler(parent):
        """
        Recursively traverse a directory tree and identify image files.

        Args:
            parent (str): The root directory to start the search from.
        """
        for root, dir, file in os.walk(parent):
            match root:
                case "C:Pictures" | "C:Pictures\Camera Roll" | "C:Pictures\Saved Pictures" | "C:Pictures\Screenshots":
                    # Skip specified directories for image organization
                    pass
                case _:
                    for x in file:
                        if x.endswith(".png")  or x.endswith(".jpg") or x.endswith(".jpeg") or x.endswith(".webp"):
                            original_path.append(root + "\\" + x)
                            file_name.append(x)

    def new_path(files):
        """
        Generate new file paths for moving image files to a target directory.

        Args:
            files (list): A list of file names to be moved.
        """
        target = "C:\\Users\\Admin\\Pictures\\Unsorted\\"
        for a in files:
            final = target + a
            final_path.append(final)   

    def new_path_d(files):
        """
        Generate new file paths for moving image files to a target directory on the D: drive.

        Args:
            files (list): A list of file names to be moved.
        """
        target = "D:\\Unsorted\\"
        for a in files:
            final = target + a
            final_path.append(final)   

    def replacer(op, fp):
        """
        Rename and move image files to their new locations on the C: drive.

        Args:
            op (list): Original file paths.
            fp (list): Final file paths.
        """
        for i in range(len(op)):
            os.rename(op[i], fp[i])

    def d_replacer(op, fp):
        """
        Rename and move image files to their new locations on the D: drive.

        Args:
            op (list): Original file paths.
            fp (list): Final file paths.
        """
        for i in range(len(op)):
            os.rename(op[i], fp[i])

    # Organize image files from specified directories on the C: drive
    crawler("C:Downloads")
    new_path(file_name)
    replacer(original_path, final_path)

    crawler("C:Desktop")
    new_path(file_name)
    replacer(original_path, final_path)

    # Organize image files from specified directory on the D: drive
    crawler("D:\Downloads_D")
    new_path_d(file_name)
    d_replacer(original_path, final_path)

# Run the script to organize image files
script()
