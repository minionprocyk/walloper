import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from operationv.GlobalSettings import MAIN_WINDOW_TITLE


class MainWindow(object):

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('main_ui.glade')

        # The events are passed through this handlers dictionary for the builder to use
        builder.connect_signals(self)

        # Get UI objects using the `id` attribute in the main_ui.glade file
        self.window = builder.get_object('main_app')

        # UI methods and other callbacks can be found on the official documentation
        # https://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html
        self.window.show_all()
        self.window.set_title(MAIN_WINDOW_TITLE)
        # Load the Gtk UI application
        Gtk.main()

    def on_main_app_destroy(self, widget):
        Gtk.main_quit()

    def on_file_quit(self, widget):
        Gtk.main_quit()

    def on_btnRun_clicked(self, txt_buffer):
        print("got run button clicked {} ".format(txt_buffer))
        txt_buffer.set_text('helo\nnextline'*22)

    def on_btnStop_clicked(self, widget):
        print("got stop button clicked")


if __name__ == '__main__':
    MainWindow()


