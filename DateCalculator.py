class DateCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_day_of_week(self):
        
        adjusted_month = self.month
        adjusted_year = self.year

        if adjusted_month == 1 or adjusted_month == 2:
            adjusted_month += 12
            adjusted_year -= 1

        q = self.day
        m = adjusted_month
        K = adjusted_year % 100  
        J = adjusted_year // 100  

        #Zeller's formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        day_names = {
            0: "Saturday",
            1: "Sunday",
            2: "Monday",
            3: "Tuesday",
            4: "Wednesday",
            5: "Thursday",
            6: "Friday"
        }

        return day_names[h]

if __name__ == "__main__":
    date = DateCalculator(1589, 9, 15)
    print("Day of the week:", date.get_day_of_week())
