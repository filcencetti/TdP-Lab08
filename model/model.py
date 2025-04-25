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
        for pos in range(len(self._listEvents)-1):
            parziale = [self._listEvents[pos]]
            self.customers = self._listEvents[pos].customers_affected
            self.ricorsione(parziale,maxY,maxH,pos)
        return

    def ricorsione(self, parziale, maxY, maxH, pos):
        # esco dalla funzione se arrivo all'ultimo evento della lista
        if pos == len(self._listEvents) - 1:
            return
        # vincolo sugli anni
        event = self._listEvents[pos + 1]
        event0 = parziale[0]
        difference = event.date_event_finished.year - event0.date_event_began.year
        # vincolo sulle ore
        sum = 0
        for ev in parziale:
            sum += (ev.date_event_finished - ev.date_event_began).total_seconds()
        sum_with_new_event = (sum + (event.date_event_finished - event.date_event_began).total_seconds()) / 3600
        # se aggiungendo un evento i vincoli non sono rispettati esco dalla funzione
        if difference > maxY or sum_with_new_event > maxH:
            # verifico se la soluzione che ho trovato è ottima
            if self.max_customers < self.customers:
                self.max_customers = self.customers
                self.best_seq = deepcopy(parziale)
                self.sum_hours= sum / 3600
            return

        # se l'evento rispetta i vincoli, lo aggiungo, aggiorno il totale e invoco di nuovo la funzione, passando l'indice dell'evento successivo
        else:
            parziale.append(event)
            self.customers += event.customers_affected
            self.ricorsione(parziale, maxY, maxH, pos+1)


    def loadEvents(self, nerc):
        self._listEvents = sorted(DAO.getAllEvents(nerc), key=lambda event: event.date_event_began)


    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc