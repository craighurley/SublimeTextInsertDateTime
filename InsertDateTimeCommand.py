import sublime
import sublime_plugin
import time

format_datetime_iso     = "%Y%m%d%H%M%S"
format_datetime         = "%d/%m/%Y %H:%M:%S"
format_timedate         = "%H:%M:%S %d/%m/%Y"
format_date             = "%d/%m/%Y"

class InsertDateTimeIsoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get the date time
        dt = time.strftime(format_datetime_iso);

        # paste the datetime at each selection point
        for cursors in self.view.sel():            
            self.view.replace(edit, cursors, dt)

        # copy the last datetime to the clipboard
        sublime.set_clipboard(dt)

        # update the status message
        sublime.status_message("Inserted date time ISO")

class InsertDateTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get the date time
        dt = time.strftime(format_datetime);

        # paste the datetime at each selection point
        for cursors in self.view.sel():
            self.view.replace(edit, cursors, dt)

        # copy the last datetime to the clipboard
        sublime.set_clipboard(dt)

        # update the status message
        sublime.status_message("Inserted date time")

class InsertTimeDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get the date time
        dt = time.strftime(format_timedate);

        # paste the datetime at each selection point
        for cursors in self.view.sel():
            self.view.replace(edit, cursors, dt)

        # copy the last datetime to the clipboard
        sublime.set_clipboard(dt)

        # update the status message
        sublime.status_message("Inserted time date")

class InsertDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get the date time
        dt = time.strftime(format_date);

        # paste the datetime at each selection point
        for cursors in self.view.sel():
            self.view.replace(edit, cursors, dt)

        # copy the last datetime to the clipboard
        sublime.set_clipboard(dt)

        # update the status message
        sublime.status_message("Inserted date")
