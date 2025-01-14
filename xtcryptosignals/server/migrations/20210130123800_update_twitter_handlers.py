__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongodb_migrations.base import BaseMigration
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.server.api.projects.models import Project
from xtcryptosignals.tasks import settings as s


class Migration(BaseMigration):
    @use_mongodb(db=s.MONGODB_NAME, host=s.MONGODB_HOST, port=s.MONGODB_PORT)
    def upgrade(self):
        Project.objects(coin_or_token="UNI").update(
            twitter="https://twitter.com/Uniswap"
        )
        Project.objects(coin_or_token="LTO").update(
            twitter="https://twitter.com/TheLTONetwork"
        )
        Project.objects(coin_or_token="HBAR").update(
            twitter="https://twitter.com/hedera"
        )

    def downgrade(self):
        pass
