[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-3.3-Devel-2023.Apr.05"

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
  0, 0, "unit.select:3"
  0, 1, "unit.select:2"
  0, 2, "unit.select:1"
  0, 3, "unit.select:0"
}
