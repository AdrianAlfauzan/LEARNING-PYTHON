# Install versi terbaru dari pustaka OpenAI
# pip install openai

import openai

# Ganti dengan kunci API Anda
openai.api_key = "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"


def generate_text(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  # Gunakan model GPT-3 terbaru
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


user_input = (
    "Buatkan saya cerita fiksi tentang dunia di mana mesin waktu nyata berhasil dibuat."
)
generated_story = generate_text(user_input)
print(generated_story)
