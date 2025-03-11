import pysmile
import pysmile_license


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
            if prob == 0:
                continue
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

    scelte = ["si", "no"]
    scelta_consigliata = scelte[value.index(max(value))]
    print(f"AZIONE CONSIGLIATA : {scelta_consigliata} [{max(value):.2f}]")

    if input("Scelta: ") == "si":
        net.set_evidence(node, "Si")
    else:
        net.set_evidence(node, "No")

    net.update_beliefs()


def main():
    net.read_file("Problema1.xdsl")
    net.clear_all_evidence()
    net.update_beliefs()

    take_choice("Ricerca")

    set_evidence("Stima_mercato")

    take_choice("Sviluppa_prototipo")

    set_evidence("Qualità_finale")

    take_choice("Procedere_con_produzione")

    utility = net.get_node_value("Utilità_finale")[0]
    print(f"\n\nUtilità finale: {utility: .2f}")


if __name__ == "__main__":
    net = pysmile.Network()
    main()