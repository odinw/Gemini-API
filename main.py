from google import genai

client = genai.Client(api_key="your_api_key")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="如何保持正面思考，請用正體中文回覆",
)

print(response.text)