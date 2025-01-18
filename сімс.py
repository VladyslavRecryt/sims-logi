import random
import logging

logging.basicConfig(
    filename="tests.log",  
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_error(func, e):
    logging.error(f"Error in {func.__name__}: {str(e)}")


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}


brands_of_car = {
    "Toyota": {"fuel": 100, "strength": 100, "consumption": 10},
    "BMW": {"fuel": 80, "strength": 120, "consumption": 12},
    "Ford": {"fuel": 90, "strength": 110, "consumption": 9},
    "Honda": {"fuel": 95, "strength": 105, "consumption": 8},
}

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            logging.info(f"{self.brand} is driving. Fuel: {self.fuel}, Strength: {self.strength}")
            return True
        else:
            logging.warning(f"{self.brand} cannot drive. Fuel: {self.fuel}, Strength: {self.strength}")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()
        logging.info(f"{self.name} got a new home.")

    def get_car(self):
        self.car = Auto(brands_of_car)
        logging.info(f"{self.name} bought a {self.car.brand} car.")

    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
            logging.info(f"{self.name} got a new job as a {self.job.job} with salary {self.job.salary}.")
        else:
            logging.warning(f"{self.name} can't get a job, car needs repair.")
            self.to_repair()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
            logging.info(f"{self.name} ate. Satiety: {self.satiety}, Food left: {self.home.food}.")

    def work(self):
        if self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
            logging.info(f"{self.name} worked. Money: {self.money}, Gladness: {self.gladness}, Satiety: {self.satiety}.")
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()

    def shopping(self, manage):
        if manage == "fuel":
            logging.info(f"{self.name} bought fuel.")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            logging.info(f"{self.name} bought food.")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            logging.info(f"{self.name} bought delicacies. Gladness increased.")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        logging.info(f"{self.name} chilled. Gladness: {self.gladness}, Mess: {self.home.mess}.")

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        logging.info(f"{self.name} cleaned the house. Gladness: {self.gladness}.")

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
        logging.info(f"{self.name} repaired the car. Money: {self.money}, Car strength: {self.car.strength}.")

    def days_indexes(self, day):
        day_str = f" Today is day {day} of {self.name}'s life "
        logging.info(f"{day_str:=^50}")
        logging.info(f"{self.name}'s indexes")
        logging.info(f"Money – {self.money}")
        logging.info(f"Satiety – {self.satiety}")
        logging.info(f"Gladness – {self.gladness}")
        logging.info(f"Food – {self.home.food}")
        logging.info(f"Mess – {self.home.mess}")
        logging.info(f"{self.car.brand} car indexes")
        logging.info(f"Fuel – {self.car.fuel}")
        logging.info(f"Strength – {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            logging.warning(f"{self.name} fell into depression.")
            return False
        if self.satiety < 0:
            logging.warning(f"{self.name} died of hunger.")
            return False
        if self.money < -500:
            logging.warning(f"{self.name} went bankrupt.")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            logging.info(f"{self.name} is no longer alive.")
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            logging.info(f"{self.name} is hungry, going to eat.")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                logging.info(f"{self.name} wants to chill but needs to clean.")
                self.clean_home()
            else:
                logging.info(f"{self.name} decided to chill!")
                self.chill()
        elif self.money < 0:
            logging.info(f"{self.name} is working to earn money.")
            self.work()
        elif self.car.strength < 15:
            logging.info(f"{self.name} is repairing the car.")
            self.to_repair()
        elif dice == 1:
            logging.info(f"{self.name} decided to chill.")
            self.chill()
        elif dice == 2:
            logging.info(f"{self.name} decided to work.")
            self.work()
        elif dice == 3:
            logging.info(f"{self.name} is cleaning the house.")
            self.clean_home()
        elif dice == 4:
            logging.info(f"{self.name} bought some delicacies!")
            self.shopping("delicacies")

nick = Human(name="Nick")
for day in range(1, 8):
    if not nick.live(day):
        break
