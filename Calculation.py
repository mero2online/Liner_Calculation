from Options import *


def makeCalculation(values):
    Liner1, Liner1_Grade_ID, Liner2, Liner2_Grade_ID,  \
        Last_CSG_OD, Last_CSG_Grade_ID, OH, HW_OD, DP_OD, \
        Length_of_Liner2, Length_of_HWDP,  \
        TOL, TOL_TVD, Last_CSG_FS, FS, Shoe_track, Mud_Weight = values

    Liner1_Match = [i for i in csg[Liner1] if i['grd'] == Liner1_Grade_ID]
    Liner2_Match = [i for i in csg[Liner2] if i['grd'] == Liner2_Grade_ID]
    Last_CSG_Grade_ID_Match = [
        i for i in csg[Last_CSG_OD] if i['grd'] == Last_CSG_Grade_ID]

    Anulus_OH = ((ohData[OH]['id']**2)-(Liner1_Match[0]['od']**2))/1029
    Anulus_Csg_Csg = (
        (Last_CSG_Grade_ID_Match[0]['id']**2)-(Liner1_Match[0]['od']**2))/1029
    Anulus_DP_Csg = (
        (Last_CSG_Grade_ID_Match[0]['id']**2)-((dpData[DP_OD]['od']**2)))/1029.4
    Anulus_HW_Csg = (
        (Last_CSG_Grade_ID_Match[0]['id']**2)-((hwData[HW_OD]['od']**2)))/1029.4
    Shoe_Track_Depth = FS - Shoe_track
    Length_DP = TOL - Length_of_HWDP
    Mud_Weight_PPG = Mud_Weight/7.48

    # Displacement
    DP_Vol = (Length_DP*dpData[DP_OD]['cap']) + \
        (Length_of_HWDP*hwData[HW_OD]['cap'])
    #
    Liner_Vol = (
        ((Shoe_Track_Depth-TOL)-Length_of_Liner2)*Liner1_Match[0]['cap'])+(Length_of_Liner2*Liner2_Match[0]['cap'])
    #
    Total_Displacement = DP_Vol + Liner_Vol

    # Anulus
    Anulus_OH_Vol = Anulus_OH * ((FS+3) - Last_CSG_FS)
    Anulus_CSG_DP_Vol = Anulus_DP_Csg * Length_DP
    Anulus_CSG_HW_Vol = Anulus_HW_Csg * Length_of_HWDP
    BTM_UP_TD = Anulus_OH_Vol+Anulus_CSG_DP_Vol+Anulus_CSG_HW_Vol

    # Bouncy
    Bouncy = (65.4-Mud_Weight_PPG)/65.4

    # Weight
    Liner_Weight = (((Shoe_Track_Depth-TOL)-Length_of_Liner2)*Liner1_Match[0]['wt'])+(
        Length_of_Liner2*Liner2_Match[0]['wt'])*Bouncy

    DP_Weight = ((Length_DP*dpData[DP_OD]['wt']) +
                 (Length_of_HWDP*hwData[HW_OD]['wt']))*Bouncy

    Total_Weight = Liner_Weight+DP_Weight

    # DP Stretch
    DP_Stretch = (100*(TOL_TVD/1000)*dpData[DP_OD]['const'])/12

    result = {
        "DP Vol: BBL": int(DP_Vol),
        "Liner Vol: BBL": int(Liner_Vol),
        "Total Displacement: BBL": int(Total_Displacement),
        "Anulus OH Vol: BBL": "{:.0f}".format(Anulus_OH_Vol),
        "BTM UP @ TD: BBL": "{:.0f}".format(BTM_UP_TD),
        "Liner Weight: LBS": "{:.0f}".format(Liner_Weight),
        "DP Weight: LBS": "{:.0f}".format(DP_Weight),
        "Total Weight: LBS": "{:.0f}".format(Total_Weight),
        "Bouncy": "{:.2f}".format(Bouncy),
        "DP Stretch: FT": "{:.2f}".format(DP_Stretch)
    }

    return result
