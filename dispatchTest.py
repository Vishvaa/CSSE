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
    # Should calculate Altitude with missing value of horizon       Done
    # Should calculate Altitude with missing value of temperature   Done

    def test_100_010_ShouldCalculateAltitudeWithMandatoryInformation(self):
        param = {'observation': '45d15.2', 'height': '6.0', 'pressure': '100', 'horizon': 'natural', 'op': 'adjust', 'temperature': '-20',}
        print dspt.dispatch(param)
        expectedparam = {'altitude': '45d12.7', 'observation': '45d15.2', 'height': '6.0', 'pressure': '100', 'horizon': 'natural', 'op': 'adjust', 'temperature': '-20'}
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

    def test_100_050_ShouldcalculateAltitudewithoutTemperature(self):
        param = {'observation': '45d15.2', 'horizon': 'natural', 'op': 'adjust'}
        expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'horizon': 'natural', 'op': 'adjust'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Temperature.")

    def test_100_060_ShouldcalculateAltitudewithoutHorizon(self):
        param = {'observation': '42d0.0', 'op': 'adjust'}
        expectedparam = {'altitude': '41d59.0', 'observation': '42d0.0', 'op': 'adjust'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Horizon.")


    def test_100_070_ShouldcalculateAltitudewithoutAllOptionalValues(self):
        param = {'observation': '45d15.2', 'op': 'adjust'}
        expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'op': 'adjust'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing All Optional Values.")

    def test_200_010_ShouldcalculateAltitudewithBlankHeight(self):
        param = {'observation': '45d15.2', 'op': 'adjust', 'height':''}
        expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'op': 'adjust','height':''}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Value of height.")

    def test_200_020_ShouldcalculateAltitudewithBlankPressure(self):
        param = {'observation': '45d15.2', 'op': 'adjust', 'height':'', 'pressure':''}
        expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'op': 'adjust','height':'', 'pressure':''}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Value of pressure.")

    def test_200_030_ShouldcalculateAltitudewithBlankTemperature(self):
        param = {'observation': '45d15.2', 'op': 'adjust', 'height':'', 'pressure':'','temperature':''}
        expectedparam = {'altitude': '45d14.3', 'observation': '45d15.2', 'op': 'adjust','height':'', 'pressure':'','temperature':''}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Value of temperature.")

    def test_200_040_ShouldcalculateAltitudewithBlankHorizon(self):
        param = {'observation': '10d0', 'op': 'adjust','horizon':'artifical', 'height':'6.0', 'pressure':'1010','temperature':'72'}
        expectedparam = {'altitude': '9d54.7', 'observation': '10d0', 'op': 'adjust','horizon':'artifical','height':'6.0', 'pressure':'1010','temperature':'72'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Missing Value of horizon.")

# Sad Path Tests

    # Should generate error on wrong observation input          Done
    # Should generate error on wrong height input               Done
    # Should generate error on wrong pressure input             Done
    # Should generate error on wrong horizon input              Done
    # Should generate error on wrong temperature input
    # Should generate error on missing mandatory information

    def test_300_010_ShouldGenerateErrorOnWrongObservationDegree(self):
        param = {'observation': '100d0', 'op': 'adjust','horizon':'artifical', 'height':'6.0', 'pressure':'1010','temperature':'72'}
        expectedparam = {'observation': '100d0', 'op': 'adjust','horizon':'artifical','height':'6.0', 'pressure':'1010','temperature':'72','error': 'observation is invalid'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Invalid value of Observation Degree.")

    def test_300_020_ShouldGenerateErrorOnWrongObservationDegree(self):
        param = {'observation': '-10d0', 'op': 'adjust','horizon':'artifical', 'height':'6.0', 'pressure':'1010','temperature':'72'}
        expectedparam = {'observation': '-10d0', 'op': 'adjust','horizon':'artifical','height':'6.0', 'pressure':'1010','temperature':'72','error': 'observation is invalid'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Invalid value of Observation Degree.")

    def test_300_030_ShouldGenerateErrorOnWrongObservationDegree(self):
        param = {'observation': '10d60.1', 'op': 'adjust','horizon':'artifical', 'height':'6.0', 'pressure':'1010','temperature':'72'}
        expectedparam = {'observation': '10d60.1', 'op': 'adjust','horizon':'artifical','height':'6.0', 'pressure':'1010','temperature':'72','error': 'observation is invalid'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Invalid value of Observation Degree.")


    def test_300_040_ShouldGenerateErrorOnWrongObservationDegree(self):
        param = {'observation': '10d-0.1', 'op': 'adjust','horizon':'artifical', 'height':'6', 'pressure':'1010','temperature':'72'}
        expectedparam = {'observation': '10d-0.1', 'op': 'adjust','horizon':'artifical','height':'6', 'pressure':'1010','temperature':'72','error': 'observation is invalid'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Invalid value of Observation Degree.")

    def test_300_050_ShouldGenerateErrorOnWrongHeight(self):
        param = {'observation': '10d50', 'op': 'adjust','horizon':'artifical', 'height':'-1', 'pressure':'1010','temperature':'72'}
        expectedparam = {'observation': '10d50', 'op': 'adjust','horizon':'artifical','height':'-1', 'pressure':'1010','temperature':'72','error': 'Height is invalid'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Invalid value of Height.")

    def test_300_060_ShouldGenerateErrorOnWrongHeight(self):
        param = {'observation': '10d50', 'op': 'adjust','horizon':'artifical', 'height':'a', 'pressure':'1010','temperature':'72'}
        expectedparam = {'observation': '10d50', 'op': 'adjust','horizon':'artifical','height':'a', 'pressure':'1010','temperature':'72','error': 'Height is invalid'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Invalid value of Height.")

    def test_300_070_ShouldGenerateErrorOnWrongPressure(self):
        param = {'observation': '10d50', 'op': 'adjust','horizon':'artifical', 'height':'5', 'pressure':'25','temperature':'72'}
        print dspt.dispatch(param)
        expectedparam = {'observation': '10d50', 'op': 'adjust','horizon':'artifical','height':'5', 'pressure':'25','temperature':'72','error': 'Pressure is invalid'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Invalid value of Pressure.")

    def test_300_080_ShouldGenerateErrorOnWrongPressure(self):
        param = {'observation': '10d50', 'op': 'adjust','horizon':'artifical', 'height':'5', 'pressure':'1111','temperature':'72'}
        expectedparam = {'observation': '10d50', 'op': 'adjust','horizon':'artifical','height':'5', 'pressure':'1111','temperature':'72','error': 'Pressure is invalid'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Invalid value of Pressure.")

    def test_300_090_ShouldGenerateErrorOnWrongHorizon(self):
        param = {'observation': '10d50', 'op': 'adjust','horizon':'awgsdh', 'height':'5', 'pressure':'1100','temperature':'72'}
        expectedparam = {'observation': '10d50', 'op': 'adjust','horizon':'awgsdh','height':'5', 'pressure':'1100','temperature':'72','error': 'Horizon is invalid'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Invalid value of Pressure.")

    def test_300_100_ShouldGenerateErrorOnWrongTemperature(self):
        param = {'observation': '10d50', 'op': 'adjust','horizon':'artifical', 'height':'5', 'pressure':'1100','temperature':'-21'}
        print dspt.dispatch(param)
        expectedparam = {'observation': '10d50', 'op': 'adjust','horizon':'artifical','height':'5', 'pressure':'1100','temperature':'-21','error': 'Temperature is invalid'}
        self.assertDictEqual(dspt.dispatch(param), expectedparam, "Not Able to pass Dict with Invalid value of Temperature.")
