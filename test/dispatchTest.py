from unittest import TestCase
import urllib

import softwareprocess.dispatch as dspt

class dispatch(TestCase):
    def setUpClass(cls):
        cls.errorDict = {'error':'true'}

# Happy Path tests

    # Should calculate altitude on all the values provided
    # Should calculate altitude on missing height
    # Should calculate altitude on missing pressure
    # Should calculate altitude on missing temperature
    # Should calculate altitude on missing horizon

    def test_100_010_ShouldCalculateAltitudeWithMandatoryInformation(self):
        param = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        expectedparam = {'altitude': '29d59.9', 'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam)






# Sad Path Tests

    # Should generate error on wrong observation input
    # Should generate error on wrong height input
    # Should generate error on wrong pressure input
    # Should generate error on wrong horizon input
    # Should generate error on wrong temperature input
    # Should generate error on missing mandatory information





