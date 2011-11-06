import sublime
import sublime_plugin

from gist import create


class UploadToGistCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            try:
                url = create([self.view.file_name()])
                sublime.set_clipboard(url.strip())
                sublime.status_message("Copied URL to clipboard")
            except Exception, e:
                print e
                sublime.status_message("Unable to upload file")

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0
