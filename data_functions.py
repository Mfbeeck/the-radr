import pickle

def get_followed_artists():
    pickle_file = open("static/data/followed_artists.pickle",'rb')
    df_followed_artists = pickle.load(pickle_file)
    pickle_file.close()
    return df_followed_artists
