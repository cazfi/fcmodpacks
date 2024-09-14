
[spec]

; Format and options of this spec file:
options = "+Freeciv-3.2-spec"

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

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"

  0,  0, "u.lion_Idle"
  0,  1, "u.boat_Idle"
  0,  2, "u.sea_constructor_Idle"
  0,  3, "u.sail_Idle"

  1,  0, "u.cyborg_Idle"
  1,  1, "u.balloon_Idle"
  1,  2, "u.diplomat_Idle"
  1,  3, "u.warriors_Idle"

  2,  0, "u.nuclear_submarine_Idle"
}
