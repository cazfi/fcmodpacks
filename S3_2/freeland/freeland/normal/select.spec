[spec]

; Format and options of this spec file:
options = "+Freeciv-3.2-spec"

[info]

artists = "
    Jason Dorje Short <jdorje@freeciv.org>
	 Adaptation by Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "freeland/normal/select"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 64
dy = 32
pixel_border = 0

tiles = { "row", "column", "tag"
  0, 0, "unit.select3"
  0, 1, "unit.select2"
  0, 2, "unit.select1"
  0, 3, "unit.select0"
}
