#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from future import standard_library

standard_library.install_aliases()
from chiplotle import *
from chiplotle.tools.io.import_hpgl_file import import_hpgl_file
from chiplotle.tools.plottertools import instantiate_virtual_plotter

import time


def main():

    print("Importing ./Flensburg.hpgl")
    f = import_hpgl_file("./Flensburg.hpgl")

    print(
        "Here are the contents of the file, expanded into a list of chiplotle objects:"
    )
    print(f)

    print("\nAnd here are the raw hpgl commands:")

    for c in f:
        print(c.format)

    # We can use io.view() to take a look...
    io.view(f)

    # small delay to give our external postscript reader time to
    # load the output file
    time.sleep(1)

    # We can also send the commands to a plotter.
    # We'll use a virtual plotter in this example:
    # plotter = instantiate_virtual_plotter()
    
    plotter = instantiate_plotters()[0]

    # Now we'll send the contents of the file to the plotter
    # so we can take a look.
    plotter.write(f)

if __name__ == "__main__":
    main()

