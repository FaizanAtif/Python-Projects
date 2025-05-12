import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import json
import os

# Initialize session state
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = True

# Generate Fernet key (in production, store securely)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# JSON file for persistence
DATA_FILE = "stored_data.json"

# Load stored data from JSON
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

# Save stored data to JSON
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Initialize in-memory storage
stored_data = load_data()

# Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Function to encrypt data
def encrypt_data(text, passkey):
    encrypted_text = cipher.encrypt(text.encode()).decode()
    return encrypted_text

# Function to decrypt data
def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)
    
    if encrypted_text in stored_data and stored_data[encrypted_text]["passkey"] == hashed_passkey:
        st.session_state.failed_attempts = 0
        return cipher.decrypt(encrypted_text.encode()).decode()
    
    st.session_state.failed_attempts += 1
    return None

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

# Navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")
    st.info("Navigate to 'Store Data' to save encrypted data or 'Retrieve Data' to access it.")

elif choice == "Store Data":
    if not st.session_state.authenticated:
        st.warning("🔒 Please reauthorize in the Login page.")
    else:
        st.subheader("📂 Store Data Securely")
        user_data = st.text_area("Enter Data:", height=100)
        passkey = st.text_input("Enter Passkey:", type="password")

        if st.button("Encrypt & Save"):
            if user_data and passkey:
                hashed_passkey = hash_passkey(passkey)
                encrypted_text = encrypt_data(user_data, passkey)
                stored_data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
                save_data(stored_data)
                st.success("✅ Data stored securely!")
                st.write("Copy this encrypted key for retrieval:")
                st.code(encrypted_text)
            else:
                st.error("⚠️ Both data and passkey are required!")

elif choice == "Retrieve Data":
    if not st.session_state.authenticated:
        st.warning("🔒 Please reauthorize in the Login page.")
    else:
        st.subheader("🔍 Retrieve Your Data")
        encrypted_text = st.text_area("Enter Encrypted Key:", height=100)
        passkey = st.text_input("Enter Passkey:", type="password")

        if st.button("Decrypt"):
            if encrypted_text and passkey:
                decrypted_text = decrypt_data(encrypted_text, passkey)

                if decrypted_text:
                    st.success(f"✅ Decrypted Data: {decrypted_text}")
                else:
                    st.error(f"❌ Incorrect passkey or key! Attempts remaining: {3 - st.session_state.failed_attempts}")
                    
                    if st.session_state.failed_attempts >= 3:
                        st.session_state.authenticated = False
                        st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                        st.experimental_rerun()
            else:
                st.error("⚠️ Both encrypted key and passkey are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password", help="Default: admin123")

    if st.button("Login"):
        if login_pass == "admin123":  # Hardcoded for demo; replace with secure auth in production
            st.session_state.authenticated = True
            st.session_state.failed_attempts = 0
            st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data...")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password!")