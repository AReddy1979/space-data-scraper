import os
import sys
import unittest
import random

#current_dir = os.path.dirname(os.path.realpath(__file__))
#parent_dir = os.path.dirname(current_dir)
#sys.path.append(parent_dir)

from src.alerts_backend import Alerts


class AlertsTestCase(unittest.TestCase):

    def test_get_alert_gives_same_output(self):
        self.assertEqual(Alerts.get_alert(), Alerts.get_alert())

    def test_custom_alert_no_alert(self):
        account = Alerts()
        account.customize_alerts(False, False, False)
        custom_string = account.get_custom_alert()
        self.assertFalse("Density" in custom_string)
        self.assertFalse("Speed" in custom_string)
        self.assertFalse("Temperature" in custom_string)

    def test_custom_alert_density(self):
        account = Alerts()
        account.customize_alerts(True, False, False)
        custom_string = account.get_custom_alert()
        self.assertTrue("Density" in custom_string)
        self.assertFalse("Speed" in custom_string)
        self.assertFalse("Temperature" in custom_string)

    def test_custom_alert_speed(self):
        account = Alerts()
        account.customize_alerts(False, True, False)
        custom_string = account.get_custom_alert()
        self.assertFalse("Density" in custom_string)
        self.assertTrue("Speed" in custom_string)
        self.assertFalse("Temperature" in custom_string)

    def test_custom_alert_temperature(self):
        account = Alerts()
        account.customize_alerts(False, False, True)
        custom_string = account.get_custom_alert()
        self.assertFalse("Density" in custom_string)
        self.assertFalse("Speed" in custom_string)
        self.assertTrue("Temperature" in custom_string)

    def test_custom_alert_density_and_speed(self):
        account = Alerts()
        account.customize_alerts(True, True, False)
        custom_string = account.get_custom_alert()
        self.assertTrue("Density" in custom_string)
        self.assertTrue("Speed" in custom_string)
        self.assertFalse("Temperature" in custom_string)

    def test_custom_alert_density_and_temperature(self):
        account = Alerts()
        account.customize_alerts(True, False, True)
        custom_string = account.get_custom_alert()
        self.assertTrue("Density" in custom_string)
        self.assertFalse("Speed" in custom_string)
        self.assertTrue("Temperature" in custom_string)

    def test_custom_alert_speed_and_temperature(self):
        account = Alerts()
        account.customize_alerts(False, True, True)
        custom_string = account.get_custom_alert()
        self.assertFalse("Density" in custom_string)
        self.assertTrue("Speed" in custom_string)
        self.assertTrue("Temperature" in custom_string)

    def test_custom_alert_all_alerts(self):
        account = Alerts()
        account.customize_alerts(True, True, True)
        custom_string = account.get_custom_alert()
        self.assertTrue("Density" in custom_string)
        self.assertTrue("Speed" in custom_string)
        self.assertTrue("Temperature" in custom_string)

    def test_custom_alert_initially_same_get_alert(self):
        account = Alerts()
        custom_string = account.get_custom_alert()
        self.assertEqual(custom_string, Alerts.get_alert())

    def test_custom_can_be_different_than_get_alert(self):
        account = Alerts()
        account.customize_alerts(False, True, True)
        custom_string = account.get_custom_alert()
        self.assertNotEqual(custom_string, Alerts.get_alert())




