from django.core.management.base import BaseCommand
from chatterbot.ext.django_chatterbot.models import Statement
from .import list_train

class Command(BaseCommand):

    def handle(self,**options):
        statement = Statement.objects.all()
        if statement:
            statement.delete()
            self.stdout.write(self.style.SUCCESS('データを削除しました。'))
        list_train.training()
        self.stdout.write(self.style.SUCCESS('トレーニング終了'))

        
