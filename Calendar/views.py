from datetime import timedelta

from django.shortcuts import render

from AssetData.models import Asset


def full_calendar(request):
    events = []
    for asset in Asset.objects.all():
        events.append("""
            {{
                title: '{title}',
                start: '{start}',
                end: '{end}'
            }}"""
            .format(
                title=asset.name,
                start=asset.dateRented.isoformat(),
                end=(asset.dateRented + timedelta(days=asset.outLength)).isoformat()
            )
        )
    return render(request, 'calendar.html', {'events': ',\n'.join(events)})