import google.generativeai as genai

# Use your key safely
genai.configure(api_key="AIzaSyB2IddMajaRCJ9U4SBIQ_hs-kE7gdp7hSk")  # replace YOUR_NEW_KEY with the regenerated key

# List available models
models = genai.list_models()
for m in models:
    print(m.name, m.description)
