from book_modu.changed_temperatures_on_my_birthday.models import ChangedTemperaturesOnMyBirthday

if __name__ == '__main__':
    this = ChangedTemperaturesOnMyBirthday()
    this.read_data()
    # this.show_highest_temperature()
    # this.save_highest_temperature()
    # this.visualize_highest_temperature()
    this.highest_temperature_my_birthday()