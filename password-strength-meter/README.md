Password Strength Meter
A Python-based tool to evaluate password strength based on security criteria, provide feedback, and generate strong passwords.
Features

Password Evaluation: Analyzes passwords based on length, character types (uppercase, lowercase, digits, special characters), and patterns.
Scoring System: Assigns a strength score (Weak, Moderate, Strong) with custom weights for complexity factors.
Feedback System: Provides detailed suggestions for improving weak passwords.
Password Generator: Generates secure, random passwords meeting all strength criteria.
Blacklist Check: Rejects common passwords like "password123" or "qwerty".

Requirements

Python 3.6+: The program uses standard Python libraries (re, random, string).
No external dependencies are required.

Installation

Install Python (if not already installed):
Windows: Download from python.org. Ensure "Add Python to PATH" is checked.
macOS (via Homebrew):brew install python


Ubuntu/Debian:sudo apt update && sudo apt install python3 python3-pip


Fedora:sudo dnf install python3




Verify Python Installation:python3 --version


Download the Code:
Save password_strength_meter.py to a directory of your choice.



Usage

Navigate to the directory containing password_strength_meter.py:cd /path/to/directory


Run the program:python3 password_strength_meter.py


Follow the prompts:
Enter a password to evaluate its strength.
Type generate to receive a randomly generated strong password.


Review the output, which includes:
Strength rating (Weak, Moderate, Strong).
Feedback for improvement.
A numerical score out of 5.0.



Example
Password Strength Meter
Enter your password (or type 'generate' for a suggestion): password123
Results:
❌ Password is too common. Choose a unique password.
Score: 0.0/5.0

Password Strength Meter
Enter your password (or type 'generate' for a suggestion): generate
Generated Password: kJ#9mP2nL$5x
Results:
✅ Strong Password! You're good to go.
Score: 5.0/5.0

Project Structure

password_strength_meter.py: Main script containing the password strength logic and generator.
README.md: This file, providing setup and usage instructions.

Contributing
Feel free to fork the repository, make improvements, and submit pull requests. Suggestions for additional features (e.g., GUI with Streamlit, advanced pattern checks) are welcome!
License
This project is licensed under the MIT License.
