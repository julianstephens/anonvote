from anonvote.models import Poll
from flask_seeder import Seeder, Faker, generator


class PollSeeder(Seeder):
    def run(self):
        faker = Faker(cls=Poll, init={
            "id_num": generator.Sequence(),
            "name": generator.
            })
