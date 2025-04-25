from copy import deepcopy

from database.DAO import DAO


class Model:
    def __init__(self):
        self._solBest = []
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()
        self.best_seq = []
        self.max_customers = 0
        self.customers = 0
        self.sum_hours = 0

    def worstCase(self, nerc, maxY, maxH):
        self.loadEvents(nerc)
        parziale = []
        self.ricorsione(parziale, maxY, maxH, 0)

    def ricorsione(self, parziale, maxY, maxH, pos):
        sum = 0
        for ev in parziale:
            sum += (ev._date_event_finished - ev._date_event_began).total_seconds()

        if sum / 3600 > maxH:
            return

        self.customers = 0
        for ev in parziale:
            self.customers += ev.customers_affected
        if self.max_customers < self.customers:
                self.max_customers = self.customers
                self.best_seq = deepcopy(parziale)
                self.sum_hours= sum / 3600

        i = pos
        for e in (self._listEvents[pos:]):
            parziale.append(e)
            if parziale[-1].date_event_finished.year - parziale[0].date_event_began.year > maxY:
                parziale.remove(e)
                return
            i += 1
            self.ricorsione(parziale, maxY, maxH, i)
            parziale.remove(e)


    def loadEvents(self, nerc):
        self._listEvents = sorted(DAO.getAllEvents(nerc), key=lambda event: event.date_event_began)


    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc