def map_uniq(artist_origin, data):
    '''
    Map values from artist_origin dict to Natl column in dataframe
    
    args: art_ori - dict with {artist : nationality} structure
    return: data - dataframe with Natl column of mapped nationalities
    '''

    ## build list of unique artist in df2
    uniq_artists = data.Artist.unique().tolist()
    
    ## get intersection of uniq_artists and artist_origin to filter nationalities not found
    ao_set = set(list(artist_origin.keys()))
    ua_set = set(uniq_artists)
    known_origin = list(ao_set.intersection(ua_set))

    ## set values for Natl column from artist_origin after determining the key exists
    data['Natl'] = df2.Artist.apply(lambda x: artist_origin[x] if x in known_origin else 'not_found') 

    return data

def map_norps(norp_tmp):
    '''
    Map exceptions for countries with multiple NORPs
    '''
    ## make dict out of norps_list for mapping
    norp_dict = dict()
    
    for n in norp_tmp:
        norp_dict[n] = n
        
        if n == 'English':
            norp_dict.update({
                n:'British'
            })
        elif n == 'Saudi Arabian':
            norp_dict.update({
                n:'Saudi'
            })
        elif n == 'Puerto Rican':
            norp_dict.update({
                n:'American'
            })
    return norp_dict
    
    
    


def map_uniq_v1(art_ori, data):
    '''
    Map values from artist_origin dict to Natl column in dataframe
    
    args: art_ori - dict with {artist : nationality} structure
    return: data - dataframe with Natl column of mapped nationalities
    '''
    ## sort index for speed
    data.sort_index(inplace = True)
    ## build list of unique artist in df2
    uniq_art = data.Artist.unique().tolist()
    ## build list of artist for whom we already know origins to skip in processing
    skip_keys = [i for i in list(art_ori.keys()) if i in uniq_art]
    ## set values for Natl column from artist_origin dict after determining the key exists & preview result
    data['Natl'] = data.Artist.apply(lambda x: art_ori[x] if x in skip_keys else 'not_found')
    return data