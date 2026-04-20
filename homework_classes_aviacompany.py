class Plane:
    def __init__(self, model: str, tail_number: str):
        self.model = model
        self.tail_number = tail_number

    def __repr__(self):
        return f"Plane({self.tail_number})"


class Pilot:
    def __init__(self, name: str, license_id: str):
        self.name = name
        self.license_id = license_id

    def __repr__(self):
        return f"Pilot({self.name})"


class Flight:
    def __init__(self, flight_id: str, plane: Plane, pilot: Pilot, start_time: int, end_time: int):
        self.flight_id = flight_id
        self.plane = plane
        self.pilot = pilot
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"Flight({self.flight_id}, {self.plane}, {self.pilot}, {self.start_time}-{self.end_time})"


class FlightRepository:
    def __init__(self, all_planes: list, all_pilots: list):
        self._flights = []
        self._all_planes = all_planes
        self._all_pilots = all_pilots

    def add(self, flight: Flight):
        for existing in self._flights:
            if existing.plane is flight.plane and self._overlaps(existing, flight):
                raise ValueError(f"Самолёт {flight.plane.tail_number} уже занят в интервале "
                                 f"[{flight.start_time}, {flight.end_time}) рейсом {existing.flight_id}")
        for existing in self._flights:
            if existing.pilot is flight.pilot and self._overlaps(existing, flight):
                raise ValueError(f"Пилот {flight.pilot.name} уже занят в интервале "
                                 f"[{flight.start_time}, {flight.end_time}) рейсом {existing.flight_id}")
        self._flights.append(flight)

    def get_all(self):
        return self._flights.copy()

    def available_planes(self, window_start: int, window_end: int):
        result = []
        for plane in self._all_planes:
            busy = False
            for flight in self._flights:
                if flight.plane is plane and self._overlaps_interval(flight, window_start, window_end):
                    busy = True
                    break
            if not busy:
                result.append(plane)
        return result

    def available_pilots(self, window_start: int, window_end: int):
        result = []
        for pilot in self._all_pilots:
            busy = False
            for flight in self._flights:
                if flight.pilot is pilot and self._overlaps_interval(flight, window_start, window_end):
                    busy = True
                    break
            if not busy:
                result.append(pilot)
        return result

    @staticmethod
    def _overlaps(flight1: Flight, flight2: Flight) -> bool:
        return not (flight1.end_time <= flight2.start_time or flight1.start_time >= flight2.end_time)

    @staticmethod
    def _overlaps_interval(flight: Flight, window_start: int, window_end: int) -> bool:
        return not (flight.end_time <= window_start or flight.start_time >= window_end)


if __name__ == "__main__":
    plane1 = Plane("Boeing 737", "RA-12345")
    plane2 = Plane("Airbus A320", "RA-54321")
    plane3 = Plane("Boeing 747", "RA-98765")

    pilot1 = Pilot("Иванов Иван", "LIC-001")
    pilot2 = Pilot("Петров Пётр", "LIC-002")
    pilot3 = Pilot("Сидоров Сидор", "LIC-003")

    all_planes = [plane1, plane2, plane3]
    all_pilots = [pilot1, pilot2, pilot3]

    repo = FlightRepository(all_planes, all_pilots)

    flight1 = Flight("SU100", plane1, pilot1, 9, 12)  # 9:00 - 12:00
    flight2 = Flight("SU101", plane2, pilot2, 10, 13)  # 10:00 - 13:00
    repo.add(flight1)
    repo.add(flight2)

    print("Добавлено два рейса.")
    print("Все рейсы:", repo.get_all())

    try:
        flight_conflict = Flight("SU102", plane1, pilot3, 11, 14)  # пересекается с flight1
        repo.add(flight_conflict)
    except ValueError as e:
        print("Ошибка добавления:", e)

    free_planes = repo.available_planes(13, 15)
    print("Свободные самолёты с 13 до 15:", free_planes)

    free_pilots = repo.available_pilots(8, 10)
    print("Свободные пилоты с 8 до 10:", free_pilots)

    flight3 = Flight("SU103", plane3, pilot3, 14, 17)
    repo.add(flight3)
    print("Добавлен рейс", flight3)
    print("Все рейсы:", repo.get_all())

    free_planes_14_16 = repo.available_planes(14, 16)
    print("Самолёты свободные с 14 до 16:", free_planes_14_16)
