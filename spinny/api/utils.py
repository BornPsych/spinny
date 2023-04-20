from .models import User, Box
from django.conf import settings
from django.db.models import Avg
from .models import User

def AverageArea():
    average_area = Box.objects.aggregate(Avg("area"))
    if average_area < settings.DATA_MANUPLATION_LIMITS['A1']:
        return True
    else:
        return False

def AverageVolumeForUser(userId):
    user = User.objects.get(id=userId)
    qs = Box.objects.filter(created_by=user)
    average_area = queryset.aggregate(Avg("volume"))
    if average_area < settings.DATA_MANUPLATION_LIMITS['V1']:
        return True
    else:
        return False

def manuallyValidate(area, volume):
        request = self.context['request']
        user = request.user
        d = datetime.datetime.today()
        sunday_offset = (d.weekday() - 6) % 7
        sunday = d - datetime.timedelta(days = sunday_offset)
        Boxes = Box.objects.filter(created_at__gte=sunday)
        countBoxes = Boxes.count() + 1
        Boxes = Boxes.filter(created_by=user)
        countUsersBoxes = Boxes.count() + 1
        if countBoxes >= settings.DATA_MANUPLATION_LIMITS['L1']:
            return False, "max limit for user reached"
        elif countUsersBoxes >= settings.DATA_MANUPLATION_LIMITS['L2']:
            return False, "max weekly limit reached"
        Boxes = Box.objects.filter(created_by=user)
        if Boxes.count() > 0:
            avVolume = (Boxes.aggregate(Sum('volume'))['volume__sum'] + volume) / countBoxes 
            avArea = (Boxes.aggregate(Sum('area'))['area__sum'] + area) / countBoxes
            if avVolume > settings.DATA_MANUPLATION_LIMITS['V1']:
                return False, "max average volume exceeded"
            elif avArea > settings.DATA_MANUPLATION_LIMITS['A1']:
                return False, "max average area exceeded"
        return True, "valid"