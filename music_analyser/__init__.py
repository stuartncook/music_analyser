__version__ = '0.1.0'

import zipfile
from io import BytesIO

import pandas as pd


def read_ytm_takeout(filename: str):
    """Read the YouTube Music play history from a Google Takeout Zip file

    Parameters
    ----------
    filename : str
        the Google Takeout Zip file path

    Returns
    -------
    pd.DataFrame
        a Pandas DataFrame containing the time, artist and song columns
    """
    archive = zipfile.ZipFile(filename)
    df = pd.read_json(
        BytesIO(
            archive.read("Takeout/YouTube and YouTube Music/history/watch-history.json")
        )
    )
    df.time = pd.to_datetime(df.time)
    df = df[df.header=="YouTube Music"]
    df = df.join(df.subtitles.str[0].apply(pd.Series))
    df = df[df.name.str[-6:] == " Topic"]
    df['artist'] = df.name.str[:-8]
    df['song'] = df.title.str[8:]
    return df[['time','artist','song']]
