import pandas as pd
import arcpy
from tqdm import tqdm
sourcedata = r"C:\Users\M3ECHJJJ\Documents\Data\Parcels\RE\Real_acct_owner\real_acct_utf8.txt"
targetdata = r'C:\Users\M3ECHJJJ\Documents\Data\Parcels\RE\HCAD.gdb\parcels'

ra_df = pd.read_csv(sourcedata,sep="\t")
ra_df['acct'] = ra_df['acct'].astype(str)
ra_df['acct']= ra_df['acct'].str.zfill(13)
ra_df = ra_df.set_index('acct')

targetfields = ['HCAD_NUM', 'Market_Area_1', 'Market_Area_1_Dscr',
       'Market_Area_2', 'Market_Area_2_Dscr', 'econ_area', 'econ_bld_class',
       'center_code', 'yr_impr', 'yr_annexed', 'splt_dt', 'dsc_cd', 'nxt_bld',
       'bld_ar', 'land_ar', 'acreage', 'Cap_acct', 'shared_cad', 'land_val',
       'bld_val', 'x_features_val', 'ag_val', 'assessed_val', 'tot_appr_val',
       'tot_mkt_val', 'prior_land_val', 'prior_bld_val',
       'prior_x_features_val', 'prior_ag_val', 'prior_tot_appr_val',
       'prior_tot_mkt_val', 'new_construction_val', 'tot_rcn_val',
       'value_status', 'noticed', 'notice_dt', 'protested', 'certified_date',
       'rev_dt', 'rev_by', 'new_own_dt', 'lgl_1', 'lgl_2', 'lgl_3', 'lgl_4',
       'jurs']


count = int(arcpy.GetCount_management(targetdata).getOutput(0))

# Create update cursor for feature class
with arcpy.da.UpdateCursor(targetdata, targetfields,"land_val is null") as cursor:
    for row in tqdm(cursor, total=count):
        try:
            df = ra_df.loc[row[0]]
            row[1]=df['Market_Area_1']
            row[2]=df['Market_Area_1_Dscr']
            row[3]=df['Market_Area_2']
            row[4]=df['Market_Area_2_Dscr']
            row[5]=df['econ_area']
            row[6]=df['econ_bld_class']
            row[7]=df['center_code']
            row[8]=df['yr_impr']
            row[9]=df['yr_annexed']
            row[10]=df['splt_dt']
            row[11]=df['dsc_cd']
            row[12]=df['nxt_bld']
            row[13]=df['bld_ar']
            row[14]=df['land_ar']
            row[15]=df['acreage']
            row[16]=df['Cap_acct']
            row[17]=df['shared_cad']
            row[18]=df['land_val']
            row[19]=df['bld_val']
            row[20]=df['x_features_val']
            row[21]=df['ag_val']
            row[22]=df['assessed_val']
            row[23]=df['tot_appr_val']
            row[24]=df['tot_mkt_val']
            row[25]=df['prior_land_val']
            row[26]=df['prior_bld_val']
            row[27]=df['prior_x_features_val']
            row[28]=df['prior_ag_val']
            row[29]=df['prior_tot_appr_val']
            row[30]=df['prior_tot_mkt_val']
            row[31]=df['new_construction_val']
            row[32]=df['tot_rcn_val']
            row[33]=df['value_status']
            row[34]=df['noticed']
            row[35]=df['notice_dt']
            row[36]=df['protested']
            row[37]=df['certified_date']
            row[38]=df['rev_dt']
            row[39]=df['rev_by']
            row[40]=df['new_own_dt']
            row[41]=df['lgl_1']
            row[42]=df['lgl_2']
            row[43]=df['lgl_3']
            row[44]=df['lgl_4']
            row[45]=df['jurs']

            cursor.updateRow(row)
        except Exception as e:
            pass
