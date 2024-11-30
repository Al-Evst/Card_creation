from file_operations import read_file, render_template
from faker import Faker
import random
import json 
import os

def main():

    os.makedirs("images", exist_ok=True)
    skill = read_file("Skills.txt")
    let = read_file('letters_maping.txt') 
    fake = Faker("ru_RU")
    sortys = let.replace("\'","\"")
    js = json.loads(sortys)
    skill = skill.split("\n")
    for number in range(10):
        sort_ = random.sample(skill, 3)
        runic_skills = []  
        for skil in sort_: 
            for letter in skil:
                if letter in js:
                    skil = skil.replace(letter, js[letter])
            runic_skills.append(skil)
        context = {
          "first_name": fake.first_name(),
          "last_name": fake.last_name(),
          "job": fake.job(),
          "town": fake.city(),
          "strength": random.randint(3, 18),
          "agility": random.randint(3, 18),
          "endurance": random.randint(3, 18),
          "intelligence": random.randint(3, 18),
          "luck": random.randint(3, 18),
          "skill_1": runic_skills[0],
          "skill_2": runic_skills[1],
          "skill_3" : runic_skills[2]
        }
        render_template("charsheet.svg","images/{}result.svg".format(number), context)
if __name__ == '__main__':
    main()