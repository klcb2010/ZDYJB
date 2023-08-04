'''
cron: 0 0 8 * * *
const $ = new Env("掘金签到");
'''
import os
import requests

juejin_cookie = os.getenv('juejin_cookie')

base_url = 'https://api.juejin.cn/growth_api/v1/'

headers = {

    'Accept': 'application/json',

    'Cookie': juejin_cookie

}

def _http(options):

    url = options['url']

    method = options.get('method', 'get')

    params = options.get('params', {})

    

    try:

        response = requests.request(method, url, params=params, headers=headers, timeout=30)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        print('Request failed:', e)

        return False

apis = {

    'verifyTodayStatus': {

        'url': base_url + 'get_today_status',

        'method': 'get',

        'description': '获取今天是否签到'

    },

    'checkIn': {

        'url': base_url + 'check_in',

        'method': 'post',

        'description': '开始签到'

    },

    'getSignInfo': {

        'url': base_url + 'get_counts',

        'method': 'get',

        'description': '获取签到天数状态'

    },

    'getPointCount': {

        'url': base_url + 'get_cur_point',

        'method': 'get',

        'description': '获取当前矿石数'

    },

    'getLuckyInfo': {

        'url': base_url + 'lottery_lucky/my_lucky',

        'method': 'post',

        'description': '获取幸运抽奖我的状态'

    },

    'getFreeCount': {

        'url': base_url + 'lottery_config/get',

        'method': 'get',

        'description': '获取免费次数'

    },

    'dipLucky': {

        'url': base_url + 'lottery_lucky/dip_lucky',

        'method': 'post',

        'description': '沾喜气',

        'params': {

            'lottery_history_id': '7090346718260101131'

        }

    },

    'startLottery': {

        'url': base_url + 'lottery/draw',

        'method': 'post',

        'description': '开始抽奖'

    }

}

def check_in_juejin():

    final_result = {

        'checkInStatus': False,

        'continuousDay': 0,

        'totalDay': 0,

        'oreCount': 0,

        'prize': '',

        'luckyValue': 0

    }

    

    res_verifyTodayStatus = _http(apis['verifyTodayStatus'])

    

    if res_verifyTodayStatus['err_no'] != 0:

        print('==================掘金脚本失败咯~应该需要更新cookie啦!===================')

        return

    

    if not res_verifyTodayStatus['data']:

        res_checkIn = _http(apis['checkIn'])

        if res_checkIn['err_no'] == 0:

            final_result['checkInStatus'] = True

    else:

        final_result['checkInStatus'] = True

    

    _http(apis['dipLucky']) # 沾喜气

    

    res_getFreeCount = _http(apis['getFreeCount'])

    if res_getFreeCount['data']['free_count'] != 0:

        res_startLottery = _http(apis['startLottery']) # 执行免费抽奖

        if res_startLottery['err_no'] == 0:

            final_result['prize'] = res_startLottery['data']['lottery_name']

    else:

        final_result['prize'] = None

    

    temp_user_info = [_http(apis['getSignInfo']), _http(apis['getPointCount']), _http(apis['getLuckyInfo'])]

    res_getSignInfo, res_getPointCount, res_getLuckyInfo = temp_user_info

    final_result['oreCount'] = res_getPointCount['data']

    final_result['continuousDay'] = res_getSignInfo['data']['cont_count']

    final_result['totalDay'] = res_getSignInfo['data']['sum_count']

    final_result['luckyValue'] = res_getLuckyInfo['data']['total_value']

    

    text = '''

    今日签到成功, 已连续签到 [ {} ], 累计签到 [ {} ], 当前拥有矿石 [ {} ]

    今日免费抽奖成功, {}已累计幸运值 [ {}/6000 ]

    '''.format(final_result['continuousDay'], final_result['totalDay'], final_result['oreCount'], '抽中奖品 [ '+ final_result['prize'] +' ], ' if final_result['prize'] else '', final_result['luckyValue'])

    print(text)

check_in_juejin()
