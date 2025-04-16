import streamlit as st
import re

# Set page config for better aesthetics
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stTextInput>div>div>input {
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# 🎉 Title with Emoji
st.markdown("<h1 style='text-align: center; color: #4a4a4a;'>🔐 Ultimate Password Strength Checker</h1>", unsafe_allow_html=True)

# 📝 Description
st.markdown("""
<div style='text-align: center; font-size: 18px;'>
    🔎 Check your password's strength using the following criteria:
    <ul style='list-style-type: none; padding-left: 0;'>
        <li>✅ Minimum <b>8 characters</b></li>
        <li>🔤 Includes <b>uppercase and lowercase</b> letters</li>
        <li>🔢 Contains at least <b>one number</b></li>
        <li>💥 Has at least <b>one special character</b> (!@#$%^&*)</li>
    </ul>
    <i>💡 Pro tip: Use a mix of all to make your password unbreakable!</i>
</div>
""", unsafe_allow_html=True)

# 🏷️ Input Field
st.markdown("### 🔑 Enter your password below:")
password = st.text_input("", type="password", placeholder="Type your password here...")

# 🔍 Password Strength Logic
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase and lowercase** letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least **one number (0-9)**.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least **one special character (!@#$%^&*)**.")

    return score, feedback

# ✅ Button to Check Password
if st.button("🔍 Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        st.markdown("### 🔒 Password Strength Result:")

        if score == 4:
            st.success("✅ Strong Password! Your password is secure and well-protected.")
        elif score == 3:
            st.warning("⚠️ Moderate Password - You're almost there! Strengthen it a bit more.")
        else:
            st.error("❌ Weak Password - Try improving it using the suggestions below.")

        if feedback:
            st.markdown("### 💡 Suggestions to Improve:")
            for tip in feedback:
                st.markdown(f"- {tip}")
    else:
        st.error("🚨 Please enter a password to check.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color: gray;'>🔐 Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
