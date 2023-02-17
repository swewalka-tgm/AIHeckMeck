import whisper

model = whisper.load_model("small")

# We can pass in a filename or a tensor (PyTorch or numpy).
result = model.transcribe("./samples/audio2.wav")

# Print the transcript.
print(result["text"])
