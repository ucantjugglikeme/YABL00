def retrieve_data(reply_dict):
    attachment_str = ''
    for key, value in reply_dict.items():
        if key != 'text':
            attachment_str = ','.join([value, attachment_str])
    return attachment_str.rstrip(',')
