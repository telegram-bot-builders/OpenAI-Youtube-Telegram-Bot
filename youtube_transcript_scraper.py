from youtube_transcript_api import YouTubeTranscriptApi
import pprint

video_id = "ZcBJwyCPUHU"

transcript = YouTubeTranscriptApi.get_transcript(video_id)

pprint.pprint(transcript)