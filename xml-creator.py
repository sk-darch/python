import sys
import os
import xml.etree.ElementTree as ET

table_name = sys.argv[1]
tree = ET.parse('MYSQL.dbrep')
root = tree.getroot()

def find_table(root):
        with open('DEVMYSQL.dbrep', 'a') as f:
            for tables in root.iter():
                for table in list(tables):
                    if table.get('name') == table_name:
                        root_id = "<" + root.tag + ">\n"
                        tablelst_id = "<" + tables.tag + (str(tables.attrib)) + ">\n"
                        table_id = "<" + table.tag + (str(table.attrib)) + ">\n"
                        closing_tag = "</" + table.tag + ">" + "\n</" + tables.tag + ">"  + "\n</" + root.tag + ">"
                        table_val = root_id + tablelst_id + table_id
                        f.write(table_val)
                        for columns in list(table):
                            column_id = "<" + columns.tag + (str(columns.attrib)) + "/>\n"
                            f.write(column_id)
            f.write(closing_tag)

find_table(root)

