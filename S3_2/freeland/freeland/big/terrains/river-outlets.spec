
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]

artists = "
	 Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "freeland/big/terrains/river-outlets"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 128
dy = 64
pixel_border = 0

tiles = { "row", "column","tag"
 0, 0, "road.river_outlet_n"
 0, 1, "road.river_outlet_e"
 0, 2, "road.river_outlet_s"
 0, 3, "road.river_outlet_w"
}
