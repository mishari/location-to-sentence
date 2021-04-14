import random
from random import choice as ch
import csv

random.seed(5113711941)

def read_location_csv(filename):

    locations = []

    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            locations.append((row[1],row[4],row[7]))

    return locations


def generate_tambons(persons, particles, actions, from_str, to_str, locations):
    random.shuffle(locations)
    sentences = set()

    for i,k in zip(locations[0::2], locations[1::2]):
        new_text = "%s%s%sจาก%s %s ไป%s %s" % (ch(persons), ch(particles), ch(actions), i[2], i[1], k[2], k[1])
        sentences.add(new_text)

    return sentences

if __name__ == "__main__":
    PERSONS = ["พ่อ","แม่","เรา"]
    PARTICLE = ["เคย","จะ"]
    ACTION = ["ปั่นจักรยาน", "ขับรถ"]
    FROM = ["จาก"]
    TO = ["ไป"]
    f = "../data/geocode-1.csv"
    locations = read_location_csv(f)
    for t in generate_tambons(PERSONS, PARTICLE, ACTION, FROM, TO, locations):
        print(t)