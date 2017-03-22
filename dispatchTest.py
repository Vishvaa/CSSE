from unittest import TestCase
import urllib
import softwareprocess.dispatch as dspt


class dispatch(TestCase):
    # def setUpClass(cls):
    #     cls.errorDict = {'error':'true'}

# Happy Path tests

    # Should calculate altitude on all the values provided          Done
    # Should calculate altitude on missing height                   Done
    # Should calculate altitude on missing pressure                 Done
    # Should calculate altitude on missing temperature              Done
    # Should calculate altitude on missing horizon                  Done
    # Should calculate altitude from observation                    Done
    # Should pass with extra info provided                          Done



    # Should calculate Altitude with missing value of height        Done
    # Should calculate Altitude with missing value of pressure      Done
    # Should calculate Altitude with missing value of horizon
    # Should calculate Altitude with missing value of temperature   Done

    # def test_100_010_ShouldCalculateAltitudeWithMandatoryInformation(self):
    #     param = {'observation': '45d15.2', 'height': '6.0', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71',}
    #     expectedparam = {'altitude': '45d11.9', 'observation': '45d15.2', 'height': '6.0', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
    #     self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with All Mandatory Information Provided.")
    #
    # def test_100_020_ShouldcalculateAltitudewithoutHeight(self):
    #     param = {'observation': '45d15.2', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
    #     expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
    #     self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Height.")
    #
    # def test_100_030_ShouldCalculateAltitudeWithMandatoryInformation(self):
    #     param = {'observation': '45d15.2', 'height': '6.0', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71','extra':'extra'}
    #     expectedparam = {'altitude': '45d11.9', 'observation': '45d15.2', 'height': '6.0', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71','extra':'extra'}
    #     self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Extra Information Provided.")
    #
    # def test_100_040_ShouldcalculateAltitudewithoutPressure(self):
    #     param = {'observation': '45d15.2', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
    #     expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
    #     self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Pressure.")
    #
    # def test_100_050_ShouldcalculateAltitudewithoutTemperature(self):
    #     param = {'observation': '45d15.2', 'horizon': 'natural', 'op': 'adjust'}
    #     expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'horizon': 'natural', 'op': 'adjust'}
    #     self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Temperature.")
    #
    # def test_100_060_ShouldcalculateAltitudewithoutHorizon(self):
    #     param = {'observation': '42d0.0', 'op': 'adjust'}
    #     expectedparam = {'altitude': '41d59.0', 'observation': '42d0.0', 'op': 'adjust'}
    #     self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Horizon.")
    #
    #
    # def test_100_070_ShouldcalculateAltitudewithoutAllOptionalValues(self):
    #     param = {'observation': '45d15.2', 'op': 'adjust'}
    #     expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'op': 'adjust'}
    #     self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing All Optional Values.")
    #
    # def test_200_010_ShouldcalculateAltitudewithBlankHeight(self):
    #     param = {'observation': '45d15.2', 'op': 'adjust', 'height':''}
    #     expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'op': 'adjust','height':''}
    #     self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Value of height.")
    #
    # def test_200_020_ShouldcalculateAltitudewithBlankPressure(self):
    #     param = {'observation': '45d15.2', 'op': 'adjust', 'height':'', 'pressure':''}
    #     expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'op': 'adjust','height':'', 'pressure':''}
    #     self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Value of pressure.")
    #
    # def test_200_030_ShouldcalculateAltitudewithBlankTemperature(self):
    #     param = {'observation': '45d15.2', 'op': 'adjust', 'height':'', 'pressure':'','temperature':''}
    #     expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'op': 'adjust','height':'', 'pressure':'','temperature':''}
    #     self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Value of temperature.")

    def test_200_040_ShouldcalculateAltitudewithBlankHorizon(self):
        param = {'observation': '10d0', 'op': 'adjust','horizon':'artifical', 'height':'6.0', 'pressure':'1010','temperature':'72'}
        expectedparam = {'altitude': '9d55.7', 'observation': '10d0', 'op': 'adjust','horizon':'artifical','height':'6.0', 'pressure':'1010','temperature':'72'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Value of horizon.")
        print dspt.dispatch(param)
# Sad Path Tests

    # Should generate error on wrong observation input
    # Should generate error on wrong height input
    # Should generate error on wrong pressure input
    # Should generate error on wrong horizon input
    # Should generate error on wrong temperature input
    # Should generate error on missing mandatory information





