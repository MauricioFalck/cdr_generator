# CDR Generator
Generates dummy CDR files using random information. 


## How to use

- Download the repo
- python3 main.py

To change the number of records and other parameters, you can update the main.py file

## Output format
- a_number: INTEGER
- a_country_code: INTEGER
- a_area_code: INTEGER
- b_number: INTEGER
- b_country_code: INTEGER
- b_area_code: INTEGER
- start_date: INTEGER (in seconds)
- end_date: INTEGER (in seconds)
- duration: INTEGER (in seconds)
- call_type: STRING
- call_result: STRING

Values are separated by '|'
