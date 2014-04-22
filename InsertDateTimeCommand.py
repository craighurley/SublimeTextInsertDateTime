import sublime
import sublime_plugin
import time

format_date             = "%d/%m/%Y"
format_datetime         = "%d/%m/%Y %H:%M:%S"
format_time             = "%H:%M:%S"
format_timedate         = "%H:%M:%S %d/%m/%Y"
format_datetime_xml     = "%Y-%m-%dT%H:%M:%S"
format_datetime_iso     = "%Y%m%d%H%M%S"

class InsertDateCommand(sublime_plugin.TextCommand):
    def on_done(self, index):
        # if cancelled, index is returned as -1
        if index == -1:
            return

        # if user picks from list, return the correct entry
        self.view.run_command("insert_text", {"args":{'text': self.list[index]}})

    def run(self, edit):
        self.list = [time.strftime(format_date), 
                    time.strftime(format_datetime),
                    time.strftime(format_time),
                    time.strftime(format_timedate),
                    time.strftime(format_datetime_xml),
                    time.strftime(format_datetime_iso)]

        self.view.window().show_quick_panel(self.list, self.on_done, 1, 0)

class InsertTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, args):
        for cursors in self.view.sel():
            self.view.replace(edit, cursors, args['text'])

        # copy the last datetime to the clipboard
        sublime.set_clipboard(args['text'])

        # update the status message
        sublime.status_message("Inserted text")
