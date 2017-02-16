import pandas as pd
from bs4 import BeautifulSoup
from string import punctuation
from string import printable

cols_to_del = ['acct_type','country','currency','delivery_method', 'email_domain', 'event_created', 'event_end', 'event_published', 'event_start', 'listed', 'name', 'name_length', 'object_id', 'org_desc', 'org_name', 'payee_name', 'payout_type', 'previous_payouts', 'ticket_types', 'venue_address',\
  'venue_country', 'venue_latitude', 'venue_longitude', 'venue_name', 'venue_state']

keys = [u'approx_payout_date', u'body_length', u'channels', u'fb_published', u'gts', u'has_analytics', u'has_header', u'has_logo', u'num_order', u'num_payouts', u'org_facebook', u'org_twitter', u'sale_duration', u'sale_duration2',  u'show_map', u'user_age', \
 u'user_created', u'user_type', 'tot_cost', 'potential_cost', 'new_listed', 'pay_check', 'pay_ach', 'payee_blank', 'blank_name', 'time_to_event', 'domain_org_edu', 'domain_public', 'description']


def clean_new(data):
    open_doms = ['gmail', 'yahoo', 'ymail', 'hotmail', 'aol', 'lidf', 'live', 'rocketmail', 'yopmail', 'outlook', 'me', 'mail', 'joonbug']
    # data['delivery_method'].fillna(value=4.0, inplace=True)
    data['tot_cost'] = get_cost(data['ticket_types'])
    data['potential_cost'] = potential_cost(data['ticket_types'])
    data['new_listed'] =  0 if data['listed'] == 'n' else 1
    data['pay_check'] = 1 if data['payout_type'] == 'CHECK' else 0
    data['pay_ach'] = 1 if data['payout_type'] == 'ACH' else 0
    data['payee_blank'] = 1 if data['payout_type'] == '' else 0
    data['blank_name'] = 1 if data['payee_name'] == '' else 0
    data['time_to_event'] = data['event_start'] - data['event_created']
    data['domain_org_edu'] = 1 if '.org' in data['email_domain'] or '.edu' in data['email_domain'] else 0
    data['domain_public'] = 1 if data['email_domain'].split('.')[0] in open_doms else 0
    data = text_processing(data)
    # data['upper_case_ratio'] = data['description'].map(up_low_ratio)
    data['description'] = to_lower_case(data['description'])
    for col in cols_to_del:
        data.pop(col, None)

    v = []
    for key in keys:
        v.append(data[key])
    # data.dropna(how='any',inplace=True)
    return pd.DataFrame(data=v, index=keys).T

def get_cost(dics):
    cost = 0
    for dic in dics:
        cost += dic['cost'] * dic['quantity_sold']
    return cost

def potential_cost(dics):
    cost = 0
    for dic in dics:
        cost += dic['cost'] * dic['quantity_total']
    return cost

def up_low_ratio(text):
    count_l = 0
    count_u = 0
    for char in text:
        if char == char.upper():
            count_u += 1
        elif char == char.lower():
            count_l += 1
    if count_u + count_l > 0:
        return count_u / (count_u + count_l + 0.)
    else:
        return 0

def to_lower_case(text):
    clean = ''
    for char in text:
        clean += char.lower()
    return clean

def parse_html(content):
    soup = BeautifulSoup(content, "html.parser")
    text = ''
    for page in soup.find_all('span'):
        text += page.get_text()
    return text

def clean_text(text):
    clean = ''
    for char in text:
        if char in printable and char not in punctuation:
            clean += char
    return clean

def text_processing(df):
    df['description'] = parse_html(df['description'])
    df['description'] = clean_text(df['description'])
    return df
