import gtk
from gtk import glade

class FtoC:
    def __init__(self):
        self.xml = glade.XML("ftoc.glade", None, None)
        self.xml.signal_connect("on_fahr_value_changed", self.on_spin_change)
        self.xml.signal_connect("on_window1_destroy", lambda w: gtk.main_quit())
        self.spin = self.xml.get_widget("fahr")
        self.result = self.xml.get_widget("celsius")

    def on_spin_change(self, w):
        fahr = self.spin.get_value_as_int();
        cent = (fahr - 32) / 1.8
        texto = "%.2f C" % cent
        self.result.set_label(texto)

if __name__ == "__main__":
    ftoc = FtoC()
    gtk.main()
