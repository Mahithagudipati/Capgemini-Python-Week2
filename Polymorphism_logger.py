# Polymorphism
# •	11. Create a class `Logger` with a method `log(message)`. Implement method overloading to log different message types (`error`, `warning`, `info`).
# •	12. Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.
# •	13. Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
# •	14. Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
# •	15. Write an example where `Operator Overloading` is used to concatenate two `Book` objects, treating them as a series.


class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        if message == "error":
            print("Log: ERROR")
            self.logs.append("ERROR")
        elif message == "warning":
            print("Log: WARNING")
            self.logs.append("WARNING")
        elif message == "info":
            print("Log: INFO")
            self.logs.append("INFO")
        else:
            print("Log: Unknown")
            self.logs.append("Unknown")


def main():
    logger = Logger()
    while True:
        msg = input("Enter the log (enter 'exit' to exit): ")
        if msg == 'exit':
            break
        logger.log(msg)
    print(f"The logs are: {logger.logs}")

main()