import os

__author__ = 'lennart'

from gi.repository import Gtk


class LevelEditor(object):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file(os.path.join("..", "..", "data", "ui", "leveleditor.glade"))
        self.window = builder.get_object("window1")
        self.toolbar = builder.get_object("toolbar1")
        self.window.show_all()
        builder.connect_signals(Handler())


class Handler(object):
    def __init__(self):
        pass

    def on_new_clicked(self, widget):
        print "New!"

    def on_save_clicked(self, widget):
        print "Save!"

if __name__ == "__main__":
    le = LevelEditor()
    Gtk.main()

