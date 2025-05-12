Secure Data Encryption System
A Streamlit-based application for securely storing and retrieving data using unique passkeys. Data is encrypted with Fernet, passkeys are hashed with SHA-256, and storage persists in a JSON file. The system enforces a three-attempt limit for decryption, redirecting to a login page after failures.
Features

Secure Storage: Encrypts user data with Fernet and stores it with a hashed passkey.
Data Retrieval: Decrypts data only with the correct passkey.
Attempt Limit: Locks access after three failed decryption attempts, requiring reauthorization.
Persistence: Stores encrypted data in a JSON file for session persistence.
User-Friendly UI: Streamlit interface with Home, Store Data, Retrieve Data, and Login pages.

Requirements

Python 3.6+: For running the application.
Dependencies:
streamlit: Web-based UI framework.
cryptography: For Fernet encryption/decryption.


No external database is required (uses JSON file for persistence).

Installation

Install Python (if not already installed):
Windows: Download from python.org. Check "Add Python to PATH".
macOS (Homebrew):brew install python


Ubuntu/Debian:sudo apt update && sudo apt install python3 python3-pip


Fedora:sudo dnf install python3




Install Dependencies:pip install streamlit cryptography


Verify Installation:python3 --version
pip show streamlit cryptography


Download the Code:
Save secure_data_system.py to a directory.



Usage

Navigate to the directory containing secure_data_system.py:cd /path/to/directory


Run the Streamlit app:streamlit run secure_data_system.py


Open the provided URL (e.g., http://localhost:8501) in a browser.
Use the interface:
Home: View app overview.
Store Data: Enter data and a passkey to encrypt and save. Copy the generated encrypted key.
Retrieve Data: Paste the encrypted key and enter the passkey to decrypt.
Login: Reauthorize with the master password (admin123) after three failed attempts.


Data is saved in stored_data.json for persistence across sessions.

Example

Store Data:
Input: Data = "My secret note", Passkey = "mykey123"
Output: Encrypted key (e.g., gAAAAAB...)
JSON file updated with encrypted data and hashed passkey.


Retrieve Data:
Input: Encrypted key, Passkey = "mykey123"
Output: "My secret note"
Incorrect passkey: Error and reduced attempts (locks after 3 failures).


Login:
Input: Master Password = "admin123"
Output: Reauthorized, redirects to Retrieve Data.



Project Structure

secure_data_system.py: Main application script.
stored_data.json: Auto-generated file for storing encrypted data.
README.md: This file with setup and usage instructions.

Security Notes

The master password (admin123) is hardcoded for demo purposes. In production, use a secure authentication system.
The Fernet key is generated per session for simplicity. In production, store it securely.
SHA-256 is used for passkey hashing. For enhanced security, consider PBKDF2 with a salt.

Contributing
Fork the repository, make improvements, and submit pull requests. Ideas for enhancements include multi-user support, time-based lockouts, or advanced hashing.
License
MIT License.
