import gi
from gi.overrides import Gtk


if __name__ == '__main__':
    builder = Gtk.Builder()
    builder.add_from_file('testme.glade')

    # Register UI events with python methods here
    handlers = {
        "onDestroy": Gtk.main_quit
    }

    # The events are passed through this handlers dictionary for the builder to use
    builder.connect_signals(handlers)

    # Get a UI window object using the `id` attribute in the testme.glade file
    window = builder.get_object('window1')

    # UI methods and other callbacks can be found on the official documentation
    # https://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html
    window.show_all()

    # Load the Gtk UI application
    Gtk.main()