
[spec]
options = "+Freeciv-spec-3.3-Devel-2023.Apr.05"

[info]
artists = "Xin Yu"

[file]
gfx = "chess/misc"

[grid_main]
x_top_left = 0
y_top_left = 0
dx = 60
dy = 60

tiles = { "row", "column", "tag"
0,  3, "ts.spice"
0,  4, "ts.furs"
0,  5, "ts.peat"
0,  6, "ts.arctic_ivory"
0,  7, "ts.seals"
0,  8, "ts.oasis"
0,  9, "ts.forest_game", "ts.tundra_game"
0, 10, "ts.oil", "ts.arctic_oil"
1,  3, "ts.fruit"
1,  4, "ts.iron"
1,  5, "ts.whales"
1,  6, "ts.wheat"
1,  7, "ts.grassland_resources", "ts.river_resources"
1,  8, "ts.coal"
1,  9, "ts.gems"
2,  3, "ts.pheasant"
2,  4, "ts.buffalo"
2,  5, "ts.silk"
2,  6, "ts.wine"
2,  7, "ts.gold"
2,  8, "ts.fish"
2,  9, "ts.horses"

0, 11, "tx.village"
0, 12, "base.fortress_bg"
1, 10, "base.airbase_mg"
6, 12, "base.buoy_mg"
7, 12, "extra.ruins_mg"
1, 11, "tx.mine"
1, 12, "tx.pollution"
2, 10, "tx.farmland"
2, 11, "tx.irrigation"
2, 12, "tx.fallout"
5, 10, "tx.fog"
5, 11, "mask.tile"

4,  0, "unit.vet_1"
4,  1, "unit.vet_2"
4,  2, "unit.vet_3"
4,  3, "unit.vet_4"
4,  4, "unit.vet_5"
4,  5, "unit.vet_6"
4,  6, "unit.vet_7"
4,  7, "unit.vet_8"
4,  8, "unit.vet_9"

5,  0, "upkeep.gold"
5,  1, "upkeep.gold2"
5,  2, "upkeep.food"
5,  3, "upkeep.food2"
5,  4, "upkeep.unhappy"
5,  5, "upkeep.unhappy2"
5,  6, "upkeep.shield"
5,  7, "unit.lowfuel", "unit.tired"
5,  8, "unit.loaded"

4,  9, "unit.stack"
4, 10, "unit.auto_attack", "unit.auto_settler"
4, 11, "unit.connect", "unit.convert"
4, 12, "unit.auto_explore"
3,  0, "unit.transform"
3,  1, "unit.sentry"
3,  2, "unit.goto"
3,  3, "unit.plant"
3,  4, "unit.pollution"
3,  5, "unit.road"
3,  6, "unit.cultivate",
       "unit.irrigate" ; For rulesets still using this tag
3,  7, "unit.fortifying", "unit.fortress"
3,  8, "unit.airbase"
3,  9, "unit.pillage"
3, 10, "unit.fortified"
3, 11, "unit.fallout"
3, 12, "unit.patrol"
5,  9, "user.attention", "user.infratile"

5,  9, "path.step"
5,  7, "path.exhausted_mp"
4, 12, "path.waypoint"

12,  0, "unit.hp_100"
12,  1, "unit.hp_90"
12,  2, "unit.hp_80"
12,  3, "unit.hp_70"
12,  4, "unit.hp_60"
12,  5, "unit.hp_50"
12,  6, "unit.hp_40"
12,  7, "unit.hp_30"
12,  8, "unit.hp_20"
12,  9, "unit.hp_10"
12, 10, "unit.hp_0"

6,  0, "city.size_0"
6,  1, "city.size_1"
6,  2, "city.size_2"
6,  3, "city.size_3"
6,  4, "city.size_4"
6,  5, "city.size_5"
6,  6, "city.size_6"
6,  7, "city.size_7"
6,  8, "city.size_8"
6,  9, "city.size_9"
7,  0, "city.size_00"
7,  1, "city.size_10"
7,  2, "city.size_20"
7,  3, "city.size_30"
7,  4, "city.size_40"
7,  5, "city.size_50"
7,  6, "city.size_60"
7,  7, "city.size_70"
7,  8, "city.size_80"
7,  9, "city.size_90"
8,  1, "city.size_100"
8,  2, "city.size_200"
8,  3, "city.size_300"
8,  4, "city.size_400"
8,  5, "city.size_500"
8,  6, "city.size_600"
8,  7, "city.size_700"
8,  8, "city.size_800"
8,  9, "city.size_900"

11,  0, "city.t_food_0"
11,  1, "city.t_food_1"
11,  2, "city.t_food_2"
11,  3, "city.t_food_3"
11,  4, "city.t_food_4"
11,  5, "city.t_food_5"
11,  6, "city.t_food_6"
11,  7, "city.t_food_7"
11,  8, "city.t_food_8"
11,  9, "city.t_food_9"

9,  0, "city.t_shields_0"
9,  1, "city.t_shields_1"
9,  2, "city.t_shields_2"
9,  3, "city.t_shields_3"
9,  4, "city.t_shields_4"
9,  5, "city.t_shields_5"
9,  6, "city.t_shields_6"
9,  7, "city.t_shields_7"
9,  8, "city.t_shields_8"
9,  9, "city.t_shields_9"

10,  0, "city.t_trade_0"
10,  1, "city.t_trade_1"
10,  2, "city.t_trade_2"
10,  3, "city.t_trade_3"
10,  4, "city.t_trade_4"
10,  5, "city.t_trade_5"
10,  6, "city.t_trade_6"
10,  7, "city.t_trade_7"
10,  8, "city.t_trade_8"
10,  9, "city.t_trade_9"
}

[grid_nuke]
x_top_left = 0
y_top_left = 0
dx = 180
dy = 180
tiles = { "row", "column", "tag"
0,  0, "explode.nuke"
}

