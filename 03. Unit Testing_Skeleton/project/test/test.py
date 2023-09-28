from project.trip import Trip

from unittest import main, TestCase


class TripTest(TestCase):
    def test_initializaion_correctly_not_family(self):
        test_trip = Trip(234, 3, False)
        self.assertEqual(234, test_trip.budget)
        self.assertEqual(3, test_trip.travelers)
        self.assertFalse(test_trip.is_family)

    def test_initializaion_correctly_family(self):
        test_trip = Trip(234, 3, True)
        self.assertEqual(234, test_trip.budget)
        self.assertEqual(3, test_trip.travelers)
        self.assertTrue(test_trip.is_family)

    def test_initialization_travelers_raises(self):
        with self.assertRaises(ValueError) as ex:
            test_trip = Trip(837, 0, False)
        self.assertEqual('At least one traveler is required!', str(ex.exception))

    def test_initialization_is_family_set_to_False(self):
        test_trip = Trip(425, 1, True)
        self.assertFalse(test_trip.is_family)

    def test_book_a_trip_wrong_destination(self):
        test_trip = Trip(872, 2, False)
        result = test_trip.book_a_trip("Zimbabve")
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_not_enough_budget(self):
        test_trip = Trip(1000, 3, False)
        result = test_trip.book_a_trip("Bulgaria")
        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_not_a_family(self):
        test_trip = Trip(2000, 3, False)
        result = test_trip.book_a_trip("Bulgaria")
        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 500.00', result)
        self.assertEqual({"Bulgaria": 1500}, test_trip.booked_destinations_paid_amounts)

    def test_book_a_trip_a_family(self):
        test_trip = Trip(2000, 3, True)
        result = test_trip.book_a_trip("Bulgaria")
        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 650.00', result)
        self.assertEqual({"Bulgaria": 1350}, test_trip.booked_destinations_paid_amounts)

    def test_booking_status_nothing_booked(self):
        test_trip = Trip(1000, 3, False)
        result = test_trip.booking_status()
        self.assertEqual('No bookings yet. Budget: 1000.00', result)

    def test_booking_status_2_booked(self):
        test_trip = Trip(9000, 1, False)
        test_trip.book_a_trip("Bulgaria")
        test_trip.book_a_trip("New Zealand")
        result = test_trip.booking_status()
        self.assertEqual("Booked Destination: Bulgaria\nPaid Amount: 500.00\nBooked Destination: New Zealand\nPaid Amount: 7500.00\nNumber of Travelers: 1\nBudget Left: 1000.00", result)

    if __name__ == "__main__":
        main()
