[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

artists = "
	 Peter Arbor <peter.arbor@gmail.com>
"

[file]
gfx = "freeland/big/terrains/s"

[grid_main]

x_top_left = 0
y_top_left = 0
dx = 128
dy = 64
pixel_border = 0

tiles = { "row", "column", "tag"
0,0, "t.l0.cellgroup_s_s_s_s", "t.l0.floor1"
0,1, "t.l0.cellgroup_s_s_s_g"
0,2, "t.l0.cellgroup_s_s_s_p"
0,3, "t.l0.cellgroup_s_s_s_d"
0,4, "t.l0.cellgroup_s_s_s_t"
0,5, "t.l0.cellgroup_s_s_s_a"
1,0, "t.l0.cellgroup_s_s_g_s"
1,1, "t.l0.cellgroup_s_s_g_g"
1,2, "t.l0.cellgroup_s_s_g_p"
1,3, "t.l0.cellgroup_s_s_g_d"
1,4, "t.l0.cellgroup_s_s_g_t"
1,5, "t.l0.cellgroup_s_s_g_a"
2,0, "t.l0.cellgroup_s_s_p_s"
2,1, "t.l0.cellgroup_s_s_p_g"
2,2, "t.l0.cellgroup_s_s_p_p"
2,3, "t.l0.cellgroup_s_s_p_d"
2,4, "t.l0.cellgroup_s_s_p_t"
2,5, "t.l0.cellgroup_s_s_p_a"
3,0, "t.l0.cellgroup_s_s_d_s"
3,1, "t.l0.cellgroup_s_s_d_g"
3,2, "t.l0.cellgroup_s_s_d_p"
3,3, "t.l0.cellgroup_s_s_d_d"
3,4, "t.l0.cellgroup_s_s_d_t"
3,5, "t.l0.cellgroup_s_s_d_a"
4,0, "t.l0.cellgroup_s_s_t_s"
4,1, "t.l0.cellgroup_s_s_t_g"
4,2, "t.l0.cellgroup_s_s_t_p"
4,3, "t.l0.cellgroup_s_s_t_d"
4,4, "t.l0.cellgroup_s_s_t_t"
4,5, "t.l0.cellgroup_s_s_t_a"
5,0, "t.l0.cellgroup_s_s_a_s"
5,1, "t.l0.cellgroup_s_s_a_g"
5,2, "t.l0.cellgroup_s_s_a_p"
5,3, "t.l0.cellgroup_s_s_a_d"
5,4, "t.l0.cellgroup_s_s_a_t"
5,5, "t.l0.cellgroup_s_s_a_a"
6,0, "t.l0.cellgroup_s_g_s_s"
6,1, "t.l0.cellgroup_s_g_s_g"
6,2, "t.l0.cellgroup_s_g_s_p"
6,3, "t.l0.cellgroup_s_g_s_d"
6,4, "t.l0.cellgroup_s_g_s_t"
6,5, "t.l0.cellgroup_s_g_s_a"
7,0, "t.l0.cellgroup_s_g_g_s"
7,1, "t.l0.cellgroup_s_g_g_g"
7,2, "t.l0.cellgroup_s_g_g_p"
7,3, "t.l0.cellgroup_s_g_g_d"
7,4, "t.l0.cellgroup_s_g_g_t"
7,5, "t.l0.cellgroup_s_g_g_a"
8,0, "t.l0.cellgroup_s_g_p_s"
8,1, "t.l0.cellgroup_s_g_p_g"
8,2, "t.l0.cellgroup_s_g_p_p"
8,3, "t.l0.cellgroup_s_g_p_d"
8,4, "t.l0.cellgroup_s_g_p_t"
8,5, "t.l0.cellgroup_s_g_p_a"
9,0, "t.l0.cellgroup_s_g_d_s"
9,1, "t.l0.cellgroup_s_g_d_g"
9,2, "t.l0.cellgroup_s_g_d_p"
9,3, "t.l0.cellgroup_s_g_d_d"
9,4, "t.l0.cellgroup_s_g_d_t"
9,5, "t.l0.cellgroup_s_g_d_a"
10,0, "t.l0.cellgroup_s_g_t_s"
10,1, "t.l0.cellgroup_s_g_t_g"
10,2, "t.l0.cellgroup_s_g_t_p"
10,3, "t.l0.cellgroup_s_g_t_d"
10,4, "t.l0.cellgroup_s_g_t_t"
10,5, "t.l0.cellgroup_s_g_t_a"
11,0, "t.l0.cellgroup_s_g_a_s"
11,1, "t.l0.cellgroup_s_g_a_g"
11,2, "t.l0.cellgroup_s_g_a_p"
11,3, "t.l0.cellgroup_s_g_a_d"
11,4, "t.l0.cellgroup_s_g_a_t"
11,5, "t.l0.cellgroup_s_g_a_a"
12,0, "t.l0.cellgroup_s_p_s_s"
12,1, "t.l0.cellgroup_s_p_s_g"
12,2, "t.l0.cellgroup_s_p_s_p"
12,3, "t.l0.cellgroup_s_p_s_d"
12,4, "t.l0.cellgroup_s_p_s_t"
12,5, "t.l0.cellgroup_s_p_s_a"
13,0, "t.l0.cellgroup_s_p_g_s"
13,1, "t.l0.cellgroup_s_p_g_g"
13,2, "t.l0.cellgroup_s_p_g_p"
13,3, "t.l0.cellgroup_s_p_g_d"
13,4, "t.l0.cellgroup_s_p_g_t"
13,5, "t.l0.cellgroup_s_p_g_a"
14,0, "t.l0.cellgroup_s_p_p_s"
14,1, "t.l0.cellgroup_s_p_p_g"
14,2, "t.l0.cellgroup_s_p_p_p"
14,3, "t.l0.cellgroup_s_p_p_d"
14,4, "t.l0.cellgroup_s_p_p_t"
14,5, "t.l0.cellgroup_s_p_p_a"
15,0, "t.l0.cellgroup_s_p_d_s"
15,1, "t.l0.cellgroup_s_p_d_g"
15,2, "t.l0.cellgroup_s_p_d_p"
15,3, "t.l0.cellgroup_s_p_d_d"
15,4, "t.l0.cellgroup_s_p_d_t"
15,5, "t.l0.cellgroup_s_p_d_a"
16,0, "t.l0.cellgroup_s_p_t_s"
16,1, "t.l0.cellgroup_s_p_t_g"
16,2, "t.l0.cellgroup_s_p_t_p"
16,3, "t.l0.cellgroup_s_p_t_d"
16,4, "t.l0.cellgroup_s_p_t_t"
16,5, "t.l0.cellgroup_s_p_t_a"
17,0, "t.l0.cellgroup_s_p_a_s"
17,1, "t.l0.cellgroup_s_p_a_g"
17,2, "t.l0.cellgroup_s_p_a_p"
17,3, "t.l0.cellgroup_s_p_a_d"
17,4, "t.l0.cellgroup_s_p_a_t"
17,5, "t.l0.cellgroup_s_p_a_a"
18,0, "t.l0.cellgroup_s_d_s_s"
18,1, "t.l0.cellgroup_s_d_s_g"
18,2, "t.l0.cellgroup_s_d_s_p"
18,3, "t.l0.cellgroup_s_d_s_d"
18,4, "t.l0.cellgroup_s_d_s_t"
18,5, "t.l0.cellgroup_s_d_s_a"
19,0, "t.l0.cellgroup_s_d_g_s"
19,1, "t.l0.cellgroup_s_d_g_g"
19,2, "t.l0.cellgroup_s_d_g_p"
19,3, "t.l0.cellgroup_s_d_g_d"
19,4, "t.l0.cellgroup_s_d_g_t"
19,5, "t.l0.cellgroup_s_d_g_a"
20,0, "t.l0.cellgroup_s_d_p_s"
20,1, "t.l0.cellgroup_s_d_p_g"
20,2, "t.l0.cellgroup_s_d_p_p"
20,3, "t.l0.cellgroup_s_d_p_d"
20,4, "t.l0.cellgroup_s_d_p_t"
20,5, "t.l0.cellgroup_s_d_p_a"
21,0, "t.l0.cellgroup_s_d_d_s"
21,1, "t.l0.cellgroup_s_d_d_g"
21,2, "t.l0.cellgroup_s_d_d_p"
21,3, "t.l0.cellgroup_s_d_d_d"
21,4, "t.l0.cellgroup_s_d_d_t"
21,5, "t.l0.cellgroup_s_d_d_a"
22,0, "t.l0.cellgroup_s_d_t_s"
22,1, "t.l0.cellgroup_s_d_t_g"
22,2, "t.l0.cellgroup_s_d_t_p"
22,3, "t.l0.cellgroup_s_d_t_d"
22,4, "t.l0.cellgroup_s_d_t_t"
22,5, "t.l0.cellgroup_s_d_t_a"
23,0, "t.l0.cellgroup_s_d_a_s"
23,1, "t.l0.cellgroup_s_d_a_g"
23,2, "t.l0.cellgroup_s_d_a_p"
23,3, "t.l0.cellgroup_s_d_a_d"
23,4, "t.l0.cellgroup_s_d_a_t"
23,5, "t.l0.cellgroup_s_d_a_a"
24,0, "t.l0.cellgroup_s_t_s_s"
24,1, "t.l0.cellgroup_s_t_s_g"
24,2, "t.l0.cellgroup_s_t_s_p"
24,3, "t.l0.cellgroup_s_t_s_d"
24,4, "t.l0.cellgroup_s_t_s_t"
24,5, "t.l0.cellgroup_s_t_s_a"
25,0, "t.l0.cellgroup_s_t_g_s"
25,1, "t.l0.cellgroup_s_t_g_g"
25,2, "t.l0.cellgroup_s_t_g_p"
25,3, "t.l0.cellgroup_s_t_g_d"
25,4, "t.l0.cellgroup_s_t_g_t"
25,5, "t.l0.cellgroup_s_t_g_a"
26,0, "t.l0.cellgroup_s_t_p_s"
26,1, "t.l0.cellgroup_s_t_p_g"
26,2, "t.l0.cellgroup_s_t_p_p"
26,3, "t.l0.cellgroup_s_t_p_d"
26,4, "t.l0.cellgroup_s_t_p_t"
26,5, "t.l0.cellgroup_s_t_p_a"
27,0, "t.l0.cellgroup_s_t_d_s"
27,1, "t.l0.cellgroup_s_t_d_g"
27,2, "t.l0.cellgroup_s_t_d_p"
27,3, "t.l0.cellgroup_s_t_d_d"
27,4, "t.l0.cellgroup_s_t_d_t"
27,5, "t.l0.cellgroup_s_t_d_a"
28,0, "t.l0.cellgroup_s_t_t_s"
28,1, "t.l0.cellgroup_s_t_t_g"
28,2, "t.l0.cellgroup_s_t_t_p"
28,3, "t.l0.cellgroup_s_t_t_d"
28,4, "t.l0.cellgroup_s_t_t_t"
28,5, "t.l0.cellgroup_s_t_t_a"
29,0, "t.l0.cellgroup_s_t_a_s"
29,1, "t.l0.cellgroup_s_t_a_g"
29,2, "t.l0.cellgroup_s_t_a_p"
29,3, "t.l0.cellgroup_s_t_a_d"
29,4, "t.l0.cellgroup_s_t_a_t"
29,5, "t.l0.cellgroup_s_t_a_a"
30,0, "t.l0.cellgroup_s_a_s_s"
30,1, "t.l0.cellgroup_s_a_s_g"
30,2, "t.l0.cellgroup_s_a_s_p"
30,3, "t.l0.cellgroup_s_a_s_d"
30,4, "t.l0.cellgroup_s_a_s_t"
30,5, "t.l0.cellgroup_s_a_s_a"
31,0, "t.l0.cellgroup_s_a_g_s"
31,1, "t.l0.cellgroup_s_a_g_g"
31,2, "t.l0.cellgroup_s_a_g_p"
31,3, "t.l0.cellgroup_s_a_g_d"
31,4, "t.l0.cellgroup_s_a_g_t"
31,5, "t.l0.cellgroup_s_a_g_a"
32,0, "t.l0.cellgroup_s_a_p_s"
32,1, "t.l0.cellgroup_s_a_p_g"
32,2, "t.l0.cellgroup_s_a_p_p"
32,3, "t.l0.cellgroup_s_a_p_d"
32,4, "t.l0.cellgroup_s_a_p_t"
32,5, "t.l0.cellgroup_s_a_p_a"
33,0, "t.l0.cellgroup_s_a_d_s"
33,1, "t.l0.cellgroup_s_a_d_g"
33,2, "t.l0.cellgroup_s_a_d_p"
33,3, "t.l0.cellgroup_s_a_d_d"
33,4, "t.l0.cellgroup_s_a_d_t"
33,5, "t.l0.cellgroup_s_a_d_a"
34,0, "t.l0.cellgroup_s_a_t_s"
34,1, "t.l0.cellgroup_s_a_t_g"
34,2, "t.l0.cellgroup_s_a_t_p"
34,3, "t.l0.cellgroup_s_a_t_d"
34,4, "t.l0.cellgroup_s_a_t_t"
34,5, "t.l0.cellgroup_s_a_t_a"
35,0, "t.l0.cellgroup_s_a_a_s"
35,1, "t.l0.cellgroup_s_a_a_g"
35,2, "t.l0.cellgroup_s_a_a_p"
35,3, "t.l0.cellgroup_s_a_a_d"
35,4, "t.l0.cellgroup_s_a_a_t"
35,5, "t.l0.cellgroup_s_a_a_a"
}
