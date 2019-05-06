import pandas as pd
import matplotlib.pyplot as plt 
import networkx as nx 

#Importing data
data = pd.read_csv('Full-table.csv')
data = data.head(100) #removing data to speed up graph


#Preprocessing
data['Tm_year'] = data['Tm'] + [str(i) for i in data['Year']]
tm_year_dict = {i:[] for i in data['Tm_year']}
for index, player_id in enumerate(data['ID']):
    tm_year_dict[data['Tm_year'][index]].append(player_id)

#Dictionary to change player ids to player names
id_to_name = {data['ID'].loc[i]: data['Player'].loc[i] for i in range(len(data))}

#initilizing the graph dictionary
player_dict = {i:set() for i in data['ID']}

#Filling up the data
for team in tm_year_dict:
    for player in tm_year_dict[team]:
        gen = (teammate for teammate in tm_year_dict[team] if teammate != player)
        for i in gen:
            player_dict[player].add(i)

#changing player_dict from a dict of sets to s dict of list
for player in player_dict:
    player_dict[player] = list(player_dict[player])

#initilizing empty graph
G = nx.Graph()
#filling up graph with the constructed player_dict
G = nx.convert.from_dict_of_lists(player_dict)

#Plotting graph
plt.figure(figsize=(30,30))
nx.draw_shell(G, with_labels=True, font_weight='bold', font_size=10, node_size=10)
plt.show()