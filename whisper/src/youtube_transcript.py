from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

YouTubeTranscriptApi.get_transcript("j2mXlzOZ4V4")

transcript = YouTubeTranscriptApi.get_transcript("j2mXlzOZ4V4")

formatter = TextFormatter()

formatted = formatter.format_transcript(transcript)

print(formatted)


