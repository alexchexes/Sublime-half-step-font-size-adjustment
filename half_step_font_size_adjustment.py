import sublime
import sublime_plugin


def changeFontSizeBy(value):
    current_font_size = sublime.load_settings("Preferences.sublime-settings").get('font_size')
    new_font_size = current_font_size + value
    settings = sublime.load_settings("Preferences.sublime-settings")
    settings.set('font_size', new_font_size)
    sublime.save_settings("Preferences.sublime-settings")
    sublime.set_timeout(lambda: sublime.status_message('New font size: ' + str(new_font_size)), 0)


class IncreaseFontSizeHalfStepCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        changeFontSizeBy(0.5)


class DecreaseFontSizeHalfStepCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        changeFontSizeBy(-0.5)
