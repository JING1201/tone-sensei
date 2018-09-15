def transcribe_gcs(gcs_uri):
    """Transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.aRecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='cmn-Hans-CN')

    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))

    return result.alternatives[0].transcript #returns the first alternative of the pronunciation

def text_to_tone (transcript):
    import pinyin
    pronunciation = pinyin.get(transcript, format="numerical")
    tones = [c for c in pronunciation if c.isDigit()]
    return tones

#to tell users what they said
def text_to_pinyin (transcript):
    import pinyin
    return pinyin.get(transcript)
