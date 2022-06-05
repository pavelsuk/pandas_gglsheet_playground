import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import private_settings

def get_data_google_sheets(sample_spreadsheet_id, tab_index):
    
    # Link to authenticate 
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]

    # Read the .json file and authenticate with the links
    credentials = Credentials.from_service_account_file(
            private_settings.GOOGLE_SHEET_JSON_FILE,
            scopes=scopes
        )
    
    # Request authorization and open the selected spreadsheet
    gc = gspread.authorize(credentials).open_by_key(sample_spreadsheet_id)

    # Prompts for all spreadsheet values
    values = gc.get_worksheet(tab_index).get_all_values()
    
    # Turns the return into a dataframe
    df = pd.DataFrame(values)
    df.columns = df.iloc[0]
    df.drop(df.index[0], inplace=True)         

    return df

df_ = get_data_google_sheets(private_settings.SPREADSHEET_ID, 0 )
print(df_.head())
