import flet as ft

from model.nerc import Nerc


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()

    def handleWorstCase(self, e):
        self._view._txtOut.controls.clear()
        id = ""
        for nerc in self._model.listNerc:
            if nerc._value == self._view._ddNerc.value:
                id = nerc.id
                break
        if self._view._txtYears.value is None or self._view._txtHours.value is None or self._view._txtHours.value == "" or self._view._txtYears.value == "":
            return self._view.create_alert("Inserisci i valori!")

        self._model.worstCase(Nerc(id,self._view._ddNerc.value),int(self._view._txtYears.value), int(self._view._txtHours.value))

        # TEXT OUTPUT
        self._view._txtOut.controls.append(ft.Text(f"Tot people affected: {self._model.max_customers}"))
        self._view._txtOut.controls.append(ft.Text(f"Tot hours of outage: {self._model.sum_hours}"))
        for event in self._model.best_seq:
            self._view._txtOut.controls.append(ft.Text(event))

        self._view.update_page()


    def fillDD(self):
        nercList = self._model.listNerc

        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v
