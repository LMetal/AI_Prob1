import pysmile
import pysmile_license
import random


def init_by_definition(node):
    values = list(range(len(net.get_node_definition(node))))  # Lista degli indici
    probabilities = net.get_node_definition(node)  # Probabilità associate

    r = random.choices(values, weights=probabilities, k=1)  # Campionamento pesato
    net.set_evidence(node, r[0])
    print(node, " campiono ", net.get_evidence_id(node))

    net.update_beliefs()


def set_evidence(node):
    values = list(range(len(net.get_node_value(node))))  # Lista degli indici
    probabilities = net.get_node_value(node)  # Probabilità associate
    state_names = net.get_outcome_ids(node)

    if probabilities.count(1) == 1:  # se c'è solo una possibilità
        net.set_evidence(node, probabilities.index(1))
    else:
        print("\n\nImpostare risultato nodo " + node)
        print("N\tState")
        print("--------------------")
        for n, state, prob in zip(values, state_names, probabilities):
            print(f"{n}\t{state}") #print(f"{n}\t{state}\t\t{prob:.2f}")
        n = int(input("Quale N? : "))
        net.set_evidence(node, n)

    print(node, " settato a  ", net.get_evidence_id(node))
    net.update_beliefs()


def take_choice(node):
    print("\n\nEffettuare ", node, "? [si, no]")

    value = net.get_node_value(node)
    print("Scelta\t:\tUtilità")
    print("-------------------")
    print(f"si\t\t:\t{value[0]:.2f}")
    print(f"no\t\t:\t{value[1]:.2f}")

    if input("Scelta: ") == "si":
        net.set_evidence(node, "Si")
    else:
        net.set_evidence(node, "No")
    net.update_beliefs()


def problema1():
    net.read_file("Problema1.xdsl");
    net.clear_all_evidence()
    net.update_beliefs()

    # random mercato
    # init_by_definition("Mercato")

    take_choice("Ricerca")

    set_evidence("Stima_mercato")

    take_choice("Sviluppa_prototipo")

    set_evidence("Qualità_finale")

    #set_evidence("Probabilità_di_profitto")  # ???

    take_choice("Procedere_con_produzione")

    print("Utilità totale: " + str(net.get_node_value("Utilità_finale")[0]))


if __name__ == "__main__":
    net = pysmile.Network()
    problema1()
