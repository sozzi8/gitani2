
def det_lan(song):
    """Detects the text's language."""
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    result = translate_client.detect_language(song)

    print("Language: {}".format(result["language"]))
