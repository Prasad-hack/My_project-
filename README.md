# My_project-
Secure data hiding in images using stegnography

This project is a steganography-based application that allows users to securely hide and retrieve secret messages within images using a simple GUI built with Tkinter.

**Features**
- Load an image for embedding secret messages.
- Encrypt and hide a message inside an image using the Least Significant Bit (LSB) technique.
- Retrieve the hidden message from an encrypted image.
- Password protection for security.

**Requirements**
Make sure you have the following dependencies installed before running the application:

pip install opencv-python numpy pillow tkinter

**How to Use**

1. **Clone the Repository**
   git clone https://github.com/Prasad-hack/SECURE-DATA-HIDING-IN-IMAGES-USING-STEGANOGRAPHY.git
   cd steganography-project

2. **Run the Application**
   python steganography.py

3. **Usage**
   - Click on **Select Image** to choose an image.
   - Enter a secret message and a password.
   - Click **Encrypt** to hide the message inside the image.
   - Click **Decrypt** to retrieve the hidden message.

**File Structure**

├── steganography.py   # Main application script
├── pic.jpg            # Background image for GUI
├── encryptedImage.png # Encrypted image output (generated after encryption)
├── README.md          # Project documentation


**Encryption and Decryption Process**
- **Encryption:** The message is converted to binary and embedded into the pixel values of the image using the LSB technique.
- **Decryption:** The binary message is extracted from the image and converted back to text.

## License
This project is open-source and available under the MIT License.

## Author
VANAPALLI DURGA PRASAD

