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
    "Length of Liner2: FT",
    "Length of HWDP: FT",
    "TOL: FT",
    "TOL_TVD: FT",
    "Last CSG FS: FT",
    "Float Shoe: FT",
    "Shoe track: FT",
    "Mud Weight: PCF",
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
    "Length_of_Liner2",
    "Length_of_HWDP",
    "TOL",
    "TOL_TVD",
    "Last_CSG_FS",
    "FS",
    "Shoe_track",
    "Mud_Weight",
]

csg = {
    '': [{'grd': '', 'od': 0,
          'id': 0, 'cap': 0, 'trq': 0}],
    '13-3/8': [
        {'grd': 'TN-110HS / TENARIS BLUE', 'od': 13.375,
            'id': 13.031, 'cap': 0.1650, 'trq': 41750},
        {'grd': 'VM-110HCSS / VAM TOP', 'od': 13.375,
            'id': 13.39, 'cap': 0.1742, 'trq': 23150},
        {'grd': 'TN-100HS / TENARIS BLUE', 'od': 13.375,
            'id': 13.031, 'cap': 0.1650, 'trq': 41750},
        {'grd': 'VM-100HCSS / VAM 21', 'od': 13.375,
            'id': 12.835, 'cap': 0.1601, 'trq': 47750},
        {'grd': 'VM-95HC / VAM TOP', 'od': 13.375,
            'id': 13.386, 'cap': 0.1741, 'trq': 23150},
        {'grd': 'TN-95HC / 3SB Casing', 'od': 13.375,
            'id': 11.811, 'cap': 0.1356, 'trq': 20000},
    ],
    '9-5/8': [
        {'grd': 'VM-125HC / VAM FJL', 'od': 9.625,
            'id': 8.435, 'cap': 0.0691, 'trq': 15900},
        {'grd': 'TN-110HS / TENARIS BLUE', 'od': 9.625,
            'id': 8.435, 'cap': 0.0691, 'trq': 29180},
        {'grd': 'VM-110HCSS / VAM TOP-HC-NB', 'od': 9.625,
            'id': 8.435, 'cap': 0.0691, 'trq': 23150},
        {'grd': 'VM-110HCSS / VAM 21', 'od': 9.625,
            'id': 8.435, 'cap': 0.0691, 'trq': 43700},
        {'grd': 'TN-110HC / 3SB Casing', 'od': 9.625,
            'id': 8.435, 'cap': 0.0691, 'trq': 18000},
        {'grd': 'VM-110HC / VAM TOP-HC-NB', 'od': 9.625,
            'id': 8.435, 'cap': 0.0691, 'trq': 23150},
        {'grd': 'TN-95HS / 3SB Casing', 'od': 9.625,
            'id': 8.535, 'cap': 0.0708, 'trq': 16500},
        {'grd': 'VM-95HCSS / VAM TOP-HC-NA', 'od': 9.625,
            'id': 8.535, 'cap': 0.0708, 'trq': 23150},
    ],
    '7': [
        {'grd': 'TN-110HS / TENARIS BLUE', 'od': 7,
            'id': 6.004, 'cap': 0.0350, 'trq': 14280},
        {'grd': 'VM-110HCSS / VAM TOP-HC', 'od': 7,
            'id': 6.004, 'cap': 0.0350, 'trq': 22800},
        {'grd': 'L-80.1 / NEW VAM', 'od': 7,
            'id': 6.004, 'cap': 0.0350, 'trq': 10500},
        {'grd': 'VM-95-13CRSS / VAM TOP-HC', 'od': 7,
            'id': 6.094, 'cap': 0.0361, 'trq': 17700},
        {'grd': 'TN-95HS / 3SB CASING', 'od': 7,
            'id': 6.094, 'cap': 0.0361, 'trq': 11000},
        {'grd': 'VM-95HCSS / VAM TOP-HC', 'od': 7,
            'id': 6.094, 'cap': 0.0361, 'trq': 17700},
        {'grd': 'L-80.1 / NEW VAM', 'od': 7,
            'id': 6.276, 'cap': 0.0383, 'trq': 8300},
        {'grd': 'L-80.1 / VA-GT*', 'od': 7,
            'id': 6.276, 'cap': 0.0383, 'trq': 10550},
        {'grd': 'J-55 / VA-GT*', 'od': 7, 'id': 6.276, 'cap': 0.0383, 'trq': 8510},
        {'grd': 'J-55 / NEW VAM', 'od': 7, 'id': 6.276, 'cap': 0.0383, 'trq': 7230},
    ],
    '4-1/2': [
        {'grd': 'Q-125 / TENARIS BLUE', 'od': 4.5,
            'id': 3.826, 'cap': 0.0142, 'trq': 8150},
        {'grd': 'VM-125HC / VAM TOP-HC-KA', 'od': 4.5,
            'id': 3.826, 'cap': 0.0142, 'trq': 7960},
        {'grd': 'TN-95HS / 3SB Casing', 'od': 4.5,
            'id': 3.82, 'cap': 0.0142, 'trq': 5300},
        {'grd': 'VM-95HCSS / VAM TOP-HC-KA', 'od': 4.5,
            'id': 3.826, 'cap': 0.0142, 'trq': 6510},
        {'grd': 'TN-CR13S-95 / 3SB Casing', 'od': 4.5,
            'id': 3.92, 'cap': 0.0149, 'trq': 4400},
        {'grd': 'VM-95-13CRSS / VAM TOP-HC', 'od': 4.5,
            'id': 3.92, 'cap': 0.0149, 'trq': 5210},
        {'grd': 'VM-95HCSS / VAM TOP-HC', 'od': 4.5,
            'id': 3.92, 'cap': 0.0149, 'trq': 5210},
        {'grd': 'TN-95HS / 3SB Casing', 'od': 4.5,
            'id': 3.92, 'cap': 0.0149, 'trq': 4400},
        {'grd': 'L-80.1 / NEW VAM', 'od': 4.5,
            'id': 3.958, 'cap': 0.0152, 'trq': 4770},
        {'grd': 'L-80.1 / VA-GT*', 'od': 4.5,
            'id': 3.958, 'cap': 0.0152, 'trq': 4480},
        {'grd': 'J-55 / VA-GT*', 'od': 4.5, 'id': 4, 'cap': 0.0155, 'trq': 3590},
    ],
    '3-1/2': [
        {'grd': 'J/K-55 / EUE', 'od': 3.5, 'id': 2.992, 'cap': 0.0087, 'trq': 2280},
        {'grd': 'L-80.1 / NEW VAM', 'od': 3.5,
            'id': 2.992, 'cap': 0.0087, 'trq': 3250},
        {'grd': 'L-80.1 / VA-GT*', 'od': 3.5,
            'id': 2.992, 'cap': 0.0087, 'trq': 2820},
        {'grd': 'J-55 / VA-GT SPCL*', 'od': 3.5,
            'id': 2.992, 'cap': 0.0087, 'trq': 2320},
    ],
    '2-7/8': [
        {'grd': 'L-80.1 / PH-6', 'od': 2.875,
            'id': 2.259, 'cap': 0.0050, 'trq': 3400},
        {'grd': 'J/K-55 / EUE', 'od': 2.875,
            'id': 2.441, 'cap': 0.0058, 'trq': 1650},
        {'grd': 'L-80.1 / NEW VAM', 'od': 2.875,
            'id': 2.441, 'cap': 0.0058, 'trq': 2390},
        {'grd': 'J-55 / VAM FJL', 'od': 2.875,
            'id': 2.441, 'cap': 0.0058, 'trq': 720},
        {'grd': 'J-55 / NEW VAM', 'od': 2.875,
            'id': 2.441, 'cap': 0.0058, 'trq': 1740},
        {'grd': 'J-55 / VA-GT*', 'od': 2.875,
            'id': 2.441, 'cap': 0.0058, 'trq': 1770},
    ],
    '2-3/8': [
        {'grd': 'L-80.1 / SC HYDRIL', 'od': 2.375,
            'id': 1.995, 'cap': 0.0039, 'trq': 1700},
        {'grd': 'J/K-55 / EUE', 'od': 2.375,
            'id': 1.995, 'cap': 0.0039, 'trq': 1290},
        {'grd': 'J-55 / NEW VAM', 'od': 2.375,
            'id': 1.995, 'cap': 0.0039, 'trq': 1160},
    ],
}
hwData = {
    '': {
        'id': 0,
        'od': 0,
        'thr': '',
        'cap': 0,
        'wt': 0
    },
    '3-1/2': {
        'id': 2.25,
        'od': 3.5,
        'thr': '3-1/5 IF',
        'cap': 0.00464,
        'wt': 25.6
    },
    '5': {
        'id': 3,
        'od': 5,
        'thr': '4-1/5 IF',
        'cap': 0.01026,
        'wt': 50
    },
    '4': {
        'id': 2.625,
        'od': 4,
        'thr': 'XT-39',
        'cap': 0.0063,
        'wt': 25
    },
    '5-1/2': {
        'id': 3.25,
        'od': 5.5,
        'thr': 'XT-54',
        'cap': 0.01026,
        'wt': 52
    },
}
dpData = {
    '3-1/2': {
        'id': 2.602,
        'od': 3.5,
        'thr': '3-1/5 IF',
        'cap': 0.00742,
        'wt': 13.3,
        'const': 0.12
    },
    '5': {
        'id': 4.276,
        'od': 5,
        'thr': '4-1/5 IF',
        'cap': 0.01776,
        'wt': 19.5,
        'const': 0.09
    },
    '4': {
        'id': 3.34,
        'od': 4,
        'thr': 'XT-39',
        'cap': 0.0108,
        'wt': 14,
        'const': 0.11
    },
    '5-1/2': {
        'id': 4.67,
        'od': 5.5,
        'thr': 'XT-54',
        'cap': 0.0212,
        'wt': 24.7,
        'const': 0.08
    },
}
ohData = {
    '16': {
        'id': 16,
        'od': 99999,
        'cap': 0.2488
    },
    '12': {
        'id': 12,
        'od': 99999,
        'cap': 0.1399
    },
    '8-1/2': {
        'id': 8.5,
        'od': 99999,
        'cap': 0.0702
    },
    '8-3/8': {
        'id': 8.375,
        'od': 99999,
        'cap': 0.0682
    },
    '6-1/8': {
        'id': 6.125,
        'od': 99999,
        'cap': 0.0365
    },
    '5-7/8': {
        'id': 5.875,
        'od': 99999,
        'cap': 0.0335
    },
}
options = {
    "Liner1": csg,
    "Liner2": csg,
    "Last_CSG_OD": csg,
    "OH": ohData.keys(),
    "HW_OD": hwData.keys(),
    "DP_OD": dpData.keys()
}
