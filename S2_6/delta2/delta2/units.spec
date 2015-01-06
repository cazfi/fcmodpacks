
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-Devel-2013.Feb.13"

[info]

artists = "
  ngunjaca (boat, sail, diplomat, warriors)
  GriffonSpade (lion)
"

[file]
gfx = "delta2/units"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"

  0,  0, "u.lion"
  0,  1, "u.boat"

  0,  3, "u.sail"

  1,  2, "u.diplomat"
  1,  3, "u.warriors"
}
