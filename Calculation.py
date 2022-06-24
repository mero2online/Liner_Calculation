from Options import *


def makeCalculation(values):
    Liner1, Liner1_Grade_ID, Liner2, Liner2_Grade_ID, *o1 = values
    Last_CSG_OD, Last_CSG_Grade_ID, OH, HW_OD, DP_OD, Length_of_HWDP, *o2 = o1
    TOL, Last_CSG_FS, FS, Shoe_track, Top_Cement_above_TOL, *o3 = o2
    Mud_Weight, Excess_OH, Excess_Cased_Hole, *o4 = o3
    Additional_OH_Vol, Cement_Behind_Plug, *o5 = o4
    Dead_Volume, Tail_Slurry_Yield, Tail_Mix_Water, *o6 = o5
    Lead_Slurry_Yield, Lead_Mix_Water, Spacer_Volume = o6

    Liner1_Match = [i for i in csg[Liner1] if i['grd'] == Liner1_Grade_ID]
    Last_CSG_Grade_ID_Match = [
        i for i in csg[Last_CSG_OD] if i['grd'] == Last_CSG_Grade_ID]

    Anulus_OH = ((ohData[OH]['id']**2)-(Liner1_Match[0]['od']**2))/1029
    Anulus_Csg_Csg = (
        (Last_CSG_Grade_ID_Match[0]['id']**2)-(Liner1_Match[0]['od']**2))/1029
    Anulus_DP_Csg = (
        (Last_CSG_Grade_ID_Match[0]['id']**2)-(dpData[DP_OD]['od']**2))/1029.4
    Shoe_Track_Depth = FS - Shoe_track
    Tail_TOC = FS-1400
    TO_Cement = TOL - Top_Cement_above_TOL
    TO_Displ_Mud_DP = TO_Cement-(6*90)
    Hight_Spacer_above_TOC = Spacer_Volume / Anulus_DP_Csg
    TOS_CSG = TO_Cement - Hight_Spacer_above_TOC
    Length_DP = TOL - Length_of_HWDP
    Mud_Weight_PPG = Mud_Weight/7.48

    # Cement Calculation
    Dead_Volume_cuft = Dead_Volume * 5.615
    # Tail Slurry
    Tail_Shoe_track_behind_plug_BBL = (
        (FS-Shoe_Track_Depth)*Liner1_Match[0]['cap'])+Cement_Behind_Plug
    Tail_Annulus_OH_Liner_BBL = (
        ((FS-Tail_TOC)*Anulus_OH)+Additional_OH_Vol)*(1+(Excess_OH/100))
    Total_Tail_Slurry_Volume_BBL = Tail_Shoe_track_behind_plug_BBL + \
        Tail_Annulus_OH_Liner_BBL

    Tail_Shoe_track_behind_plug_cuft = Tail_Shoe_track_behind_plug_BBL * 5.6146
    Tail_Annulus_OH_Liner_cuft = Tail_Annulus_OH_Liner_BBL * 5.6146
    Total_Tail_Slurry_Volume_cuft = Total_Tail_Slurry_Volume_BBL * 5.6146

    Tail_Sacks_Needed_sx = (Total_Tail_Slurry_Volume_cuft +
                            Dead_Volume_cuft) / Tail_Slurry_Yield
    # Lead Slurry
    Lead_Annulus_OH_Liner_BBL = (
        Tail_TOC-Last_CSG_FS)*Anulus_OH*(1+(Excess_OH/100))
    Lead_Annulus_OH_Liner_DP_BBL = ((Last_CSG_FS-TOL)*Anulus_Csg_Csg*(
        1+(Excess_Cased_Hole/100))) + (Top_Cement_above_TOL*Anulus_DP_Csg)
    Total_Lead_Slurry_Volume_BBL = Lead_Annulus_OH_Liner_BBL + \
        Lead_Annulus_OH_Liner_DP_BBL

    Lead_Annulus_OH_Liner_cuft = Lead_Annulus_OH_Liner_BBL * 5.6146
    Lead_Annulus_OH_Liner_DP_cuft = Lead_Annulus_OH_Liner_DP_BBL * 5.6146
    Total_Lead_Slurry_Volume_cuft = Total_Lead_Slurry_Volume_BBL * 5.6146

    Lead_Sacks_Needed_sx = (Total_Lead_Slurry_Volume_cuft +
                            Dead_Volume_cuft) / Lead_Slurry_Yield

    # Displacement
    Vol_DP = Length_DP*dpData[DP_OD]['cap']+Length_of_HWDP*0.0103
    #
    Vol_Liner_TOL_Shoe_Track = (Shoe_Track_Depth-TOL)*Liner1_Match[0]['cap']
    #
    Total_Displacement = Vol_DP + Vol_Liner_TOL_Shoe_Track

    # Spacer
    Displacement_Mud = (
        (FS-TOL)*Liner1_Match[0]['cap'])+((TOL-TO_Displ_Mud_DP)*dpData[DP_OD]['cap'])

    # Bouncy
    Bouncy = (65.4-Mud_Weight_PPG)/65.4

    resultTxt = f'''
Tail_Sacks_Needed: {int(Tail_Sacks_Needed_sx)} sx
Lead_Sacks_Needed: {int(Lead_Sacks_Needed_sx)} sx
Vol_DP: {int(Vol_DP)} BBL
Vol_Liner_TOL_Shoe_Track: {int(Vol_Liner_TOL_Shoe_Track)} BBL
Total_Displacement: {int(Total_Displacement)} BBL
Displacement_Mud: {int(Displacement_Mud)} BBL
Bouncy: {"{:.2f}".format(Bouncy)}
'''

    return resultTxt
