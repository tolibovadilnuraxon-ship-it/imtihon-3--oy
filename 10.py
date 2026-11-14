from matplotlib import pyplot

kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]

pyplot.plot(kunlar, daromad, marker="o", linestyle="-.", label="Daromad grafigi", color="red")

pyplot.title("Haftalik daromad grafigi")
pyplot.xlabel("Kunlar")
pyplot.ylabel("Daromad")

pyplot.legend()
pyplot.grid(True)
pyplot.savefig("daromad.png")
pyplot.show()
