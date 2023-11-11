def modify_column_names(sample_array):
    for item in sample_array:
        if item['COLUMN_NAME'].endswith('Id') or item['COLUMN_NAME'].startswith('Id'):
            item['COLUMN_NAME'] = 'DINZ_' + item['COLUMN_NAME']

    return sample_array

# Example of array
sample_array = [

    {
     'TABLE_NAME': 'TABLE_ONE',
     'COLUMN_NAME': 'Id',
     'DATA_TYPE': 'Int'},
    {
        'TABLE_NAME': 'TABLE_ONE',
        'COLUMN_NAME': 'fname',
        'DATA_TYPE': 'String'
    },
    {
        'TABLE_NAME': 'TABLE_ONE',
        'COLUMN_NAME': 'lname',
        'DATA_TYPE': 'String'
    },
    {
        'TABLE_NAME': 'TABLE_ONE',
        'COLUMN_NAME': 'name_Id',
        'DATA_TYPE': 'Int'
    },

    {
        'TABLE_NAME': 'TABLE_TWO',
        'COLUMN_NAME': 'Id',
        'DATA_TYPE': 'Int'},
    {
        'TABLE_NAME': 'TABLE_TWO',
        'COLUMN_NAME': 'fname',
        'DATA_TYPE': 'String'
    },
    {
        'TABLE_NAME': 'TABLE_TWO',
        'COLUMN_NAME': 'lname',
        'DATA_TYPE': 'String'
    },
    {
        'TABLE_NAME': 'TABLE_TWO',
        'COLUMN_NAME': 'name_Id',
        'DATA_TYPE': 'Int'
    },
]

modified_array = modify_column_names(sample_array)
print(modified_array)




