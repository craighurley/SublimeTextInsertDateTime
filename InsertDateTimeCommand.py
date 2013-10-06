import sublime
import sublime_plugin
import time

format_datetime_iso     = "%Y%m%d%H%M%S"
format_datetime_human   = "%H:%M:%S %d/%m/%Y"
format_date_human       = "%d/%m/%Y"

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
        sublime.status_message("Inserted ISO date time")

class InsertDateTimeHumanCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get the date time
        dt = time.strftime(format_datetime_human);

        # paste the datetime at each selection point
        for cursors in self.view.sel():
            self.view.replace(edit, cursors, dt)

        # copy the last datetime to the clipboard
        sublime.set_clipboard(dt)

        # update the status message
        sublime.status_message("Inserted human date time")

class InsertDateHumanCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get the date time
        dt = time.strftime(format_date_human);

        # paste the datetime at each selection point
        for cursors in self.view.sel():
            self.view.replace(edit, cursors, dt)

        # copy the last datetime to the clipboard
        sublime.set_clipboard(dt)

        # update the status message
        sublime.status_message("Inserted human date")
