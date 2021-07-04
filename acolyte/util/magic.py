from typing import Union
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
        return self.libmagic.from_buffer(bytes)

    def get_audio_extension(self, bytes: bytes) -> Union[str, None]:
        mimetype = self.__get_mime_type(bytes)

        if mimetype in self.audio_extensions:
            return self.audio_extensions[mimetype]

        return None

    def get_image_extension(self, bytes: bytes) -> Union[str, None]:
        mimetype = self.__get_mime_type(bytes)

        if mimetype in self.image_extensions:
            return self.image_extensions[mimetype]

        return None
