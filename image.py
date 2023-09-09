import openai

openai.api_key = "EU9hJ8jjL4ZlK1TIUGYxXPyKKgI2FfpPoKx30JEw4BY"
openai.api_base = "https://chimeragpt.adventblocks.cc/api/v1"

response = openai.Image.create(
    model="stable-diffusion-2.1",
    prompt="Chinese little girl at the seaside.",
    n=3,  # images count
    size="1024x1024"
)

print(response["data"])
