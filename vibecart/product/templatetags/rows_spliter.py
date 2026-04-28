from django import template

register = template.Library()

@register.filter(name='split_rows')
def split_rows(list_data, split_rows_size):
    """_summary_
    splits list into rows
    Args:
        split_rows_size (_type_): _description_
        list_data (_type_): _description_
    Returns:
        _type_: _description_
    """
    split_rows= []
    i=0
    for data in list_data:
        split_rows.append(data)
        i=i+1
        if i == split_rows_size:
            yield split_rows
            i=0
            split_rows = []

    if split_rows:
        yield split_rows
    