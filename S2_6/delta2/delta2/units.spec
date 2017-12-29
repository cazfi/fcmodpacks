
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

artists = "
  ngunjaca: boat, sail, diplomat, warriors
  GriffonSpade: lion
  Bebro, CapTVK (thomas@worldonline.nl), GriffonSpade: cyborg
  VladimirSlavik: Sea Constructor, Nuclear Submarine
  Clker-Free-Vector-Images: Balloon
"

[file]
gfx = "delta2/units"

[grid_main]

x_top_left   = 0
y_top_left   = 0
pixel_border = 1
dx      = 64
dy      = 48
tiles   = { "row", "column", "tag"
             0, 0, "u.lion"
             0, 1, "u.boat"
             0, 2, "u.sea_constructor"
             1, 0, "u.sail"
             1, 1, "u.cyborg"
             1, 2, "u.balloon"
             2, 0, "u.diplomat"
             2, 1, "u.warriors"
             2, 2, "u.nuclear_submarine"
          }

