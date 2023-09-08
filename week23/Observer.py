from abc import ABC, abstractmethod


class Station(ABC):

    @abstractmethod
    def registering(self, observer):
        pass

    @abstractmethod
    def unregistering(self, observer):
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class WeatherStation(Station):

    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.observers = []

    def registering(self, observer):
        self.observers.append(observer)
        pass

    def unregistering(self, observer):
        self.observers.remove(observer)

    def notify(self) -> None:
        for observer in self.observers:
            observer.update(self)

    def set_measurements(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, weather_info: WeatherStation) -> None:
        pass


class TemperatureDisplay(Observer):
    print("Temperature Observer Called")

    def update(self, weather_info: WeatherStation):
        print(f'Temperature: {weather_info.temperature}')


class HumidityDisplay(Observer):
    print("Humidity Observer Called")

    def update(self, weather_info: WeatherStation):
        print(f'Humidity: {weather_info.humidity}')


if __name__ == "__main__":
    weather_info = WeatherStation()

    temperature_observer = TemperatureDisplay()
    weather_info.registering(temperature_observer)

    Humidity_observer = HumidityDisplay()
    weather_info.registering(Humidity_observer)

    weather_info.set_measurements(60, 20)
