import matplotlib.pyplot as plt
import networkx as nx
from urllib.request import urlopen
import json
import tkinter as tk
import tkinter.messagebox




file = urlopen("https://data.transportation.gov/resource/4f3n-jbg2.json?year=2022")


flights = json.loads(file.read())
print(flights[0])

#G = nx.Graph()
G = nx.DiGraph()

#------------------------
# direct flights

for flight in flights:
    city1 = flight["city1"].split(',')[0].strip()
    city2 = flight["city2"].split(',')[0].strip()
    fare = float(flight["fare"])
    #print("Flight from " + city1 + " to " + city2)
    G.add_edge(city1, city2, weight=fare)
    G.add_edge(city2, city1, weight=fare)

#city1 = input("Enter first city: ")
#city2 = input("Enter second city: ")

window = tk.Tk()
window.title("Flight Planner")
window.geometry("500x300")

outputLabel = tk.Label(window, text="", bg="light blue", width=50, height=10, wraplength=400)
outputLabel.grid(row=4, column=1, columnspan=2)


def button1Click():
  print("Button clicked")
  city1 = entry1.get().split(',')[0].strip()
  city2 = entry2.get().split(',')[0].strip()
 

  


  
  #code help below from chatgpt

  if G.has_edge(city1, city2):
      price = G[city1][city2]["weight"]
      outputLabel.config(text="Direct flight from " + city1 + " to " + city2 + " has a price of $" + str(format(price, '.2f')))
      G_path = nx.path_graph([city1, city2])
      position = nx.spring_layout(G_path)
      nx.draw(G_path, position, with_labels=True, font_weight='bold')
      nx.draw_networkx_edge_labels(G_path, position, edge_labels=nx.get_edge_attributes(G_path, "weight"))
      plt.show()
  
   
  else: #Non-direct flights
    connecting_flights = []
    for flight1 in flights:
      for flight2 in flights:
        if flight1["city1"].split(',')[0].strip() == city1 and flight2["city2"].split(',')[0].strip() == city2 and flight1["city2"].split(',')[0].strip() == flight2["city1"].split(',')[0].strip():
          connecting_flights.append((flight1, flight2))
          price = float(flight1["fare"]) + float(flight2["fare"])
          
          outputLabel.config(text="Connecting flights found between " + city1 + " and " + city2 + " with a price of $" + str(format(price, '.2f')))

  
     
    


   
  
  
      
                                                            
                                                 
          
          
          
        


    
button1 = tk.Button(window, text="Find Flights", 
          bg="salmon", fg="dark blue", width=10, height = 2, 
          command = button1Click)


label1 = tk.Label(window, text="Enter first City", bg="light blue", width=20)
label1.grid(row=1,column=1)

entry1 = tk.Entry(window)
entry1.grid(row=1, column=2)

label2 = tk.Label(window, text="Enter second city", bg="light blue", width=20)
label2.grid(row=2,column=1)

entry2 = tk.Entry(window)
entry2.grid(row=2, column=2)

#entry1 = tk.Entry(window)
#entry2 = tk.Entry(window)
#entry1.grid(row=1, column=2)


button1.grid(row=3, column=1)


window.mainloop()
#------------------------------



#G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1,2),(1,3),(4,1),(2,4)])

pos_spaced = nx.fruchterman_reingold_layout(G, k=0.5, iterations=100)
plt.figure(figsize=(6,10)) # 6x10 inches
nx.draw(G, pos=pos_spaced, with_labels=True) 
nx.draw_networkx_edge_labels(G, pos_spaced,
              edge_labels = nx.get_edge_attributes(G,"weight"))
plt.show(block=False)





'''nx.draw(G, with_labels=True, font_weight='bold')
nx.draw_networkx_edge_labels(G,  nx.spring_layout(G), edge_labels = nx.get_edge_attributes(G, "weight"))


plt.show()'''

