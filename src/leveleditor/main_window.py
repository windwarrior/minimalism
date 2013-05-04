import os, glob, json

__author__ = 'lennart'

from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf
from tile_data import TileData


class LevelEditor(object):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file(os.path.join("..", "..", "data", "ui", "leveleditor.glade"))
        self.data_dir = os.path.join("..", "..", "data", "leveleditor")
        self.window = builder.get_object("window1")
        self.toolbar = builder.get_object("toolbar1")
        self.tilestore = builder.get_object("tilestore")
        self.tileview = builder.get_object("iconview1")
        self.tileview.set_model(self.tilestore)
        self.tileview.set_pixbuf_column(0)
        self.layerstore = builder.get_object("layerstore")
        self.level_view = builder.get_object("drawingarea1")
        self.level_view.set_size_request( 700, 700 );
        self.window.show_all()

        self.populate_with_data()

        builder.connect_signals(Handler())

    def populate_with_data(self):
        for floc in glob.glob(os.path.join(self.data_dir, "tiles", "*.json")):
            f = json.load(open(floc))
            td = TileData(f["solid"], f["visible"], f["name"], f["icon"])
            pb = Pixbuf.new_from_file_at_size(os.path.join(self.data_dir, "icons", f["icon"]), 64, 64)
            self.tilestore.append([pb, td])

class Handler(object):
    def __init__(self):
        pass

    def on_new_clicked(self, widget):
        print "New!"

    def on_save_clicked(self, widget):
        print "Save!"

    def on_save_as_clicked(self, widget):
        print "Save As!"

    def on_open_clicked(self, widget):
        print "Open!"

    def draw_level(self, widget, cairo_context):
        cairo_context.move_to(50, 50)
        cairo_context.rel_line_to(0, 200)
        cairo_context.rel_line_to(200, 0)
        cairo_context.rel_line_to(0, -200)
        cairo_context.set_source_rgb(0, 0, 0)
        cairo_context.stroke()

if __name__ == "__main__":
    le = LevelEditor()
    Gtk.main()

