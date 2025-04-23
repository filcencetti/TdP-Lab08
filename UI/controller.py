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
        id = ""
        for nerc in self._model.listNerc:
            if nerc._value == self._view._ddNerc.value:
                id = nerc.id
                break
        self.worst_case = self._model.worstCase(Nerc(id,self._view._ddNerc.value),
                                                self._view._txtYears.value, self._view._txtHours.value)

    def fillDD(self):
        nercList = self._model.listNerc

        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v
