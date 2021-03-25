[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]

artists = "
    Jason Dorje Short <jdorje@freeciv.org>
	 Adaptation by Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "freeland/big/select"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 128
dy = 64
pixel_border = 0

tiles = { "row", "column", "tag"
  0, 0, "unit.select3"
  0, 1, "unit.select2"
  0, 2, "unit.select1"
  0, 3, "unit.select0"
}
