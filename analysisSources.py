import re
import locale
p = re.compile(ur'\((\d+):(\d+),(\d+)\)')

locale.setlocale(locale.LC_ALL, 'en_US')

indexToSource = [
    'nrt',
    'flurry',
    'bkd',
    'adw',
    'datax',
    'dac',
    'premium_audience',
    'yamp_impression',
    'yamp_click',
    'yamp_action',
    'yamp_beacon',
    'dot_pixel',
    'nrt_dotconv',
    'urs_keyword',
    'mx3_click',
    'mx3_action',
    'taxonomy',
    'datax_custom_audience',
    'cluster_profile',
    'lookalike',
    'mx3_impression',
    'benzene',
    'language',
    'urs_optout',
    'polka',
    'cross_device',
    'bkd_instrument',
    'best_known_id',
    'mail_event'
]

indexToUserType = [
    'BID',
    'SID',
    'GPSAID',
    'IDFA'
]

count_without_bkd = 0
with open('./updatesFromSources') as f:
    my_lines = f.readlines()
    for line in my_lines:
        line = line.strip()
        regex_results = re.search(p, line)
        if regex_results:
            count = int(regex_results.group(3))
            sourceIndex = int(regex_results.group(1))
            userIndex = int(regex_results.group(2)) - 1
            print "%-20s %-10s %-10s" % (indexToSource[sourceIndex], indexToUserType[userIndex], locale.format('%d', count, grouping=True))


