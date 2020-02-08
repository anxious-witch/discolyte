from watchdog.events import FileSystemEventHandler
from watchdog.events import FileModifiedEvent
import os
import time

class FileHandler(FileSystemEventHandler):
    def __init__(self, bot):
        FileSystemEventHandler.__init__(self)
        self.bot = bot
        self.queued_events = set()
        self.path_seperator = os.path.sep

    def on_modified(self, event):
        filename = event.src_path.split(self.path_seperator)[-1]

        # Don't care about dir events
        if not isinstance(event, FileModifiedEvent):
            return

        file, file_extension = filename[:-3], filename[-3::]

        if file_extension == '.py':
            self.queued_events.add(file)

        # Sleep for 50ms because watchdog triggers multiple events
        time.sleep(0.05)

        self.fire_extension_reload(file)

    def fire_extension_reload(self, extension_name):
        """
            Check if the event is in the queued events
            If it's not in the queued events,
            it means the event has already been fired
        """

        if extension_name not in self.queued_events:
            return

        self.queued_events.remove(extension_name)
        self.bot.reload_extension(extension_name)
