from database.DAO import DAO


class Model:
    def __init__(self):
        self._solBest = []
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()

    def worstCase(self, nerc, maxY, maxH):
        self._listNerc = self.loadEvents(nerc)

        pass

    def ricorsione(self, parziale, maxY, maxH, pos):



        pass

    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc