from unittest import TestCase
import urllib
import softwareprocess.dispatch as dspt


class dispatch(TestCase):
    # def setUpClass(cls):
    #     cls.errorDict = {'error':'true'}

# Happy Path tests

    # Should calculate altitude on all the values provided      Done
    # Should calculate altitude on missing height               Done
    # Should calculate altitude on missing pressure
    # Should calculate altitude on missing temperature
    # Should calculate altitude on missing horizon
    # Should calculate altitude from observation
    # Should pass with extra info provided                      Done

    def test_100_010_ShouldCalculateAltitudeWithMandatoryInformation(self):
        param = {'observation': '45d15.2', 'height': '6.0', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71',}
        expectedparam = {'altitude': '45d11.9', 'observation': '45d15.2', 'height': '6.0', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with All Mandatory Information Provided.")

    def test_100_020_ShouldcalculateAltitudewithoutHeight(self):
        param = {'observation': '45d15.2', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Height.")

    def test_100_030_ShouldCalculateAltitudeWithMandatoryInformation(self):
        param = {'observation': '45d15.2', 'height': '6.0', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71','extra':'extra'}
        expectedparam = {'altitude': '45d11.9', 'observation': '45d15.2', 'height': '6.0', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71','extra':'extra'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Extra Information Provided.")

    def test_100_040_ShouldcalculateAltitudewithoutPressure(self):
        param = {'observation': '45d15.2', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Pressure.")


# Sad Path Tests

    # Should generate error on wrong observation input
    # Should generate error on wrong height input
    # Should generate error on wrong pressure input
    # Should generate error on wrong horizon input
    # Should generate error on wrong temperature input
    # Should generate error on missing mandatory information





