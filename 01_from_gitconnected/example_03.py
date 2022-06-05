# based on 
# https://levelup.gitconnected.com/python-pandas-google-spreadsheet-476bd6a77f2b
# https://gist.github.com/lucasmbribeiro/d39f8b1c95c8322c6edfed8e667582c0#file-03_gs-ipynb


import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import private_settings


#   Reference Link: https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account
def create_credentials():

    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]
        
    credentials = Credentials.from_service_account_file(
            private_settings.GOOGLE_SHEET_JSON_FILE,
            scopes=scopes
        )
    
    return gspread.authorize(credentials)

# Reference Link: 
# https://gspread.readthedocs.io/en/latest/user-guide.html?#getting-all-values-from-a-row-or-a-column
# https://gspread.readthedocs.io/en/latest/user-guide.html?#getting-a-cell-value
def read_spreadsheet(spreadsheet_id, tab_name):
    
    gc = create_credentials()
    
    gc = gc.open_by_key(spreadsheet_id)
    
    values = gc.worksheet(tab_name).get_all_values(value_render_option = "FORMULA")
    # values = gc.get_worksheet(tab_index).batch_get(value_render_option  = "FORMULA")
    
    df = pd.DataFrame(values)
    df.columns = df.iloc[0]
    df.drop(df.index[0], inplace=True)         

    return df

df_ = read_spreadsheet(private_settings.SPREADSHEET_ID, 'RB' )
print(df_.head())
