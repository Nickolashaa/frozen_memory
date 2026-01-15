from faster_whisper import WhisperModel
import tempfile
import os


class VoiceToTextService:
    _model = None

    @classmethod
    def _get_model(cls):
        if cls._model is None:
            cls._model = WhisperModel("base", device="cpu", compute_type="int8")
        return cls._model

    @staticmethod
    def bytes_to_text(audio_bytes: bytes, language: str = "ru") -> str:
        temp_file_path = None

        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".ogg") as temp_file:
                temp_file.write(audio_bytes)
                temp_file_path = temp_file.name

            model = VoiceToTextService._get_model()

            segments, info = model.transcribe(
                temp_file_path, language=language, vad_filter=True, beam_size=5
            )

            segments_list = list(segments)

            text = " ".join([segment.text for segment in segments_list])

            return text

        except Exception as e:
            raise Exception(f"Error during transcription: {str(e)}")

        finally:
            if temp_file_path and os.path.exists(temp_file_path):
                os.remove(temp_file_path)
