import sublime
import sublime_plugin

from gist import create

settings = sublime.load_settings('upload-to-gist.sublime-settings')


class UploadToGistCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            try:
                url = create([self.view.file_name()],
                    public=settings.get('public', None),
                    description=settings.get('description', None),
                    login=settings.get('login', None),
                    token=settings.get('token', None))
                sublime.set_clipboard(url.strip())
                sublime.status_message("Copied URL to clipboard")
            except Exception, e:
                print e
                sublime.status_message("Unable to upload file: " + str(e))

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0
