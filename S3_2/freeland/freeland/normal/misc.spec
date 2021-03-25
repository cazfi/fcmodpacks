
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]

artists = "
	 Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "freeland/normal/misc"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 64
dy = 32
pixel_border = 0

tiles = { "row", "column","tag"
  0, 0, "tx.darkness"
  0, 0, "t.dither_tile"
  0, 2, "mask.tile"
  0, 3, "tx.fog"
  1, 0, "t.l0.ocean1"
}

