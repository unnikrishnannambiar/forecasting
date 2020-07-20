

import pandas as pd

def tata_data():
    '''
    Takes the consolidated data of Tata Steel and formats it and returns a dictionary
    with the asset datas of Tata Steel, Tata Motors, Titan Watches and Tata Chemicals,
    all subsidiaries of the Tata Group. 
    '''
    import pandas as pd
    rets = pd.read_csv('TATASTEEL.NS - Consolidated.csv', header = 0, index_col = 0, parse_dates = True, na_values = ('X', 'null'))
    rets.columns.str.rstrip()
    columns = ['Open_T0', 'High_T0', 'Close_T0', 'AdjClose_T0','Volume_T0']
    steel = rets[columns]
    columns1 = ['Open_S1', 'High_S1', 'Close_S1', 'AdjClose_S1','Volume_S1']
    motors = rets[columns1]
    columns2 = ['Open_S2', 'High_S2', 'Close_S2', 'AdjClose_S2','Volume_S2']
    titan = rets[columns2]
    columns3 = ['Open_S3', 'High_S3', 'Close_S3', 'AdjClose_S3','Volume_S3']
    chem = rets[columns3]
    steel.columns = ['Open', 'High', 'Close', 'Adjusted Close', 'Volume']
    motors.columns = ['Open', 'High', 'Close', 'Adjusted Close', 'Volume']
    titan.columns = ['Open', 'High', 'Close', 'Adjusted Close', 'Volume']
    chem.columns = ['Open', 'High', 'Close', 'Adjusted Close', 'Volume']
    out = {'Steel': steel, 'Motors': motors, 'Titan': titan, 'Chemicals' : chem}
    return out

def steel_data():
    '''
    Takes the consolidated data of competitors of Tata Steel and formats it and returns 
    a dictionary with the asset datas of JSW Steel, Jindal Steel and Sail,
    all subsidiaries of the Tata Group. 
    '''
    import pandas as pd 
    rets = pd.read_csv('TATASTEEL.NS - Consolidated.csv', header = 0, index_col = 0, parse_dates = True, na_values = ('X', 'null'))
    rets.columns.str.rstrip()
    columns = ['Open_C1', 'High_C1', 'Close_C1', 'AdjClose_C1','Volume_C1']
    jsw = rets[columns]
    columns1 = ['Open_C2', 'High_C2', 'Close_S2', 'AdjClose_S2','Volume_S2']
    jindal = rets[columns1]
    columns2 = ['Open_C3', 'High_C3', 'Close_C3', 'AdjClose_C3','Volume_C3']
    sail = rets[columns2]
    columns3 = ['Open_T0', 'High_T0', 'Close_T0', 'AdjClose_T0','Volume_T0']
    tata = rets[columns3]
    tata.columns = ['Open', 'High', 'Close', 'Adjusted Close', 'Volume']
    jsw.columns = ['Open', 'High', 'Close', 'Adjusted Close', 'Volume']
    sail.columns = ['Open', 'High', 'Close', 'Adjusted Close', 'Volume']
    jindal.columns = ['Open', 'High', 'Close', 'Adjusted Close', 'Volume']
    out = {'Tata Steel': tata, 'JSW Steel': jsw, 'Jindal Steel': jindal, 'SAIL' : sail}
    return out

def tata_open():
    '''
    Returns the daily opening prices of Tata Steel, Tata Motors, Tata Chemicals and Titan
    during the period 2017 - 2020. 
    '''
    import pandas as pd
    dat = tata_data()
    out = pd.DataFrame({
        'Tata Steel': dat['Steel']['Open'],
        'Tata Motors': dat['Motors']['Open'],
        'Titan': dat['Titan']['Open'],
        'Tata Chemicals': dat['Chemicals']['Open']
    })
    return out

def close(r: pd.DataFrame):
    '''
    Returns the daily closing prices of a pandas DataFrame of given stocks. 
    '''
    dat = r
    out = pd.DataFrame()
    for k,v in dat.items():
        out[k] = v['Close']
    return out
        

def aclose(r: pd.DataFrame):
    '''
    Returns the daily adjusted closing prices of a pandas DataFrame of given stocks. 
    '''
    dat = r
    out = pd.DataFrame()
    for k,v in dat.items():
        out[k] = v['Adjusted Close']
    return out
