from i2s.i2s import *

TEST_PERSONS = ["พ่อ","แม่","เรา"]
TEST_PARTICLE = ["เคย","จะ"]
TEST_ACTION = ["ปั่นจักรยาน", "ขับรถ"]
TEST_FROM = ["จาก"]
TEST_TO = ["ไป"]
TEST_LOCATION = [("จังหวัด1","อำเภอ1","ตำบล1"),
            ("จังหวัด1", "อำเภอ2", "ตำบล2"),
            ("จังหวัด3", "อำเภอ3", "ตำบล3"),
            ("จังหวัด4", "อำเภอ4", "ตำบล4")
            ]

def test_generate_district():
    assert 'แม่จะขับรถจากตำบล3 อำเภอ3 ไปตำบล4 อำเภอ4' in generate_tambons(TEST_PERSONS, TEST_PARTICLE, TEST_ACTION, TEST_FROM, TEST_TO, TEST_LOCATION)