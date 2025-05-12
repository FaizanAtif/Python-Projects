import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Blacklist common passwords
    common_passwords = ["password", "password123", "123456", "qwerty", "admin"]
    if password.lower() in common_passwords:
        return 0, ["❌ Password is too common. Choose a unique password."]
    
    # Length Check (weight: 1.5 for added importance)
    if len(password) >= 8:
        score += 1.5
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check (weight: 1)
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check (weight: 1)
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check (weight: 1.5 for added security)
    if re.search(r"[!@#$%^&*]", password):
        score += 1.5
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Determine strength based on score
    if score >= 5:
        strength = "Strong"
        feedback.append("✅ Strong Password! You're good to go.")
    elif score >= 3:
        strength = "Moderate"
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        strength = "Weak"
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")
    
    return score, feedback

def generate_strong_password(length=12):
    if length < 8:
        length = 8  # Enforce minimum length
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]
    password += [random.choice(characters) for _ in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Password Strength Meter")
    password = input("Enter your password (or type 'generate' for a suggestion): ").strip()
    
    if password.lower() == 'generate':
        new_password = generate_strong_password()
        print(f"Generated Password: {new_password}")
        score, feedback = check_password_strength(new_password)
    else:
        score, feedback = check_password_strength(password)
    
    # Display results
    print("\nResults:")
    for msg in feedback:
        print(msg)
    print(f"Score: {score:.1f}/5.0")

if __name__ == "__main__":
    main()