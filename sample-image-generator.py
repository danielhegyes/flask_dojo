import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import get_sql
import psycopg2





img = Image.new("RGB", (512, 512), "blue")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype("sans-serif.ttf", 16)
text_options = {
    'fill': (255, 255, 255)
}

#Add your connection info here (SQL)
def get_list_from_sql(sql_statement):
    list_return = []
    database = get_sql.runSql(sql_statement, "dbname='dumbohill' user='dumbohill' host='localhost' password='sokszorkell'")
    c = 0
    for i in database:
        if database[c] == (None,):
            pass
            c += 1 
        else:
            list_return.append(database[c])
            c += 1
    return list_return
            
    
    
    
    
x = get_list_from_sql("""SELECT name FROM project""")



print(str(x[0]).strip("'(),"))

c = 0
printable = []
for i in x:
    printable.append(str(x[c]).strip("'(),"))
    c += 1

print(printable)



text_content = (str(printable))
text_size = draw.textsize(text_content)
# draw.text((x, y),text_content,(r,g,b))
draw.text((0, 0), text_content, **text_options)
draw.text((0, text_size[1]), text_content, **text_options)
draw.text((text_size[0], 0), text_content, **text_options)
draw.text(text_size, text_content, **text_options)
img.save('sample-out.png')
