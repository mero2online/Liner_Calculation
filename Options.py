myLabel = [
    "Liner1: INCH",
    "Liner1 Grade ID: INCH",
    "Liner2: INCH",
    "Liner2 Grade ID: INCH",
    "Last CSG OD: INCH",
    "Last CSG Grade ID: INCH",
    "OH: INCH",
    "HW: INCH",
    "DP OD: INCH",
    "TOL: FT",
    "Last CSG FS: FT",
    "FS: FT",
    "Shoe track: FT",
    "Top Cement above TOL: FT",
    "Mud Weight: PCF",
    "Excess OH: %",
    "Excess Cased Hole: %",
    "Additional OH Vol: BBL",
    "Cement Behind Plug: BBL",
    "Dead Volume: BBL",
    "Tail Slurry Yield: cuf/sx",
    "Tail Mix Water: Gal/Sx",
    "Lead Slurry Yield: cuf/sx",
    "Lead Mix Water: Gal/Sx",
    "Spacer Volume: BBL"
]
varArr = [
    "Liner1",
    "Liner1_Grade_ID",
    "Liner2",
    "Liner2_Grade_ID",
    "Last_CSG_OD",
    "Last_CSG_Grade_ID",
    "OH",
    "HW_OD",
    "DP_OD",
    "TOL",
    "Last_CSG_FS",
    "FS",
    "Shoe_track",
    "Top_Cement_above_TOL",
    "Mud_Weight",
    "Excess_OH",
    "Excess_Cased_Hole",
    "Additional_OH_Vol",
    "Cement_Behind_Plug",
    "Dead_Volume",
    "Tail_Slurry_Yield",
    "Tail_Mix_Water",
    "Lead_Slurry_Yield",
    "Lead_Mix_Water",
    "Spacer_Volume"]

csg = {
    '': [{'grd': '', 'id': 0, 'trq': 0}],
    '13-3/8': [
        {'grd': 'TN-110HS / TENARIS BLUE', 'id': 13.031, 'trq': 41750},
        {'grd': 'VM-110HCSS / VAM TOP', 'id': 13.39, 'trq': 23150},
        {'grd': 'TN-100HS / TENARIS BLUE', 'id': 13.031, 'trq': 41750},
        {'grd': 'VM-100HCSS / VAM 21', 'id': 12.835, 'trq': 47750},
        {'grd': 'VM-95HC / VAM TOP', 'id': 13.386, 'trq': 23150},
        {'grd': 'TN-95HC / 3SB Casing', 'id': 11.811, 'trq': 20000},
    ],
    '9-5/8': [
        {'grd': 'VM-125HC / VAM FJL', 'id': 8.435, 'trq': 15900},
        {'grd': 'TN-110HS / TENARIS BLUE', 'id': 8.435, 'trq': 29180},
        {'grd': 'VM-110HCSS / VAM TOP-HC-NB', 'id': 8.435, 'trq': 23150},
        {'grd': 'VM-110HCSS / VAM 21', 'id': 8.435, 'trq': 43700},
        {'grd': 'TN-110HC / 3SB Casing', 'id': 8.435, 'trq': 18000},
        {'grd': 'VM-110HC / VAM TOP-HC-NB', 'id': 8.435, 'trq': 23150},
        {'grd': 'TN-95HS / 3SB Casing', 'id': 8.535, 'trq': 16500},
        {'grd': 'VM-95HCSS / VAM TOP-HC-NA', 'id': 8.535, 'trq': 23150},
    ],
    '7': [
        {'grd': 'TN-110HS / TENARIS BLUE', 'id': 6.004, 'trq': 14280},
        {'grd': 'VM-110HCSS / VAM TOP-HC', 'id': 6.004, 'trq': 22800},
        {'grd': 'L-80.1 / NEW VAM', 'id': 6.004, 'trq': 10500},
        {'grd': 'VM-95-13CRSS / VAM TOP-HC', 'id': 6.094, 'trq': 17700},
        {'grd': 'TN-95HS / 3SB CASING', 'id': 6.094, 'trq': 11000},
        {'grd': 'VM-95HCSS / VAM TOP-HC', 'id': 6.094, 'trq': 17700},
        {'grd': 'L-80.1 / NEW VAM', 'id': 6.276, 'trq': 8300},
        {'grd': 'L-80.1 / VA-GT*', 'id': 6.276, 'trq': 10550},
        {'grd': 'J-55 / VA-GT*', 'id': 6.276, 'trq': 8510},
        {'grd': 'J-55 / NEW VAM', 'id': 6.276, 'trq': 7230},
    ],
    '4-1/2': [
        {'grd': 'Q-125 / TENARIS BLUE', 'id': 3.826, 'trq': 8150},
        {'grd': 'VM-125HC / VAM TOP-HC-KA', 'id': 3.826, 'trq': 7960},
        {'grd': 'TN-95HS / 3SB Casing', 'id': 3.82, 'trq': 5300},
        {'grd': 'VM-95HCSS / VAM TOP-HC-KA', 'id': 3.826, 'trq': 6510},
        {'grd': 'TN-CR13S-95 / 3SB Casing', 'id': 3.92, 'trq': 4400},
        {'grd': 'VM-95-13CRSS / VAM TOP-HC', 'id': 3.92, 'trq': 5210},
        {'grd': 'VM-95HCSS / VAM TOP-HC', 'id': 3.92, 'trq': 5210},
        {'grd': 'TN-95HS / 3SB Casing', 'id': 3.92, 'trq': 4400},
        {'grd': 'L-80.1 / NEW VAM', 'id': 3.958, 'trq': 4770},
        {'grd': 'L-80.1 / VA-GT*', 'id': 3.958, 'trq': 4480},
        {'grd': 'J-55 / VA-GT*', 'id': 4, 'trq': 3590},
    ],
    '3-1/2': [
        {'grd': 'J/K-55 / EUE', 'id': 2.992, 'trq': 2280},
        {'grd': 'L-80.1 / NEW VAM', 'id': 2.992, 'trq': 3250},
        {'grd': 'L-80.1 / VA-GT*', 'id': 2.992, 'trq': 2820},
        {'grd': 'J-55 / VA-GT SPCL*', 'id': 2.992, 'trq': 2320},
    ],
    '2-7/8': [
        {'grd': 'L-80.1 / PH-6', 'id': 2.259, 'trq': 3400},
        {'grd': 'J/K-55 / EUE', 'id': 2.441, 'trq': 1650},
        {'grd': 'L-80.1 / NEW VAM', 'id': 2.441, 'trq': 2390},
        {'grd': 'J-55 / VAM FJL', 'id': 2.441, 'trq': 720},
        {'grd': 'J-55 / NEW VAM', 'id': 2.441, 'trq': 1740},
        {'grd': 'J-55 / VA-GT*', 'id': 2.441, 'trq': 1770},
    ],
    '2-3/8': [
        {'grd': 'L-80.1 / SC HYDRIL', 'id': 1.995, 'trq': 1700},
        {'grd': 'J/K-55 / EUE', 'id': 1.995, 'trq': 1290},
        {'grd': 'J-55 / NEW VAM', 'id': 1.995, 'trq': 1160},
    ],
}
hwData = {
    '': {
        'id': 0,
        'thread': '',
        'capacity': 0,
        'wt': 0
    },
    '3-1/2': {
        'id': 2.25,
        'thread': '3-1/5 IF',
        'capacity': 0.00464,
        'wt': 25.6
    },
    '5': {
        'id': 3,
        'thread': '4-1/5 IF',
        'capacity': 0.01026,
        'wt': 50
    },
    '4': {
        'id': 2.625,
        'thread': 'XT-39',
        'capacity': 0.0063,
        'wt': 25
    },
    '5-1/2': {
        'id': 3.25,
        'thread': 'XT-54',
        'capacity': 0.01026,
        'wt': 52
    },
}
dpData = {
    '3-1/2': {
        'id': 2.602,
        'thread': '3-1/5 IF',
        'capacity': 0.00742,
        'wt': 13.3
    },
    '5': {
        'id': 4.276,
        'thread': '4-1/5 IF',
        'capacity': 0.01776,
        'wt': 19.5
    },
    '4': {
        'id': 3.34,
        'thread': 'XT-39',
        'capacity': 0.0108,
        'wt': 14
    },
    '5-1/2': {
        'id': 4.67,
        'thread': 'XT-54',
        'capacity': 0.0212,
        'wt': 24.7
    },
}
ohCapacityData = {
    '16': 0.2488,
    '12': 0.1399,
    '8-1/2': 0.0702,
    '8-3/8': 0.0682,
    '6-1/8': 0.0365,
    '5-7/8': 0.0335,
}
options = {
    "Liner1": csg,
    "Liner2": csg,
    "Last_CSG_OD": csg,
    "OH": ohCapacityData.keys(),
    "HW_OD": hwData.keys(),
    "DP_OD": dpData.keys()
}
