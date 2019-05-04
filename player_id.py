def get_player_id(year):
    '''
    Get the player ids from basketball reference for 
    the totals table in a given year
    @param int year: the year for a player
    @rtype list: list of player ids 
    '''
    url = 'http://www.basketball-reference.com/leagues/NBA_{}_totals.html'.format(year)
    website = requests.get(url).text
    soup = bs(website, 'lxml')
    table = soup.find_all('table')[0]
    rows = table.find_all('tr')[1:]
    ids = [i.find_all('td') for i in rows]
    id_list = [i[0]['data-append-csv'] for i in ids if len(i)>0]
    return id_list