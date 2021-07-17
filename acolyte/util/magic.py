from typing import Union
import subprocess
import magic

class Magic:
    # Map mimetypes to extensions
    # Adapted from apache httpd mime.types
    audio_extensions = {
        "audio/mp4": "m4a",
        "audio/mpeg": "mp3",
        "audio/ogg": "ogg",
        "audio/webm": "weba",
        "audio/x-aac": "aac",
        "audio/x-aiff": "aiff",
        "audio/x-flac": "flac",
        "audio/x-matroska": "mka",
        "audio/x-mpegurl": "m3u",
        "audio/x-ms-wma": "wma",
        "audio/x-wav": "wav",
        "audio/x-m4a": "m4a",
        "audio/x-hx-aac-adts": "aac"
    }

    image_extensions = {
        "image/bmp": "bmp",
        "image/gif": "gif",
        "image/jpeg": "jpeg",
        "image/png": "png",
        "image/svg+xml": "svg",
        "image/tiff": "tiff",
        "image/webp": "webp",
    }

    def __init__(self):
        self.libmagic = magic.Magic(mime=True)

    def __get_mime_type(self, bytes: bytes) -> str:
        """ Guess mimetype from magic bytes """
        return self.libmagic.from_buffer(bytes)

    def get_audio_extension(self, bytes: bytes) -> Union[str, None]:
        """ Get an audio extension from bytes """
        mimetype = self.__get_mime_type(bytes)

        if mimetype in self.audio_extensions:
            return self.audio_extensions[mimetype]

        return None

    def get_image_extension(self, bytes: bytes) -> Union[str, None]:
        """ Get an image extension from bytes """
        mimetype = self.__get_mime_type(bytes)

        if mimetype in self.image_extensions:
            return self.image_extensions[mimetype]

        return None

    def has_audio_track(self, bytes: bytes) -> bool:
        """ Detect audio tracks with ffprobe """
        process = subprocess.Popen(
            ["ffprobe"] +
            ["-loglevel", "panic"] +
            ["-select_streams", "a:0"] +
            ["-show_entries", "stream=codec_name"] +
            ["-of", "default=nokey=1:noprint_wrappers=1"] +
            ["-"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )

        output = process.communicate(input=bytes)[0].decode()

        return process.returncode == 0 and output != ''
