import sublime
import sublime_plugin

default_font_size = 11.5


class IncreaseFontSizeHalfStepCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        changeFontSizeBy(0.5)


class DecreaseFontSizeHalfStepCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        changeFontSizeBy(-0.5)


class ResetFontSizeToDefaultCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        saveSettingsFontSize(default_font_size)
        sublime.status_message('Font size was reset to: ' + str(default_font_size))


def changeFontSizeBy(value):
    current_font_size = getSettingsFontSize()
    new_font_size = current_font_size + value
    saveSettingsFontSize(new_font_size)
    sublime.set_timeout(lambda: sublime.status_message('New font size: ' + str(new_font_size)), 0)


def getSettingsFontSize():
    return sublime.load_settings("Preferences.sublime-settings").get('font_size')


def saveSettingsFontSize(new_font_size):
    settings = sublime.load_settings("Preferences.sublime-settings")
    settings.set('font_size', new_font_size)
    sublime.save_settings("Preferences.sublime-settings")
