import subprocess
import streamlit as st

# Path to the ts_sms binary
TS_SMS_BINARY = "./ts_sms-2024-12-26/ts_sms"

# Streamlit app title
st.title("TS_SMS Encrypt/Decrypt")

# Text input from the user
input_text = st.text_area("Enter text to encrypt/decrypt:")

# Buttons for actions
if st.button("Encrypt"):
    if input_text:
        try:
            # Run the ts_sms binary for encryption
            result = subprocess.run(
                [TS_SMS_BINARY, "c", input_text],
                capture_output=True,
                text=True,
            )
            st.success(f"Encrypted Text: {result.stdout.strip()}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text to encrypt.")

if st.button("Decrypt"):
    if input_text:
        try:
            # Run the ts_sms binary for decryption
            result = subprocess.run(
                [TS_SMS_BINARY, "d", input_text],
                capture_output=True,
                text=True,
            )
            st.success(f"Decrypted Text: {result.stdout.strip()}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text to decrypt.")
