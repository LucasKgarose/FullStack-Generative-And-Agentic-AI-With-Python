import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hey there, I am Kgarose!"

tokens = enc.encode(text)

# Prints Tokens [25216, 1354, 11, 357, 939, 658, 6802, 918, 0]
print("Tokens", tokens) 

# Decode
decoded_text = enc.decode([25216, 1354, 11, 357, 939, 658, 6702, 918, 0])

# Prints Decoded Text: Hey there, I am Kgarose!
print("Decoded Text:", decoded_text) 