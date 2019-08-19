import pickle

def get_followed_artists():
    pickle_file = open("static/data/followed_artists.pickle",'rb')
    df_followed_artists = pickle.load(pickle_file)
    pickle_file.close()
    return df_followed_artists

def get_top_tracks():
    pickle_file = open("static/data/top_tracks.pickle",'rb')
    df_top_tracks = pickle.load(pickle_file)
    pickle_file.close()
    return df_top_tracks   

def get_top_artists():
    pickle_file = open("static/data/top_artists.pickle",'rb')
    df_top_artists = pickle.load(pickle_file)
    pickle_file.close()
    return df_top_artists
